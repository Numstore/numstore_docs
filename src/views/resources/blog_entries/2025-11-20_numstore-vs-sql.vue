<!-- Directory: /blog/entries/2025-11-20_numstore-vs-sql.vue -->
<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <h1>{{ meta.title }}</h1>

    <p class="lead text-lg text-gray-700">
      NumStore isn't trying to replace SQL databases. It solves a fundamentally different
      problem—one that SQL databases were never designed to address efficiently.
    </p>

    <h2>Different Problems, Different Solutions</h2>

    <p>
      SQL databases (PostgreSQL, MySQL, SQL Server, etc.) were designed for <strong>relational data</strong>—structured
      information organized into tables with relationships, where you need flexible queries, joins, and transactions
      across complex schemas.
    </p>

    <p>
      NumStore was designed for <strong>contiguous numeric arrays and time-series data</strong>—continuous streams
      of measurements, sensor readings, and numeric observations where write performance, temporal ordering, and
      efficient range queries matter most.
    </p>

    <h2>The Problem SQL Databases Weren't Built to Solve</h2>

    <h3>Scenario: High-Frequency Sensor Data Collection</h3>

    <p>
      Imagine you're collecting data from an oscilloscope sampling at 1 million samples per second.
      Each sample is a simple numeric value with a timestamp. Over an hour, that's 3.6 billion data points.
    </p>

    <p><strong>What happens with a SQL database:</strong></p>

    <ol>
      <li><strong>Row overhead is expensive:</strong> Each sample becomes a row with metadata, row ID, and index entries. A simple 8-byte float becomes 50-100 bytes of storage overhead.</li>
      <li><strong>Write amplification:</strong> B-tree indexes (used by most SQL databases) require multiple disk writes per insert, creating write amplification that can't keep up with high-frequency data.</li>
      <li><strong>Temporal fragmentation:</strong> Time-series data gets scattered across disk as B-tree nodes split and rebalance, destroying the natural contiguity of sequential measurements.</li>
      <li><strong>Query inefficiency:</strong> Range queries like "give me samples from 10:00 to 10:05" require scanning index nodes and reassembling scattered rows.</li>
    </ol>

    <p>
      <strong>Result:</strong> You drop samples, introduce latency, waste storage, and struggle with query performance—despite
      having a powerful, battle-tested SQL database.
    </p>

    <h3>What NumStore Does Differently</h3>

    <ol>
      <li><strong>Contiguous storage:</strong> Numeric arrays are stored as they arrive—contiguously in memory and on disk—preserving temporal locality.</li>
      <li><strong>R+ tree indexing:</strong> Instead of B-trees (optimized for random access), NumStore uses R+ trees designed for range queries and spatial/temporal data.</li>
      <li><strong>Zero per-sample overhead:</strong> No row metadata, no padding. A million floats = 4MB, period.</li>
      <li><strong>Write-optimized architecture:</strong> Append-only WAL with batched commits, minimizing disk I/O during high-throughput ingestion.</li>
    </ol>

    <p>
      <strong>Result:</strong> Sub-millisecond write latency, 10-100x better storage efficiency, and fast range queries
      that take advantage of data contiguity.
    </p>

    <h2>When to Use SQL vs NumStore</h2>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Use Case</th>
          <th class="text-left py-2 pr-4">Best Choice</th>
          <th class="text-left py-2">Why</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">User accounts, orders, inventory</td>
          <td class="py-2 pr-4 font-semibold text-blue-700">SQL</td>
          <td class="py-2">Relational data with complex queries and joins</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Sensor time-series (1M samples/sec)</td>
          <td class="py-2 pr-4 font-semibold text-green-700">NumStore</td>
          <td class="py-2">High write throughput, contiguous numeric data</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">E-commerce product catalog</td>
          <td class="py-2 pr-4 font-semibold text-blue-700">SQL</td>
          <td class="py-2">Structured data with relationships, transactions</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">ML training feature arrays</td>
          <td class="py-2 pr-4 font-semibold text-green-700">NumStore</td>
          <td class="py-2">Large numeric arrays, batch reads, zero-copy access</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Blog posts and comments</td>
          <td class="py-2 pr-4 font-semibold text-blue-700">SQL</td>
          <td class="py-2">Text data, relationships, flexible queries</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Financial tick data</td>
          <td class="py-2 pr-4 font-semibold text-green-700">NumStore</td>
          <td class="py-2">Ordered time-series, range queries, fast writes</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Customer support tickets</td>
          <td class="py-2 pr-4 font-semibold text-blue-700">SQL</td>
          <td class="py-2">Relational data with status tracking and joins</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Equipment telemetry metrics</td>
          <td class="py-2 pr-4 font-semibold text-green-700">NumStore</td>
          <td class="py-2">Continuous numeric streams, time-based queries</td>
        </tr>
      </tbody>
    </table>

    <h2>A Concrete Example: Storing Oscilloscope Data</h2>

    <h3>The Data</h3>
    <p>
      You're capturing voltage measurements from an oscilloscope:
    </p>
    <ul>
      <li>Sample rate: 1 MHz (1 million samples/second)</li>
      <li>Data type: 32-bit float (voltage in volts)</li>
      <li>Duration: 1 hour</li>
      <li>Total samples: 3,600,000,000 samples</li>
    </ul>

    <h3>PostgreSQL Approach</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>CREATE TABLE samples (
  id BIGSERIAL PRIMARY KEY,
  timestamp TIMESTAMPTZ NOT NULL,
  voltage REAL NOT NULL
);

