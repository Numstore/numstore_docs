<!-- Directory: /blog/entries/2025-11-19_numstore-usages.vue -->
<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <h1>{{ meta.title }}</h1>

    <p class="lead text-lg text-gray-700">
      NumStore excels at storing and querying numeric, time-series, and contiguous array data.
      Here's where it shines—and where it might not be the best fit.
    </p>

    <h2>Ideal Use Cases</h2>

    <h3>1. Scientific Data Collection</h3>
    <p>
      <strong>Problem:</strong> Research labs collect massive amounts of numeric data from
      instruments—oscilloscopes, spectrometers, particle detectors, sensors—and need to store
      it reliably with minimal latency.
    </p>
    <p>
      <strong>NumStore solution:</strong> High-throughput writes with sub-millisecond latency,
      efficient storage of contiguous numeric arrays, and native support for time-series indexing.
    </p>
    <p>
      <strong>Example applications:</strong>
    </p>
    <ul>
      <li>Physics experiments (CERN-style particle collision data)</li>
      <li>Astronomy telescope data pipelines</li>
      <li>Environmental monitoring stations</li>
      <li>Neuroscience electrophysiology recordings</li>
      <li>Material science characterization data</li>
    </ul>

    <h3>2. Industrial IoT and Sensor Networks</h3>
    <p>
      <strong>Problem:</strong> Industrial systems generate continuous streams of sensor
      data (temperature, pressure, vibration, power consumption) that must be captured
      without loss, even under high load.
    </p>
    <p>
      <strong>NumStore solution:</strong> Embedded deployment, minimal resource overhead,
      and write-optimized architecture that handles bursts without dropping samples.
    </p>
    <p>
      <strong>Example applications:</strong>
    </p>
    <ul>
      <li>Manufacturing equipment monitoring</li>
      <li>Smart building HVAC optimization</li>
      <li>Oil & gas pipeline monitoring</li>
      <li>Renewable energy plant telemetry</li>
      <li>Predictive maintenance systems</li>
    </ul>

    <h3>3. Financial Time-Series</h3>
    <p>
      <strong>Problem:</strong> Trading systems and financial analytics require microsecond-level
      precision and guaranteed ordering for tick data, quotes, and trades.
    </p>
    <p>
      <strong>NumStore solution:</strong> Contiguous storage model preserves temporal ordering,
      R+ tree indexing enables fast range queries, and WAL ensures no data loss during market hours.
    </p>
    <p>
      <strong>Example applications:</strong>
    </p>
    <ul>
      <li>Market data collection and replay systems</li>
      <li>High-frequency trading backtesting</li>
      <li>Risk analytics on historical tick data</li>
      <li>Order book reconstruction</li>
      <li>Regulatory compliance and audit trails</li>
    </ul>

    <h3>4. Machine Learning Feature Stores</h3>
    <p>
      <strong>Problem:</strong> ML training pipelines need fast access to large numeric feature
      arrays and time-series data, often requiring batch reads of millions of samples.
    </p>
    <p>
      <strong>NumStore solution:</strong> Contiguous storage allows zero-copy reads of numeric
      arrays, perfect for feeding directly into NumPy, PyTorch, or TensorFlow.
    </p>
    <p>
      <strong>Example applications:</strong>
    </p>
    <ul>
      <li>Training data versioning and lineage</li>
      <li>Feature engineering pipelines</li>
      <li>Model serving with real-time feature lookup</li>
      <li>A/B testing with historical replay</li>
      <li>Embedding vector storage for similarity search</li>
    </ul>

    <h3>5. Observability and Telemetry</h3>
    <p>
      <strong>Problem:</strong> Modern applications emit millions of metrics per second
      (CPU, memory, latency, throughput) that must be ingested, indexed, and queried for
      dashboards and alerting.
    </p>
    <p>
      <strong>NumStore solution:</strong> Write-optimized for high-cardinality metrics,
      efficient time-based queries, and low storage overhead for numeric time-series.
    </p>
    <p>
      <strong>Example applications:</strong>
    </p>
    <ul>
      <li>Application performance monitoring (APM)</li>
      <li>Infrastructure monitoring (Prometheus-style)</li>
      <li>Distributed tracing backends</li>
      <li>Real user monitoring (RUM) analytics</li>
      <li>Service level indicator (SLI) tracking</li>
    </ul>

    <h3>6. Medical and Healthcare Data</h3>
    <p>
      <strong>Problem:</strong> Medical devices generate continuous waveforms (ECG, EEG, vital signs)
      that require reliable storage with audit trails for regulatory compliance.
    </p>
    <p>
      <strong>NumStore solution:</strong> ACID guarantees, rollback support for data corrections,
      and efficient storage of physiological waveforms.
    </p>
    <p>
      <strong>Example applications:</strong>
    </p>
    <ul>
      <li>Patient monitoring systems</li>
      <li>Medical imaging metadata and measurements</li>
      <li>Clinical trial data collection</li>
      <li>Wearable health device backends</li>
      <li>Sleep study and polysomnography data</li>
    </ul>

    <h3>7. Geospatial and Environmental Monitoring</h3>
    <p>
      <strong>Problem:</strong> Environmental sensors, GPS trackers, and weather stations
      produce continuous time-stamped numeric data that must be queried by time and location.
    </p>
    <p>
      <strong>NumStore solution:</strong> R+ tree spatial indexing (originally designed for
      geographic data), time-series support, and efficient range queries.
    </p>
    <p>
      <strong>Example applications:</strong>
    </p>
    <ul>
      <li>Weather station networks</li>
      <li>Air quality monitoring</li>
      <li>Fleet tracking and logistics</li>
      <li>Wildlife GPS collar data</li>
      <li>Earthquake and seismic monitoring</li>
    </ul>

    <h2>Where NumStore Might Not Be the Best Fit</h2>

    <p>
      NumStore is specialized for numeric and time-series workloads. It's <em>not</em> designed for:
    </p>

    <ul>
      <li><strong>Document storage:</strong> Use MongoDB, PostgreSQL JSON, or Elasticsearch for flexible schema documents</li>
      <li><strong>Relational data with complex joins:</strong> Use PostgreSQL, MySQL, or other RDBMS for normalized relational data</li>
      <li><strong>Full-text search:</strong> Use Elasticsearch or Solr for text indexing and search</li>
      <li><strong>Graph queries:</strong> Use Neo4j, DGraph, or other graph databases for relationship-heavy data</li>
      <li><strong>Key-value caching:</strong> Use Redis or Memcached for simple key-value workloads</li>
    </ul>

    <h2>Hybrid Architectures</h2>

    <p>
      Many real-world systems combine NumStore with other databases:
    </p>

    <ul>
      <li><strong>NumStore + PostgreSQL:</strong> NumStore for sensor time-series, PostgreSQL for device metadata and configuration</li>
      <li><strong>NumStore + Redis:</strong> NumStore for long-term storage, Redis for real-time aggregation caching</li>
      <li><strong>NumStore + S3:</strong> NumStore for active data, S3 for cold archival</li>
      <li><strong>NumStore + Elasticsearch:</strong> NumStore for raw metrics, Elasticsearch for log correlation</li>
    </ul>

    <h2>Getting Started</h2>

    <p>
      If your use case involves:
    </p>
    <ul>
      <li>✅ Primarily numeric or time-series data</li>
      <li>✅ High write throughput requirements</li>
      <li>✅ Fast range queries by time or numeric value</li>
      <li>✅ Need for embedded deployment or language flexibility</li>
    </ul>

    <p>
      ...then NumStore is likely a great fit.
    </p>

    <p>
      Download NumStore and try it with your workload: <a href="/downloads/current">Get Started</a>
    </p>

    <p>
      Have questions about whether NumStore fits your use case? Email us at
      <a href="mailto:hello@numstore.dev">hello@numstore.dev</a> or check out our
      <a href="/resources/documentation">documentation</a>.
    </p>
  </article>
</template>


<script lang="ts" setup>
const meta = {
  title: 'NumStore Use Cases: Where It Excels (and Where It Doesn\'t)',
  date: '2025-11-19',
}
</script>
