<!-- Directory: /blog/entries/2025-11-24_applications-built-with-numstore.vue -->
<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <h1>{{ meta.title }}</h1>

    <p class="lead text-lg text-gray-700">
      This document describes application architectures that can be implemented using NumStore's
      contiguous storage model and high-throughput numeric data capabilities. Examples span scientific
      instrumentation, industrial monitoring, financial systems, and research computing.
    </p>

    <h2>Scientific Data Acquisition Systems</h2>

    <h3>High-Energy Physics Detector Data Pipeline</h3>

    <p>
      Particle physics experiments generate multi-terabyte datasets from detector arrays. A typical
      detector system might produce:
    </p>

    <ul>
      <li>10,000+ channels sampling at 1-10 MHz</li>
      <li>100-1000 GB/hour sustained data rate</li>
      <li>Real-time trigger decision requirements (microsecond latency)</li>
      <li>Long-term archival with queryable metadata</li>
    </ul>

    <p><strong>Implementation architecture:</strong></p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Data Flow:
  Detector Array → DAQ Frontend → NumStore Ingest Pipeline → Analysis Cluster
                                        ↓
                                   Trigger System (read-only queries)
                                        ↓
                                   Archival Storage

NumStore Configuration:
  - Multiple stream instances per detector subsystem
  - Write-ahead logging for data integrity
  - Range queries for event reconstruction
  - Integration with ROOT/HDF5 for analysis export
</code></pre>

    <p>
      NumStore's contiguous storage enables direct memory access for trigger algorithms without
      copying data between acquisition and analysis stages. The R+ tree indexing supports efficient
      temporal range queries for event correlation across detector subsystems.
    </p>

    <h3>Astronomical Observatory Data Management</h3>

    <p>
      Modern telescopes produce continuous time-series data from CCD arrays, spectrometers, and
      adaptive optics systems. Requirements include:
    </p>

    <ul>
      <li>Multi-wavelength time-domain astronomy (simultaneous data streams)</li>
      <li>Precise temporal alignment across instruments (&lt;1ms synchronization)</li>
      <li>Petabyte-scale long-term storage</li>
      <li>Fast retrieval for transient event analysis</li>
    </ul>

    <p><strong>System design:</strong></p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Architecture:
  Instrument → Time Synchronization → NumStore Buffer → Processing Pipeline
                                            ↓
                                      Event Detector
                                            ↓
                                    Alert Distribution

Storage tier:
  - Hot data: NumStore on NVMe (last 30 days)
  - Warm data: NumStore on HDD RAID (1 year)
  - Cold data: Compressed export to object storage
</code></pre>

    <p>
      The system uses NumStore's transaction support for atomic writes across multiple instrument
      streams, ensuring temporal consistency for multi-wavelength observations.
    </p>

    <h2>Industrial Monitoring and Control</h2>

    <h3>Manufacturing Process Optimization Platform</h3>

    <p>
      Industrial IoT deployments for manufacturing require real-time monitoring of equipment state,
      environmental conditions, and product quality metrics. A typical factory deployment handles:
    </p>

    <ul>
      <li>1,000-50,000 sensor endpoints</li>
      <li>Mixed sample rates (1 Hz to 10 kHz depending on sensor type)</li>
      <li>Edge computing requirements (local processing before cloud upload)</li>
      <li>Regulatory compliance with data retention (5-10 years)</li>
    </ul>

    <p><strong>Edge deployment architecture:</strong></p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Factory Floor:
  Sensor Network → Edge Gateway (NumStore) → Local Analytics
                         ↓
                   Aggregation Layer
                         ↓
                   Cloud Platform

Edge gateway implementation:
  - NumStore embedded in Linux appliance
  - Circular buffer configuration (7 days retention)
  - Automated compression and upload for long-term storage
  - Local ML inference on recent time windows
</code></pre>

    <p>
      NumStore's dependency-free C implementation enables deployment on industrial gateways and
      embedded Linux systems. The contiguous storage model reduces flash wear through sequential
      writes, critical for long-term field deployment.
    </p>

    <h3>Power Grid Monitoring System</h3>

    <p>
      Electrical grid operators require microsecond-precision monitoring for frequency, voltage,
      and current across substations. Synchrophasor measurement units (PMUs) generate:
    </p>

    <ul>
      <li>30-120 samples/second per measurement point</li>
      <li>GPS-synchronized timestamps (±1 microsecond)</li>
      <li>Distributed deployment across geographic regions</li>
      <li>Real-time stability analysis requirements</li>
    </ul>

    <p><strong>Distributed architecture:</strong></p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Regional Substations:
  PMU → NumStore (local) → Regional Aggregator → Central SCADA
                                                       ↓
                                                 Stability Analysis
                                                       ↓
                                                 Operator Interface