CREATE INDEX idx_timestamp ON samples(timestamp);

-- Insert samples (simplified)
INSERT INTO samples (timestamp, voltage)
VALUES ('2025-11-20 10:00:00.000000', 1.234),
       ('2025-11-20 10:00:00.000001', 1.235),
       ...;
</code></pre>

    <p><strong>Storage requirements:</strong></p>
    <ul>
      <li>Raw data: 3.6B × 4 bytes = 14.4 GB</li>
      <li>Timestamp: 3.6B × 8 bytes = 28.8 GB</li>
      <li>Row ID: 3.6B × 8 bytes = 28.8 GB</li>
      <li>Index: ~30-40 GB (B-tree overhead)</li>
      <li><strong>Total: ~100-110 GB</strong></li>
    </ul>

    <p><strong>Write performance:</strong></p>
    <ul>
      <li>Typical PostgreSQL: 10,000-50,000 inserts/sec (with indexes)</li>
      <li>Time to ingest 3.6B rows: <strong>20-100 hours</strong></li>
      <li>Dropped samples: Likely, unless you batch and sacrifice real-time guarantees</li>
    </ul>

    <h3>NumStore Approach</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>// Create a time-series stream
numstore_stream_t *stream = numstore_create_stream(
    "oscilloscope_ch1",
    NUMSTORE_TYPE_FLOAT32,
    1000000  // 1 MHz sample rate
);

// Write samples in batches (pseudo-code)
float samples[10000];
while (collecting) {
    read_from_scope(samples, 10000);
    numstore_write(stream, samples, 10000);
}
</code></pre>

    <p><strong>Storage requirements:</strong></p>
    <ul>
      <li>Raw data: 3.6B × 4 bytes = 14.4 GB</li>
      <li>R+ tree index: ~2-3 GB (spatial/temporal indexing)</li>
      <li>WAL overhead: ~1-2 GB (amortized)</li>
      <li><strong>Total: ~18-20 GB</strong></li>
    </ul>

    <p><strong>Write performance:</strong></p>
    <ul>
      <li>NumStore throughput: 1-10 million samples/sec (depending on hardware)</li>
      <li>Time to ingest 3.6B samples: <strong>6 minutes to 1 hour</strong></li>
      <li>Dropped samples: None (even at 1 MHz sustained rate)</li>
    </ul>

    <h3>Query Performance</h3>

    <p><strong>Task:</strong> "Get all samples between 10:00:00 and 10:00:05" (5 million samples)</p>

    <p><strong>PostgreSQL:</strong></p>
    <ul>
      <li>Index scan to find start/end range</li>
      <li>Retrieve scattered rows from heap</li>
      <li>Reconstruct result set</li>
      <li>Query time: <strong>5-30 seconds</strong> (depending on cache hit rate)</li>
    </ul>

    <p><strong>NumStore:</strong></p>
    <ul>
      <li>R+ tree lookup to find contiguous segment</li>
      <li>Direct memory/disk read (sequential I/O)</li>
      <li>Zero-copy return to application</li>
      <li>Query time: <strong>50-200 milliseconds</strong></li>
    </ul>

    <h2>NumStore Is Not Anti-SQL</h2>

    <p>
      This isn't about NumStore being "better" than SQL databases. It's about using the right tool for the job.
    </p>

    <p>
      SQL databases are incredible for what they do—relational data, ACID transactions, flexible queries, and
      decades of proven reliability. I use PostgreSQL for user accounts, configuration, and metadata.
    </p>

    <p>
      But when the problem is "store millions of numeric samples per second with sub-millisecond latency and
      fast range queries," you need a database designed specifically for that workload.
    </p>

    <p>
      That's NumStore.
    </p>

    <h2>Hybrid Architectures Work Best</h2>

    <p>
      In practice, most systems use both:
    </p>

    <ul>
      <li><strong>PostgreSQL:</strong> Device metadata, user accounts, configuration, calibration parameters</li>
      <li><strong>NumStore:</strong> Raw sensor time-series, measurement data, continuous numeric streams</li>
    </ul>

    <p>
      Each database does what it's best at, and together they provide a complete solution.
    </p>

    <h2>Try It Yourself</h2>

    <p>
      If you're currently using a SQL database for time-series or numeric data and hitting performance
      limits, give NumStore a try.
    </p>

    <p>
      Download: <a href="/downloads/current">Get NumStore</a><br>
      Documentation: <a href="/resources/documentation">Read the Docs</a><br>
      Questions: <a href="mailto:hello@numstore.dev">hello@numstore.dev</a>
    </p>

    <p class="text-sm text-gray-600 mt-8">
      <em>Note: All performance numbers are approximate and depend on hardware, configuration, and workload characteristics.
      Run your own benchmarks with your actual data for accurate comparisons.</em>
    </p>
  </article>
</template>


<script lang="ts" setup>
const meta = {
  title: 'Why NumStore vs SQL: Solving a Problem Databases Weren\'t Built For',
  date: '2025-11-20',
}
</script>
