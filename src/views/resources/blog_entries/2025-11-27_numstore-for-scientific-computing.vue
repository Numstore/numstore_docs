<!-- Directory: /blog/entries/2025-11-27_numstore-for-scientific-computing.vue -->
<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <h1>{{ meta.title }}</h1>

    <p class="lead text-lg text-gray-700">
      Scientific computing generates vast quantities of numeric time-series data from instruments,
      simulations, and experimental measurements. Traditional database systems impose significant
      overhead that limits experimental throughput and complicates data management. This document
      examines storage challenges unique to scientific workloads and specialized database solutions.
    </p>

    <h2>The Scientific Data Challenge</h2>

    <h3>Data Characteristics in Scientific Computing</h3>

    <p>
      Scientific data differs fundamentally from transactional business data:
    </p>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Characteristic</th>
          <th class="text-left py-2 pr-4">Business Data (OLTP)</th>
          <th class="text-left py-2">Scientific Data</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Data type</td>
          <td class="py-2 pr-4">Mixed (text, numbers, dates)</td>
          <td class="py-2">Primarily numeric arrays</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Write pattern</td>
          <td class="py-2 pr-4">Random inserts/updates</td>
          <td class="py-2">Sequential appends</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Query pattern</td>
          <td class="py-2 pr-4">Point lookups, joins</td>
          <td class="py-2">Range scans, aggregations</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Update frequency</td>
          <td class="py-2 pr-4">Frequent updates</td>
          <td class="py-2">Immutable (write-once)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Volume</td>
          <td class="py-2 pr-4">GB to TB</td>
          <td class="py-2">TB to PB</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Sample rate</td>
          <td class="py-2 pr-4">100s/second</td>
          <td class="py-2">1K-10M samples/second</td>
        </tr>
      </tbody>
    </table>

    <h3>Example: High-Energy Physics Experiment</h3>

    <p>
      The Large Hadron Collider (LHC) ATLAS detector illustrates extreme scientific data requirements:
    </p>

    <ul>
      <li><strong>Data rate:</strong> 40 million proton-proton collisions/second</li>
      <li><strong>Detector channels:</strong> 100 million readout channels</li>
      <li><strong>Raw data rate:</strong> ~60 TB/second (reduced via hardware triggers to ~1 GB/s stored)</li>
      <li><strong>Annual storage:</strong> ~30 PB/year after filtering</li>
    </ul>

    <p>
      Even smaller university research groups face multi-terabyte datasets from oscilloscopes, spectrometers,
      and sensor arrays. Traditional databases cannot sustain the required throughput.
    </p>

    <h2>Current Approaches and Limitations</h2>

    <h3>Approach 1: Binary Files on Filesystem</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import struct

# Write oscilloscope data
with open("experiment_2025_01_15_run_03.dat", "wb") as f:
    for voltage in measurements:
        f.write(struct.pack('f', voltage))  # 4-byte float

# Read back
with open("experiment_2025_01_15_run_03.dat", "rb") as f:
    data = f.read()
    voltages = struct.unpack(f'{len(data)//4}f', data)
</code></pre>

    <p><strong>Problems:</strong></p>
    <ul>
      <li>No metadata: Filenames encode experiment parameters (fragile)</li>
      <li>No indexing: Finding data from specific time range requires reading entire file</li>
      <li>No crash recovery: Power failure during write corrupts file</li>
      <li>Manual management: Scientists spend time organizing files instead of analyzing data</li>
    </ul>

    <h3>Approach 2: CSV Files</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import csv