Query patterns:
  - Real-time: Last 60 seconds for current grid state
  - Historical: Time-range queries for fault analysis
  - Correlation: Multi-site synchronized queries
</code></pre>

    <p>
      The R+ tree indexing enables efficient correlation queries across multiple substations for
      disturbance analysis. NumStore's write-ahead logging provides data durability guarantees
      required for regulatory compliance.
    </p>

    <h2>Financial Trading Systems</h2>

    <h3>Market Data Collection and Replay Platform</h3>

    <p>
      High-frequency trading infrastructure requires capturing and storing every market event
      (quotes, trades, order book updates) with microsecond-precision timestamps:
    </p>

    <ul>
      <li>100,000-1,000,000 updates/second during peak hours</li>
      <li>Exact temporal ordering requirements</li>
      <li>Deterministic replay for backtesting</li>
      <li>Sub-millisecond query latency for live analytics</li>
    </ul>

    <p><strong>System architecture:</strong></p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Market Data Flow:
  Exchange Feed → Normalization → NumStore Ingest → Multiple Consumers:
                                                      - Strategy Engines
                                                      - Risk Systems
                                                      - Compliance Recording
                                                      - Backtesting Platform

Storage design:
  - Separate streams per symbol/exchange
  - Snapshot + delta compression for order books
  - Hourly checkpoints for fast replay initialization
  - Zero-copy reads for strategy engine integration
</code></pre>

    <p>
      NumStore's contiguous storage preserves exact event ordering critical for regulatory
      compliance and deterministic replay. The zero-copy read capability minimizes latency
      in the critical path between data capture and trading decisions.
    </p>

    <h3>Risk Analytics Data Warehouse</h3>

    <p>
      Financial institutions compute real-time risk metrics across portfolios using historical
      time-series data. Requirements include:
    </p>

    <ul>
      <li>Multi-year historical tick data (terabytes per symbol)</li>
      <li>Fast retrieval for Value-at-Risk (VaR) calculations</li>
      <li>Parallel query execution across thousands of securities</li>
      <li>Integration with numerical computing environments (Python, R, MATLAB)</li>
    </ul>

    <p><strong>Data warehouse architecture:</strong></p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Query Engine:
  Risk Model → Query Optimizer → Parallel NumStore Readers → Aggregation
                                         ↓
                                   NumPy/Pandas
                                         ↓
                                   Computation Kernel

Optimization strategies:
  - Partition by symbol and time range
  - Columnar layout for price/volume/volatility
  - Selective materialization (query only needed columns)
  - SIMD vectorization via NumPy zero-copy integration
</code></pre>

    <p>
      The system leverages NumStore's contiguous storage to return data as NumPy arrays without
      copying, enabling direct computation in vectorized risk models.
    </p>

    <h2>Machine Learning Infrastructure</h2>

    <h3>Time-Series Feature Store</h3>

    <p>
      Machine learning pipelines for time-series prediction require efficient storage and retrieval
      of feature vectors computed from raw sensor data:
    </p>

    <ul>
      <li>Billions of feature vectors (e.g., sliding window statistics)</li>
      <li>Variable-length sequences for LSTM/Transformer models</li>
      <li>Training dataset versioning and lineage tracking</li>
      <li>Low-latency serving for online inference</li>
    </ul>

    <p><strong>Feature store architecture:</strong></p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Pipeline:
  Raw Data → Feature Engineering → NumStore (versioned streams) → Training/Serving
                                            ↓
                                    Metadata Registry (SQL)

Storage organization:
  - Separate streams per feature family
  - Time-based partitioning (daily/hourly)
  - Immutable writes for reproducibility
  - Point-in-time queries for historical consistency

Serving pattern:
  - Recent features cached in NumStore memory buffers
  - Zero-copy export to TensorFlow/PyTorch
  - Batch prefetch for training data loaders
</code></pre>

    <p>
      NumStore's transaction support enables atomic feature set updates, ensuring training datasets
      remain consistent across pipeline runs. The contiguous storage aligns with deep learning
      framework memory layouts for efficient data loading.
    </p>

    <h3>Embedding Vector Database</h3>

    <p>
      Large language models and recommendation systems require fast similarity search over dense
      vector embeddings:
    </p>

    <ul>
      <li>Millions to billions of embedding vectors (768-4096 dimensions)</li>
      <li>Approximate nearest neighbor (ANN) search requirements</li>
      <li>Periodic re-embedding and index updates</li>
      <li>Low-latency retrieval for inference serving</li>
    </ul>

    <p><strong>System design:</strong></p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Architecture:
  Embedding Model → NumStore (vector storage) → ANN Index Builder
                                                        ↓
                                                  Query Engine

Index strategy:
  - NumStore for durable vector storage
  - In-memory HNSW/IVF index for fast search
  - Periodic rebuild from NumStore base data
  - Snapshot isolation for consistent reads during updates
