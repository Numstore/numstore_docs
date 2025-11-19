<!-- Directory: /blog/entries/2025-11-23_usage-example.vue -->
<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <h1>{{ meta.title }}</h1>

    <p class="lead text-lg text-gray-700">
      Let's walk through a complete example: collecting sensor data from a temperature monitoring
      system, storing it in NumStore, and running analytics queries. This tutorial covers installation,
      data ingestion, querying, and integration with Python/NumPy.
    </p>

    <h2>The Scenario</h2>

    <p>
      You're building a smart building monitoring system with 100 temperature sensors, each
      reporting once per second. You need to:
    </p>

    <ul>
      <li>Ingest 100 samples/second (8,640,000 samples/day) with low latency</li>
      <li>Store months of historical data for trend analysis</li>
      <li>Run fast queries like "average temperature in zone 3 during business hours"</li>
      <li>Export data to Python for machine learning (anomaly detection, forecasting)</li>
    </ul>

    <h2>Step 1: Installation</h2>

    <h3>Download NumStore</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Download from https://numstore.dev/downloads/current
wget https://numstore.dev/releases/numstore-1.0.0-linux-x86_64.tar.gz
tar -xzf numstore-1.0.0-linux-x86_64.tar.gz
cd numstore-1.0.0

# Verify installation
./bin/numstore --version
# Output: NumStore v1.0.0
</code></pre>

    <h3>Install Python Bindings</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>pip install numstore
# Or build from source (see docs)
</code></pre>

    <h2>Step 2: Create a Database and Stream</h2>

    <h3>Using the CLI</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Create a new database
numstore init building_monitoring.db

# Create a stream for temperature data
numstore create-stream building_monitoring.db \
    --name temperature_sensors \
    --type float32 \
    --sample-rate 100  # 100 Hz (100 samples/sec)
</code></pre>

    <h3>Using Python</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore

# Open or create database
db = numstore.open("building_monitoring.db", create=True)

# Create a stream for temperature data
stream = db.create_stream(
    name="temperature_sensors",
    dtype=numstore.FLOAT32,
    sample_rate=100  # Hz
)

print(f"Stream created: {stream.name}")
</code></pre>

    <h2>Step 3: Ingest Sensor Data</h2>

    <h3>Simulated Sensor Data Generator</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np
import time
from datetime import datetime

# Open database and stream
db = numstore.open("building_monitoring.db")
stream = db.get_stream("temperature_sensors")

# Simulate 100 sensors reporting every second
num_sensors = 100
sample_interval = 1.0  # seconds

print("Starting data collection (Ctrl+C to stop)...")

try:
    while True:
        # Simulate temperature readings (20-25°C with noise)
        temperatures = np.random.normal(loc=22.5, scale=1.5, size=num_sensors)

        # Add timestamp metadata (current time)
        timestamp = datetime.now()

        # Write to NumStore
        stream.write(temperatures, timestamp=timestamp)

        print(f"[{timestamp}] Wrote {num_sensors} samples")

        # Wait for next interval
        time.sleep(sample_interval)

except KeyboardInterrupt:
    print("\nData collection stopped")
    stream.close()
    db.close()
</code></pre>

    <h3>Production Data Ingestion (from Real Hardware)</h3>

    <h2>Step 4: Query and Analyze Data</h2>

    <h3>Basic Range Query</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np
from datetime import datetime, timedelta

# Open database
db = numstore.open("building_monitoring.db")
stream = db.get_stream("temperature_sensors")

# Query last hour of data
end_time = datetime.now()
start_time = end_time - timedelta(hours=1)

data = stream.query(start_time=start_time, end_time=end_time)

print(f"Retrieved {len(data)} samples")
print(f"Mean temperature: {np.mean(data):.2f}°C")
print(f"Std deviation: {np.std(data):.2f}°C")
print(f"Min: {np.min(data):.2f}°C, Max: {np.max(data):.2f}°C")
</code></pre>

    <h3>Aggregation: Average by Hour</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

db = numstore.open("building_monitoring.db")
stream = db.get_stream("temperature_sensors")

# Query last 24 hours
end_time = datetime.now()
start_time = end_time - timedelta(days=1)

# Get data
data = stream.query(start_time=start_time, end_time=end_time)
timestamps = stream.query_timestamps(start_time=start_time, end_time=end_time)

# Compute hourly averages
hourly_means = []
hourly_times = []