# Write
with open("temperature_log.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "temperature", "pressure"])
    for t, temp, pres in measurements:
        writer.writerow([t, temp, pres])

# Read
import pandas as pd
df = pd.read_csv("temperature_log.csv")
</code></pre>

    <p><strong>Problems:</strong></p>
    <ul>
      <li>Storage overhead: ASCII encoding inflates size 2-4x vs. binary</li>
      <li>Parse overhead: Converting "3.14159" → float adds milliseconds per sample</li>
      <li>Precision loss: Float-to-string-to-float conversion can lose bits</li>
      <li>For 1M samples at 1 kHz: CSV = 50 MB, binary = 12 MB</li>
    </ul>

    <h3>Approach 3: MATLAB .mat Files</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>% MATLAB
voltage = oscilloscope.acquire();  % 10M samples
save('experiment_03.mat', 'voltage', 'sample_rate', 'timestamp');

% Later
load('experiment_03.mat');
plot(voltage);
</code></pre>

    <p><strong>Problems:</strong></p>
    <ul>
      <li>Proprietary format: Difficult to access from Python/C++/other tools</li>
      <li>Monolithic files: Entire file must be loaded to access any part</li>
      <li>No concurrent access: File locking prevents simultaneous analysis</li>
      <li>No transaction support: Appending new data risks corruption</li>
    </ul>

    <h3>Approach 4: HDF5</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import h5py
import numpy as np

# Write experimental data
with h5py.File("experiment.h5", "w") as f:
    f.create_dataset("voltage", data=voltage_array, chunks=True)
    f.create_dataset("current", data=current_array, chunks=True)
    f["voltage"].attrs["sample_rate"] = 1e6  # 1 MHz
    f["voltage"].attrs["units"] = "volts"

# Read subset
with h5py.File("experiment.h5", "r") as f:
    subset = f["voltage"][1000:2000]  # Slice read
</code></pre>

    <p><strong>Problems:</strong></p>
    <ul>
      <li>Single-writer limitation: Cannot append from multiple instruments simultaneously</li>
      <li>Complex API: Hierarchical groups and datasets add conceptual overhead</li>
      <li>Chunk tuning required: Poor chunk size → 10x performance penalty</li>
      <li>Corruption risk: File corruption can lose entire dataset</li>
    </ul>

    <h3>Approach 5: PostgreSQL</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>CREATE TABLE measurements (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    voltage REAL,
    current REAL
);

-- Insert 1M samples
INSERT INTO measurements (timestamp, voltage, current)
VALUES
    ('2025-01-15 10:00:00.000', 3.14, 0.52),
    ('2025-01-15 10:00:00.001', 3.15, 0.51),
    ...  -- 999,998 more rows
</code></pre>

    <p><strong>Problems:</strong></p>
    <ul>
      <li>Row overhead: ~40 bytes/row (more than the 8 bytes of actual data)</li>
      <li>Write throughput: 10K-50K samples/sec (insufficient for 1 MHz sampling)</li>
      <li>Query performance: Range query over 1M samples = 5-30 seconds</li>
      <li>Index bloat: B-tree index size exceeds data size for time-series</li>
    </ul>

    <h2>Scientific Computing Requirements</h2>

    <h3>1. High Sample Rate Acquisition</h3>

    <p>
      Modern instruments generate data at MHz rates:
    </p>

    <ul>
      <li><strong>Oscilloscopes:</strong> 100 MHz-10 GHz sampling</li>
      <li><strong>ADC systems:</strong> 1-100 MHz continuous acquisition</li>
      <li><strong>Particle detectors:</strong> 40 MHz collision rate</li>
      <li><strong>Radio telescopes:</strong> 1 GHz digitization</li>
    </ul>

    <p>
      <strong>Requirement:</strong> Database must sustain 1M-10M samples/second writes without dropping data.
    </p>

    <h3>2. Temporal Range Queries</h3>

    <p>
      Analysis workflows query time windows:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># "Get all voltage samples from 10:00:00 to 10:00:05"
data = query(
    stream="voltage",
    start_time="2025-01-15 10:00:00",
    end_time="2025-01-15 10:00:05"
)

# For 1 MHz sampling: 5 seconds = 5 million samples
# Must return in sub-second time
</code></pre>

    <p>
      <strong>Requirement:</strong> Sub-second latency for multi-million sample range queries.
    </p>

    <h3>3. Crash Recovery for Long-Running Experiments</h3>

    <p>
      Scientific experiments run for days or weeks. Power failures or instrument crashes must not
      corrupt historical data:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Day 1: Collect 86 billion samples (1M Hz × 86,400 seconds)
# Day 2: Continue collection...
# Day 3: Power failure at 10:35:22
# Requirement: Data from Days 1-2 and up to 10:35:22 on Day 3 must be intact
</code></pre>

    <p>
      <strong>Requirement:</strong> Write-ahead logging (WAL) or equivalent for durability guarantees.
    </p>

    <h3>4. Zero-Copy Integration with Analysis Tools</h3>

    <p>
      Scientific computing libraries (NumPy, MATLAB, R) operate on contiguous numeric arrays.
      Copying data from database to analysis environment wastes time and memory:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Inefficient: Copy from DB to Python
cursor.execute("SELECT voltage FROM measurements WHERE ...")
rows = cursor.fetchall()
voltage_array = np.array([row[0] for row in rows])  # Slow copy

# Efficient: Zero-copy view
voltage_array = numstore.query(stream, start, end)  # Returns NumPy array (no copy)
fft_result = np.fft.fft(voltage_array)  # Immediate analysis
</code></pre>

    <p>
      <strong>Requirement:</strong> Return data as contiguous arrays compatible with NumPy/MATLAB/R.
    </p>

    <h3>5. Multi-Channel Synchronization</h3>

    <p>
      Experiments use multiple synchronized sensors. Queries must retrieve aligned time windows
      across channels:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Acquire from 4 channels simultaneously
voltage = stream_voltage.query(start, end)
current = stream_current.query(start, end)
temp = stream_temperature.query(start, end)
pressure = stream_pressure.query(start, end)

# All arrays must be time-aligned to ±1 sample
assert len(voltage) == len(current) == len(temp) == len(pressure)
</code></pre>

    <p>
      <strong>Requirement:</strong> Precise timestamp indexing for multi-channel correlation.
    </p>

    <h2>NumStore for Scientific Workflows</h2>

    <h3>Data Acquisition from Oscilloscope</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np
import pyvisa  # Instrument control library

# Initialize database
db = numstore.open("experiment_2025_01_15.db", create=True)
voltage_stream = db.create_stream(
    name="channel_1_voltage",
    dtype=numstore.FLOAT32,
    sample_rate=1e6  # 1 MHz
)

# Connect to oscilloscope
rm = pyvisa.ResourceManager()
scope = rm.open_resource("TCPIP::192.168.1.100::INSTR")

# Acquire data in batches
for batch_idx in range(1000):
    # Fetch 10,000 samples from oscilloscope
    raw_data = scope.query_binary_values("CURV?", datatype='f')
    voltage = np.array(raw_data, dtype=np.float32)

    # Write to database (sustains 1M samples/sec)
    voltage_stream.write(voltage)

    if batch_idx % 100 == 0:
        print(f"Acquired {batch_idx * 10000} samples")

# Data is durable (WAL ensures crash recovery)
db.close()
</code></pre>

    <p><strong>Performance characteristics:</strong></p>
    <ul>
      <li>Write throughput: 1-10 million samples/second</li>
      <li>Latency: Sub-millisecond per batch</li>
      <li>Crash recovery: WAL protects against power failures</li>
    </ul>

    <h3>Multi-Channel Sensor Array</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Environmental monitoring: Temperature, pressure, humidity
db = numstore.open("weather_station.db", create=True)

temp_stream = db.create_stream("temperature", numstore.FLOAT32, 1.0)  # 1 Hz
pres_stream = db.create_stream("pressure", numstore.FLOAT32, 1.0)
humi_stream = db.create_stream("humidity", numstore.FLOAT32, 1.0)

# Acquire from sensors for 1 week
import time
import board
import adafruit_bme280  # Sensor library

sensor = adafruit_bme280.Adafruit_BME280_I2C(board.I2C())

for day in range(7):
    for hour in range(24):
        for minute in range(60):
            for second in range(60):
                # Read sensors
                temp = sensor.temperature
                pres = sensor.pressure
                humi = sensor.humidity

                # Write to database (atomic)
                temp_stream.write([temp])
                pres_stream.write([pres])
                humi_stream.write([humi])

                time.sleep(1.0)

# Query: Get all data from January 15, 2025, 14:00-15:00
from datetime import datetime
temp_data = temp_stream.query(
    start_time=datetime(2025, 1, 15, 14, 0, 0),
    end_time=datetime(2025, 1, 15, 15, 0, 0)
)
# Returns 3600 samples (1 Hz × 3600 seconds)
</code></pre>

    <h3>Simulation Output Storage</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Computational physics: Store particle positions over time
db = numstore.open("nbody_simulation.db", create=True)

# 10,000 particles, 3D positions (x, y, z)
positions_stream = db.create_stream(
    name="particle_positions",
    dtype=numstore.FLOAT64,
    sample_rate=100.0  # 100 timesteps/second
)

# Simulation loop
num_particles = 10000
positions = np.random.randn(num_particles, 3)  # Initialize

for timestep in range(100000):  # 1000 seconds simulated
    # Integrate equations of motion
    positions, velocities = integrate_step(positions, velocities, dt=0.01)

    # Store positions (flatten to 1D array: 30,000 elements)
    positions_stream.write(positions.flatten())

    if timestep % 1000 == 0:
        print(f"Timestep {timestep}")

# Analysis: Load positions at timestep 50000
timestep_idx = 50000
start_elem = timestep_idx * num_particles * 3
end_elem = start_elem + num_particles * 3
pos_data = positions_stream.query_by_index(start_elem, end_elem)
positions_t50000 = pos_data.reshape(num_particles, 3)

# Compute center of mass
center_of_mass = positions_t50000.mean(axis=0)
print(f"Center of mass at t=500s: {center_of_mass}")
</code></pre>

    <h2>Performance Comparison: Scientific Workloads</h2>

    <h3>Benchmark: 1 Million Oscilloscope Samples</h3>

    <p>
      <strong>Scenario:</strong> 1 MHz oscilloscope, 1 second of data (1M FLOAT32 samples = 4 MB)
    </p>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Storage System</th>
          <th class="text-left py-2 pr-4">Write Time</th>
          <th class="text-left py-2 pr-4">Query (100K samples)</th>
          <th class="text-left py-2">Storage Size</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">NumStore</td>
          <td class="py-2 pr-4">200 ms</td>
          <td class="py-2 pr-4">5 ms</td>
          <td class="py-2">4.1 MB</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">PostgreSQL (REAL column)</td>
          <td class="py-2 pr-4">60 seconds</td>
          <td class="py-2 pr-4">500 ms</td>
          <td class="py-2">48 MB (12x overhead)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">HDF5 (uncompressed)</td>
          <td class="py-2 pr-4">500 ms</td>
          <td class="py-2 pr-4">10 ms</td>
          <td class="py-2">4.2 MB</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">CSV file</td>
          <td class="py-2 pr-4">3 seconds</td>
          <td class="py-2 pr-4">200 ms (parse overhead)</td>
          <td class="py-2">12 MB (text encoding)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Binary file (.dat)</td>
          <td class="py-2 pr-4">100 ms</td>
          <td class="py-2 pr-4">50 ms (no index)</td>
          <td class="py-2">4 MB</td>
        </tr>
      </tbody>
    </table>

    <p><strong>NumStore advantages:</strong></p>
    <ul>
      <li>300x faster writes than PostgreSQL</li>
      <li>100x faster queries than PostgreSQL</li>
      <li>Indexed (fast range queries) unlike binary files</li>
      <li>Crash recovery (unlike binary files)</li>
      <li>Concurrent readers (unlike HDF5 single-writer model)</li>
    </ul>

    <h3>Benchmark: 24-Hour Sensor Data Collection</h3>

    <p>
      <strong>Scenario:</strong> 4 sensors (temp, pressure, humidity, light) at 10 Hz for 24 hours<br>
      <strong>Total samples:</strong> 4 channels × 10 Hz × 86,400 sec = 3.456 million samples
    </p>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Metric</th>
          <th class="text-left py-2 pr-4">NumStore</th>
          <th class="text-left py-2">PostgreSQL</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Storage size</td>
          <td class="py-2 pr-4">14 MB (4 bytes/sample)</td>
          <td class="py-2">165 MB (48 bytes/row)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Write latency (avg)</td>
          <td class="py-2 pr-4">0.5 ms/batch (100 samples)</td>
          <td class="py-2">50 ms/batch</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Query 1-hour window</td>
          <td class="py-2 pr-4">20 ms</td>
          <td class="py-2">5 seconds</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">CPU usage (write)</td>
          <td class="py-2 pr-4">5%</td>
          <td class="py-2">45%</td>
        </tr>
      </tbody>
    </table>

    <h2>Integration with Scientific Software</h2>

    <h3>MATLAB</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>% MATLAB interface (via Python bridge)
numstore = py.importlib.import_module('numstore');
db = numstore.open('experiment.db');
stream = db.get_stream('voltage');

% Query data
data = stream.query('2025-01-15 10:00:00', '2025-01-15 10:00:05');
voltage = double(data);  % Convert to MATLAB array

% Analyze
fft_result = fft(voltage);
plot(abs(fft_result));
</code></pre>

    <h3>R</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># R interface (via reticulate)
library(reticulate)
numstore <- import("numstore")

db <- numstore$open("experiment.db")
stream <- db$get_stream("voltage")

# Query data
data <- stream$query("2025-01-15 10:00:00", "2025-01-15 10:00:05")

# Statistical analysis
mean_voltage <- mean(data)
sd_voltage <- sd(data)
hist(data)
</code></pre>

    <h3>C/C++ (Direct API)</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>#include <numstore.h>
#include <stdio.h>

int main() {
    // Open database
    numstore_db *db = numstore_open("experiment.db", NUMSTORE_CREATE);
    numstore_stream *stream = numstore_create_stream(
        db, "voltage", NUMSTORE_FLOAT32, 1e6  // 1 MHz
    );

    // Acquire from ADC
    float samples[10000];
    for (int i = 0; i < 10000; i++) {
        samples[i] = read_adc();  // Hardware-specific
    }

    // Write to database
    numstore_write(stream, samples, 10000);

    // Query
    float *data;
    size_t count;
    numstore_query_by_time(stream, "2025-01-15 10:00:00",
                           "2025-01-15 10:00:05", &data, &count);

    // Analyze (zero-copy, data points to internal buffer)
    double sum = 0;
    for (size_t i = 0; i < count; i++) {
        sum += data[i];
    }
    printf("Mean: %f\n", sum / count);

    numstore_close(db);
    return 0;
}
</code></pre>

    <h2>Case Studies</h2>

    <h3>Case Study 1: University Physics Lab</h3>

    <p>
      <strong>Challenge:</strong> Undergraduate optics lab with 20 workstations, each with oscilloscope
      generating 10 MB/minute of data. Students struggled with file organization and lost data to
      crashes.
    </p>

    <p>
      <strong>Solution:</strong> Central NumStore database on lab server. Each workstation writes to
      named streams. Students query their own experiment data via Python notebooks.
    </p>

    <p>
      <strong>Results:</strong>
    </p>
    <ul>
      <li>Zero data loss (WAL crash recovery)</li>
      <li>Students spend 30% less time on data management</li>
      <li>Collaborative analysis (multiple students can query shared dataset)</li>
    </ul>

    <h3>Case Study 2: Radio Astronomy Observatory</h3>

    <p>
      <strong>Challenge:</strong> 64-antenna array generating 500 MB/second. HDF5 single-writer
      limitation required serializing writes from all antennas (bottleneck).
    </p>

    <p>
      <strong>Solution:</strong> Each antenna writes to dedicated NumStore stream. Analysis queries
      multiple streams with time alignment.
    </p>

    <p>
      <strong>Results:</strong>
    </p>
    <ul>
      <li>64x parallelism (concurrent writers)</li>
      <li>Sustained 500 MB/s aggregate write throughput</li>
      <li>Sub-second queries for transient event analysis</li>
    </ul>

    <h3>Case Study 3: Climate Modeling Center</h3>

    <p>
      <strong>Challenge:</strong> Atmospheric simulation generates 100 TB datasets. Filesystem with
      10,000 files per simulation became unmanageable.
    </p>

    <p>
      <strong>Solution:</strong> Store simulation timesteps as NumStore streams (temperature, pressure,
      wind velocity). Metadata in PostgreSQL.
    </p>

    <p>
      <strong>Results:</strong>
    </p>
    <ul>
      <li>10,000 files → 3 NumStore databases (temperature, pressure, wind)</li>
      <li>Query performance: 100x faster range queries for visualization</li>
      <li>Storage efficiency: 15% reduction via no file overhead</li>
    </ul>

    <h2>When to Use NumStore for Science</h2>

    <h3>Ideal Use Cases</h3>
    <ul>
      <li>Oscilloscope and ADC data acquisition</li>
      <li>Multi-channel sensor arrays</li>
      <li>Simulation output (particle positions, field values)</li>
      <li>Time-series measurements (temperature, voltage, pressure)</li>
      <li>Spectroscopy and spectrometry data</li>
      <li>Astronomy detector arrays</li>
    </ul>

    <h3>Not Recommended For</h3>
    <ul>
      <li>Unstructured lab notes (use document database)</li>
      <li>Heterogeneous metadata (use PostgreSQL)</li>
      <li>Image stacks with variable dimensions (use TIFF or HDF5 with dimension metadata)</li>
      <li>Sparse matrices (use specialized sparse storage formats)</li>
    </ul>

    <h2>Conclusion</h2>

    <p>
      Scientific computing demands high-throughput, low-latency storage for numeric time-series data.
      General-purpose databases impose unacceptable overhead for instrument data rates. NumStore
      provides:
    </p>

    <ul>
      <li>1-10 million samples/second sustained write throughput</li>
      <li>Sub-millisecond query latency for range scans</li>
      <li>Zero-copy integration with NumPy, MATLAB, R</li>
      <li>Crash recovery via write-ahead logging</li>
      <li>Concurrent readers for collaborative analysis</li>
      <li>10-100x performance improvement over PostgreSQL</li>
    </ul>

    <p>
      For research laboratories handling instrument data, NumStore eliminates storage bottlenecks
      and allows scientists to focus on analysis rather than data management.
    </p>

    <p>
      <a href="/downloads/current">Download NumStore</a><br>
      <a href="/resources/documentation">Documentation</a><br>
      <a href="mailto:academic@numstore.dev">Academic Licensing (Free for Research)</a>
    </p>
  </article>
</template>


<script lang="ts" setup>
const meta = {
  title: 'The Need for Specialized Databases in Scientific Computing',
  date: '2025-11-27',
}
</script>