</code></pre>

    <p>
      The contiguous storage enables fast bulk loading of embeddings into ANN index structures.
      NumStore serves as the authoritative storage layer while separate specialized indexes handle
      similarity search.
    </p>

    <h2>Medical and Healthcare Systems</h2>

    <h3>Continuous Patient Monitoring Platform</h3>

    <p>
      Hospital monitoring systems collect physiological waveforms (ECG, EEG, blood pressure) from
      multiple patients simultaneously:
    </p>

    <ul>
      <li>8-16 channels per patient at 250-1000 Hz</li>
      <li>Hundreds of concurrent patients in large hospitals</li>
      <li>Regulatory requirements (HIPAA, FDA 21 CFR Part 11)</li>
      <li>Audit trail for all data access and modifications</li>
    </ul>

    <p><strong>Monitoring system architecture:</strong></p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Data Flow:
  Bedside Monitor → Secure Gateway → NumStore Cluster → Analysis Services
                                            ↓                    ↓
                                       Audit Log          Alert Generation
                                            ↓
                                      Compliance Reporting

Security and compliance:
  - Encrypted storage at rest
  - Write-ahead logging for audit trail
  - Transaction support for atomic alarm threshold updates
  - Role-based access control via application layer
</code></pre>

    <p>
      NumStore's ACID transaction guarantees support regulatory compliance requirements.
      The write-ahead log provides a complete audit trail of all data modifications.
    </p>

    <h2>Environmental and Climate Research</h2>

    <h3>Global Climate Monitoring Network</h3>

    <p>
      Climate research requires aggregating data from distributed sensor networks, satellites, and
      weather stations:
    </p>

    <ul>
      <li>Thousands of geographically distributed sensors</li>
      <li>Multi-decade historical records</li>
      <li>Heterogeneous sample rates and sensor types</li>
      <li>Complex spatio-temporal queries for climate model validation</li>
    </ul>

    <p><strong>Distributed data architecture:</strong></p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Deployment:
  Remote Stations → Satellite Uplink → Regional Data Centers (NumStore)
                                                ↓
                                        Central Repository
                                                ↓
                                        Research Computing

Query federation:
  - Temporal queries: Direct NumStore range scans
  - Spatial queries: Geographic indexing in metadata layer
  - Spatio-temporal: Combined query execution
</code></pre>

    <p>
      The R+ tree spatial indexing, originally designed for geographic data, supports efficient
      queries over both temporal and spatial dimensions when combined with geographic metadata.
    </p>

    <h2>Implementation Considerations</h2>

    <h3>Hybrid Storage Architectures</h3>

    <p>
      Most production systems combine NumStore with complementary databases:
    </p>

    <ul>
      <li><strong>NumStore + PostgreSQL:</strong> Time-series in NumStore, metadata/configuration in PostgreSQL</li>
      <li><strong>NumStore + Redis:</strong> Persistent storage in NumStore, real-time caching in Redis</li>
      <li><strong>NumStore + Elasticsearch:</strong> Numeric data in NumStore, log correlation in Elasticsearch</li>
      <li><strong>NumStore + Object Storage:</strong> Active data in NumStore, cold archival in S3/GCS</li>
    </ul>

    <h3>Performance Tuning</h3>

    <p>
      Application-specific optimizations:
    </p>

    <ul>
      <li>Chunk size selection based on typical query ranges</li>
      <li>Write batching to match source data rate characteristics</li>
      <li>Memory mapping for read-heavy workloads</li>
      <li>Compression strategies for cold storage tiers</li>
    </ul>

    <h3>Deployment Patterns</h3>

    <p>
      Common deployment configurations:
    </p>

    <ul>
      <li><strong>Embedded:</strong> NumStore library linked directly into application</li>
      <li><strong>Edge gateway:</strong> NumStore on industrial/IoT edge devices</li>
      <li><strong>Cluster:</strong> Distributed NumStore instances with application-level sharding</li>
      <li><strong>Tiered storage:</strong> Hot/warm/cold data across NVMe/HDD/object storage</li>
    </ul>

    <h2>Reference Implementations</h2>

    <p>
      Example applications demonstrating NumStore integration are available in the documentation:
    </p>

    <ul>
      <li>Sensor data acquisition (Python)</li>
      <li>Financial tick data capture (Java)</li>
      <li>ML feature pipeline (Python + NumPy)</li>
      <li>Embedded monitoring system (C)</li>
    </ul>

    <p>
      For application design consultation: <a href="mailto:consulting@numstore.dev">consulting@numstore.dev</a>
    </p>

    <p>
      Technical documentation: <a href="/resources/documentation">/resources/documentation</a>
    </p>
  </article>
</template>


<script lang="ts" setup>
const meta = {
  title: 'Applications Built with NumStore',
  date: '2025-11-24',
}
</script>