for hour in range(24):
    hour_start = start_time + timedelta(hours=hour)
    hour_end = hour_start + timedelta(hours=1)

    # Filter data for this hour
    mask = (timestamps >= hour_start) & (timestamps < hour_end)
    hour_data = data[mask]

    if len(hour_data) > 0:
        hourly_means.append(np.mean(hour_data))
        hourly_times.append(hour_start)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(hourly_times, hourly_means, marker='o')
plt.xlabel('Time')
plt.ylabel('Average Temperature (°C)')
plt.title('24-Hour Temperature Trend')
plt.grid(True)
plt.show()
</code></pre>

    <h3>Anomaly Detection</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np
from datetime import datetime, timedelta

db = numstore.open("building_monitoring.db")
stream = db.get_stream("temperature_sensors")

# Query last 7 days for baseline
end_time = datetime.now()
start_time = end_time - timedelta(days=7)

data = stream.query(start_time=start_time, end_time=end_time)

# Compute baseline statistics
mean = np.mean(data)
std = np.std(data)

# Define anomaly threshold (3 sigma)
threshold = 3 * std

# Check recent data for anomalies
recent_start = datetime.now() - timedelta(hours=1)
recent_data = stream.query(start_time=recent_start, end_time=datetime.now())
recent_timestamps = stream.query_timestamps(start_time=recent_start, end_time=datetime.now())

# Find anomalies
anomalies = np.abs(recent_data - mean) > threshold
anomaly_count = np.sum(anomalies)

if anomaly_count > 0:
    print(f"⚠️  ALERT: {anomaly_count} anomalies detected in the last hour")
    anomaly_times = recent_timestamps[anomalies]
    anomaly_values = recent_data[anomalies]

    for t, v in zip(anomaly_times, anomaly_values):
        print(f"  [{t}] Temperature: {v:.2f}°C (expected: {mean:.2f}±{threshold:.2f}°C)")
else:
    print("✓ No anomalies detected")
</code></pre>

    <h2>Step 5: Integration with Machine Learning</h2>

    <h3>Train a Forecasting Model</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

db = numstore.open("building_monitoring.db")
stream = db.get_stream("temperature_sensors")

# Get 30 days of data
end_time = datetime.now()
start_time = end_time - timedelta(days=30)

data = stream.query(start_time=start_time, end_time=end_time)
timestamps = stream.query_timestamps(start_time=start_time, end_time=end_time)

# Convert timestamps to hours since start
hours = np.array([(t - start_time).total_seconds() / 3600 for t in timestamps])

# Create features: hour of day, day of week
hour_of_day = np.array([t.hour for t in timestamps])
day_of_week = np.array([t.weekday() for t in timestamps])

X = np.column_stack([hours, hour_of_day, day_of_week])
y = data

# Train model
model = LinearRegression()
model.fit(X, y)

print(f"Model trained on {len(data)} samples")
print(f"R² score: {model.score(X, y):.4f}")

# Predict next hour
future_time = end_time + timedelta(hours=1)
future_hours = (future_time - start_time).total_seconds() / 3600
future_X = np.array([[future_hours, future_time.hour, future_time.weekday()]])

predicted_temp = model.predict(future_X)[0]
print(f"Predicted temperature at {future_time}: {predicted_temp:.2f}°C")
</code></pre>

    <h2>Step 6: Export Data for External Analysis</h2>

    <h3>Export to CSV</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import pandas as pd
from datetime import datetime, timedelta

db = numstore.open("building_monitoring.db")
stream = db.get_stream("temperature_sensors")

# Query data
end_time = datetime.now()
start_time = end_time - timedelta(days=7)

data = stream.query(start_time=start_time, end_time=end_time)
timestamps = stream.query_timestamps(start_time=start_time, end_time=end_time)

# Create DataFrame
df = pd.DataFrame({
    'timestamp': timestamps,
    'temperature': data
})

# Export to CSV
df.to_csv('temperature_data.csv', index=False)
print(f"Exported {len(df)} samples to temperature_data.csv")
</code></pre>

    <h3>Export to Parquet (for Big Data)</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import pandas as pd
import pyarrow.parquet as pq

db = numstore.open("building_monitoring.db")
stream = db.get_stream("temperature_sensors")

# Query all data
data = stream.query_all()
timestamps = stream.query_all_timestamps()

# Create DataFrame
df = pd.DataFrame({
    'timestamp': timestamps,
    'temperature': data
})

# Export to Parquet (compressed, efficient for large datasets)
df.to_parquet('temperature_data.parquet', compression='snappy')
print(f"Exported {len(df)} samples to Parquet format")
</code></pre>

    <h2>Step 7: Real-Time Monitoring Dashboard</h2>

    <h3>Web Dashboard with Flask</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>from flask import Flask, jsonify
import numstore
import numpy as np
from datetime import datetime, timedelta

app = Flask(__name__)
db = numstore.open("building_monitoring.db")
stream = db.get_stream("temperature_sensors")

@app.route('/api/current')
def get_current_data():
    """Get last 10 minutes of data"""
    end_time = datetime.now()
    start_time = end_time - timedelta(minutes=10)

    data = stream.query(start_time=start_time, end_time=end_time)
    timestamps = stream.query_timestamps(start_time=start_time, end_time=end_time)

    return jsonify({
        'timestamps': [t.isoformat() for t in timestamps],
        'temperatures': data.tolist(),
        'stats': {
            'mean': float(np.mean(data)),
            'min': float(np.min(data)),
            'max': float(np.max(data)),
            'count': len(data)
        }
    })

@app.route('/api/hourly_summary')
def get_hourly_summary():
    """Get hourly statistics for last 24 hours"""
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)

    hourly_data = []

    for hour in range(24):
        hour_start = start_time + timedelta(hours=hour)
        hour_end = hour_start + timedelta(hours=1)

        data = stream.query(start_time=hour_start, end_time=hour_end)

        if len(data) > 0:
            hourly_data.append({
                'time': hour_start.isoformat(),
                'mean': float(np.mean(data)),
                'min': float(np.min(data)),
                'max': float(np.max(data)),
                'count': len(data)
            })

    return jsonify(hourly_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
</code></pre>

    <h2>Performance Notes</h2>

    <h3>Write Performance</h3>
    <ul>
      <li><strong>Batch writes:</strong> Writing 1000 samples at once is 10-100x faster than 1000 individual writes</li>
      <li><strong>WAL tuning:</strong> Adjust commit interval for latency vs durability trade-off</li>
      <li><strong>Throughput:</strong> On typical hardware, expect 1M-10M samples/sec sustained write rate</li>
    </ul>

    <h3>Query Performance</h3>
    <ul>
      <li><strong>Range queries:</strong> Queries aligned to chunk boundaries are fastest (e.g., hourly queries if chunks are 1 hour)</li>
      <li><strong>Zero-copy:</strong> Returned NumPy arrays are views (not copies) when possible</li>
      <li><strong>Caching:</strong> Recent queries are cached in memory for sub-millisecond response</li>
    </ul>

    <h2>Best Practices</h2>

    <ol>
      <li><strong>Batch writes:</strong> Collect samples in memory and write in batches (100-10,000 samples)</li>
      <li><strong>Choose appropriate chunk size:</strong> Default is 10,000 samples; tune based on query patterns</li>
      <li><strong>Use transactions:</strong> Wrap related writes in transactions for consistency</li>
      <li><strong>Monitor disk space:</strong> Set up automatic archival or compression for old data</li>
      <li><strong>Index metadata separately:</strong> Store sensor metadata (location, calibration) in a separate SQL database</li>
    </ol>

    <h2>Next Steps</h2>

    <p>
      This example covered the basics. For more advanced topics, check out:
    </p>

    <ul>
      <li><a href="/resources/documentation">Full API Documentation</a></li>
      <li><a href="/resources/blog/2025-11-21_rope-tree-foundation">NumStore Architecture Deep Dive</a></li>
      <li><a href="/resources/blog/2025-11-20_numstore-vs-sql">When to Use NumStore vs SQL</a></li>
      <li><a href="/services/consulting">Consulting Services</a> for production deployments</li>
    </ul>

    <h2>Get Help</h2>

    <p>
      Questions about this example or NumStore in general?
    </p>

    <ul>
      <li>📧 Email: <a href="mailto:hello@numstore.dev">hello@numstore.dev</a></li>
      <li>🎓 Academic inquiries: <a href="mailto:academic@numstore.dev">academic@numstore.dev</a></li>
      <li>📚 Documentation: <a href="/resources/documentation">/resources/documentation</a></li>
      <li>💬 Community forum: <a href="/community/forum">/community/forum</a></li>
    </ul>

    <p class="text-sm text-gray-600 mt-8">
      <em>
        Code examples are simplified for clarity. See the full documentation for error handling,
        configuration options, and production deployment best practices.
      </em>
    </p>
  </article>
</template>


<script lang="ts" setup>
const meta = {
  title: 'NumStore Usage Example: Temperature Monitoring System',
  date: '2025-11-23',
}
</script>
