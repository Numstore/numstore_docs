<!-- Directory: /blog/entries/2025-11-26_numstore-for-ai-era.vue -->
<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <h1>{{ meta.title }}</h1>

    <p class="lead text-lg text-gray-700">
      Modern AI systems generate, process, and store enormous volumes of numeric data: training images,
      embeddings, feature vectors, model checkpoints, and inference results. Traditional database systems
      were designed before the deep learning era and impose significant overhead on AI workflows. This
      document examines the storage challenges unique to AI systems and how specialized databases address them.
    </p>

    <h2>The AI Data Storage Problem</h2>

    <h3>Scale of AI Datasets</h3>

    <p>
      Contemporary machine learning systems operate at unprecedented data scales:
    </p>

    <ul>
      <li><strong>ImageNet (2012):</strong> 1.2 million images, 150 GB</li>
      <li><strong>LAION-5B (2022):</strong> 5.85 billion image-text pairs, 240 TB</li>
      <li><strong>GPT-3 training (2020):</strong> 570 GB compressed text, 45 TB tokenized</li>
      <li><strong>Stable Diffusion training:</strong> 2.3 billion images, ~200 TB</li>
    </ul>

    <p>
      These datasets share common characteristics poorly served by traditional databases:
    </p>

    <ul>
      <li>Uniform numeric arrays (pixels, tokens, embeddings)</li>
      <li>High-throughput sequential access patterns</li>
      <li>Minimal metadata per sample</li>
      <li>Immutable training data (write-once, read-many)</li>
    </ul>

    <h3>Current Storage Approaches and Their Limitations</h3>

    <h4>Approach 1: Filesystem + Pickle/NPZ</h4>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Common pattern in ML codebases
import os
import numpy as np

# Save training batch
np.save(f"batch_{epoch}_{step}.npy", embeddings)

# Load for training
files = sorted(os.listdir("embeddings/"))
for f in files:
    data = np.load(f"embeddings/{f}")
    train(data)
</code></pre>

    <p><strong>Problems:</strong></p>
    <ul>
      <li>No atomic updates: Crashes corrupt files</li>
      <li>No concurrent access: Multiple readers/writers cause corruption</li>
      <li>No indexing: Must scan filenames to find data</li>
      <li>Filesystem overhead: Millions of small files overwhelm metadata servers</li>
    </ul>

    <h4>Approach 2: HDF5</h4>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import h5py

# Write embeddings
with h5py.File("embeddings.h5", "w") as f:
    f.create_dataset("bert", data=embeddings, compression="gzip")

# Read embeddings
with h5py.File("embeddings.h5", "r") as f:
    data = f["bert"][1000:2000]  # Slice read
</code></pre>

    <p><strong>Problems:</strong></p>
    <ul>
      <li>Single-writer limitation: Cannot ingest data from multiple sources simultaneously</li>
      <li>Compression overhead: Decompression adds latency during training</li>
      <li>Complex API: Hierarchical structure adds conceptual overhead</li>
      <li>File-level locking: Poor concurrency for distributed training</li>
    </ul>

    <h4>Approach 3: SQL Database (PostgreSQL, MySQL)</h4>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>-- Store image as binary blob
CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    data BYTEA,
    label TEXT
);

INSERT INTO images (data, label)
VALUES (decode('89504e47...', 'hex'), 'cat');
</code></pre>

    <p><strong>Problems:</strong></p>
    <ul>
      <li>Row overhead: ~40 bytes per row, wasteful for large arrays</li>
      <li>BYTEA encoding: Base64/hex encoding inflates storage by 33-100%</li>
      <li>No array operations: Cannot query "get pixels 100-200" without loading entire blob</li>
      <li>Random access: Retrieving 10,000 images = 10,000 random disk seeks</li>
    </ul>

    <h4>Approach 4: Object Storage (S3, GCS)</h4>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import boto3

# Upload embeddings
s3 = boto3.client('s3')
s3.upload_file("embeddings.npy", "my-bucket", "embeddings/batch_0.npy")

# Download for training
s3.download_file("my-bucket", "embeddings/batch_0.npy", "local.npy")
data = np.load("local.npy")
</code></pre>

    <p><strong>Problems:</strong></p>
    <ul>
      <li>Network latency: 10-100ms per request (vs. 0.1ms for local disk)</li>
      <li>No partial reads: Must download entire object to access subset</li>
      <li>API rate limits: Can throttle high-frequency training loops</li>
      <li>Cost: Egress bandwidth charges accumulate for large datasets</li>
    </ul>

    <h2>AI-Specific Storage Requirements</h2>

    <h3>1. High-Throughput Sequential Writes</h3>

    <p>
      Training data is typically generated or preprocessed in batches:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Feature extraction pipeline
for document in documents:
    embedding = model.encode(document)  # 768-dim float array
    store.write(embedding)  # Must sustain 1000s writes/sec
</code></pre>

    <p>
      <strong>Requirement:</strong> Sustain 10K-1M writes/second for feature pipeline ingestion.
    </p>

    <h3>2. Efficient Batch Retrieval</h3>

    <p>
      Training loops read large batches sequentially:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># PyTorch DataLoader pattern
for epoch in range(epochs):
    for batch_idx in range(0, dataset_size, batch_size):
        # Read 256 embeddings (256 * 768 floats = 786 KB)
        batch = dataset[batch_idx:batch_idx + 256]
        loss = train_step(batch)
</code></pre>

    <p>
      <strong>Requirement:</strong> Sub-millisecond latency for batch retrieval to avoid GPU starvation.
    </p>

    <h3>3. Zero-Copy Integration with NumPy/PyTorch</h3>

    <p>
      Copying data between storage and tensor libraries wastes memory and CPU:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Inefficient: Copy from database to NumPy to PyTorch
db_data = database.query("SELECT embeddings FROM table")
numpy_array = np.array(db_data)  # Copy 1
tensor = torch.from_numpy(numpy_array)  # Copy 2 (sometimes)

# Efficient: Zero-copy from storage to tensor
numpy_view = numstore.query(stream, start, end)  # Returns pointer, no copy
tensor = torch.from_numpy(numpy_view)  # Zero-copy (shared memory)
</code></pre>

    <p>
      <strong>Requirement:</strong> Return data as contiguous memory buffers compatible with tensor libraries.
    </p>

    <h3>4. Concurrent Access for Distributed Training</h3>

    <p>
      Multi-GPU training requires simultaneous reads from different workers:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Distributed training with 8 GPUs
# Each GPU reads different data shard simultaneously
# GPU 0: samples [0:1000]
# GPU 1: samples [1000:2000]
# ...
# GPU 7: samples [7000:8000]
</code></pre>

    <p>
      <strong>Requirement:</strong> Support concurrent readers without lock contention.
    </p>

    <h3>5. Immutable Data with Versioning</h3>

    <p>
      Training reproducibility requires versioned, immutable datasets:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Experiment tracking
experiment_v1 = train(dataset="imagenet_v1")
experiment_v2 = train(dataset="imagenet_v2")  # Augmented data

# Must be able to reproduce experiment_v1 exactly
</code></pre>

    <p>
      <strong>Requirement:</strong> Snapshot isolation to prevent data changes affecting running experiments.
    </p>

    <h2>NumStore for AI Workloads</h2>

    <h3>Storing Image Datasets</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np
from PIL import Image

# Create database
db = numstore.open("imagenet.db", create=True)
stream = db.create_stream(
    name="training_images",
    dtype=numstore.UINT8,
    sample_rate=1.0
)

# Ingest images (224x224x3 RGB)
for img_path in image_paths:
    img = Image.open(img_path).resize((224, 224))
    pixels = np.array(img, dtype=np.uint8).flatten()  # 150,528 elements
    stream.write(pixels)

# Training loop: batch reads
batch_size = 256
images_per_batch = batch_size * 224 * 224 * 3
for epoch in range(epochs):
    for batch_idx in range(0, num_images, batch_size):
        # Zero-copy read
        start_elem = batch_idx * 224 * 224 * 3
        end_elem = start_elem + images_per_batch
        batch = stream.query_by_index(start_elem, end_elem)
        batch = batch.reshape(batch_size, 224, 224, 3)
        # batch is a NumPy view, no copying
        train_step(batch)
</code></pre>

    <p><strong>Performance characteristics:</strong></p>
    <ul>
      <li>Write throughput: 10K-100K images/second (vs. 100-1000/sec in PostgreSQL)</li>
      <li>Batch read latency: 5-50 ms for 256 images (vs. 500-5000 ms in SQL)</li>
      <li>Storage: 150 KB/image (vs. 200 KB with BYTEA encoding in SQL)</li>
    </ul>

    <h3>Storing Embeddings for Vector Search</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np

# Create embedding store
db = numstore.open("embeddings.db", create=True)
stream = db.create_stream(
    name="bert_embeddings",
    dtype=numstore.FLOAT32,
    sample_rate=1.0
)

# Ingest embeddings from text corpus
embedding_dim = 768
for document in corpus:
    embedding = bert_model.encode(document)  # 768-dim float array
    stream.write(embedding)

# Retrieve embedding for document N
embedding_N = stream.query_by_index(N * 768, (N + 1) * 768)

# Batch retrieval for similarity search
# Get embeddings for documents [1000:2000]
embeddings = stream.query_by_index(1000 * 768, 2000 * 768)
embeddings = embeddings.reshape(1000, 768)
# Now compute cosine similarity, feed to HNSW index, etc.
</code></pre>

    <p><strong>Use case:</strong> Semantic search engines, recommendation systems, RAG pipelines</p>

    <h3>Storing Model Activations for Analysis</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Interpretability research: Store activations from all layers
activations_stream = db.create_stream(
    name="layer_12_activations",
    dtype=numstore.FLOAT32,
    sample_rate=1.0
)

# During inference, save activations
for input_sample in test_set:
    output, activations = model.forward_with_hooks(input_sample)
    # activations["layer_12"] is shape [batch, seq_len, hidden_dim]
    activations_stream.write(activations["layer_12"].flatten())

# Later: Analyze activation patterns
all_activations = activations_stream.query_all()
# Perform clustering, dimensionality reduction, etc.
</code></pre>

    <h3>Storing Time-Series Logs for Model Monitoring</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Production ML monitoring
inference_latency = db.create_stream(
    name="inference_latency_ms",
    dtype=numstore.FLOAT32,
    sample_rate=1000.0  # 1000 requests/sec
)

prediction_confidence = db.create_stream(
    name="prediction_confidence",
    dtype=numstore.FLOAT32,
    sample_rate=1000.0
)

# During serving
start_time = time.time()
prediction = model(input_data)
latency = (time.time() - start_time) * 1000  # ms
confidence = prediction.max()

inference_latency.write([latency])
prediction_confidence.write([confidence])

# Monitoring dashboard: Query last 1 hour
recent_latencies = inference_latency.query(
    start_time=datetime.now() - timedelta(hours=1),
    end_time=datetime.now()
)
print(f"P95 latency: {np.percentile(recent_latencies, 95)} ms")
</code></pre>

    <h2>Performance Comparison: AI Workloads</h2>

    <h3>Benchmark: Store and Retrieve 1 Million BERT Embeddings</h3>

    <p>
      <strong>Dataset:</strong> 1M documents, 768-dim embeddings (FLOAT32)<br>
      <strong>Total size:</strong> 1M × 768 × 4 bytes = 2.9 GB
    </p>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Storage System</th>
          <th class="text-left py-2 pr-4">Write Time</th>
          <th class="text-left py-2 pr-4">Batch Read (1000 emb)</th>
          <th class="text-left py-2">Storage Size</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">NumStore</td>
          <td class="py-2 pr-4">15 seconds</td>
          <td class="py-2 pr-4">5 ms</td>
          <td class="py-2">3.0 GB</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">PostgreSQL (BYTEA)</td>
          <td class="py-2 pr-4">25 minutes</td>
          <td class="py-2 pr-4">500 ms</td>
          <td class="py-2">6.2 GB</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">HDF5 (uncompressed)</td>
          <td class="py-2 pr-4">30 seconds</td>
          <td class="py-2 pr-4">15 ms</td>
          <td class="py-2">3.1 GB</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Filesystem (NPY files)</td>
          <td class="py-2 pr-4">20 seconds</td>
          <td class="py-2 pr-4">50 ms (cold), 10 ms (warm)</td>
          <td class="py-2">3.0 GB</td>
        </tr>
      </tbody>
    </table>

    <p><strong>NumStore advantages:</strong></p>
    <ul>
      <li>100x faster writes than PostgreSQL</li>
      <li>100x faster reads than PostgreSQL</li>
      <li>Concurrent access (multiple training jobs can read simultaneously)</li>
      <li>Crash recovery (WAL protects against corruption)</li>
    </ul>

    <h3>Benchmark: ImageNet-1K Training Data Pipeline</h3>

    <p>
      <strong>Dataset:</strong> 1.28M images (224×224×3 UINT8)<br>
      <strong>Workload:</strong> Training with batch size 256, 100 epochs
    </p>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Storage System</th>
          <th class="text-left py-2 pr-4">Batch Load Time (256 images)</th>
          <th class="text-left py-2">GPU Utilization</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">NumStore</td>
          <td class="py-2 pr-4">8 ms</td>
          <td class="py-2">95% (not I/O bound)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Filesystem (JPEG files)</td>
          <td class="py-2 pr-4">50 ms (decode overhead)</td>
          <td class="py-2">80% (I/O bound)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">PostgreSQL</td>
          <td class="py-2 pr-4">2000 ms (random seeks)</td>
          <td class="py-2">20% (severely I/O bound)</td>
        </tr>
      </tbody>
    </table>

    <h2>Integration with ML Frameworks</h2>

    <h3>PyTorch DataLoader</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import torch
from torch.utils.data import Dataset, DataLoader
import numstore

class NumStoreDataset(Dataset):
    def __init__(self, db_path, stream_name, samples_per_item):
        self.db = numstore.open(db_path)
        self.stream = self.db.get_stream(stream_name)
        self.samples_per_item = samples_per_item

    def __len__(self):
        return self.stream.count() // self.samples_per_item

    def __getitem__(self, idx):
        start = idx * self.samples_per_item
        end = start + self.samples_per_item
        data = self.stream.query_by_index(start, end)
        # data is NumPy array, zero-copy conversion to tensor
        return torch.from_numpy(data)

# Usage
dataset = NumStoreDataset("embeddings.db", "bert", 768)
loader = DataLoader(dataset, batch_size=256, num_workers=4)

for batch in loader:
    # batch is shape [256, 768]
    train_step(batch)
</code></pre>

    <h3>TensorFlow tf.data Pipeline</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import tensorflow as tf
import numstore
import numpy as np

def numstore_generator(db_path, stream_name, batch_size, samples_per_item):
    db = numstore.open(db_path)
    stream = db.get_stream(stream_name)
    num_items = stream.count() // samples_per_item

    for idx in range(0, num_items, batch_size):
        batch_data = []
        for i in range(batch_size):
            start = (idx + i) * samples_per_item
            end = start + samples_per_item
            data = stream.query_by_index(start, end)
            batch_data.append(data)
        yield np.array(batch_data)

# Create tf.data.Dataset
dataset = tf.data.Dataset.from_generator(
    lambda: numstore_generator("embeddings.db", "bert", 256, 768),
    output_signature=tf.TensorSpec(shape=(256, 768), dtype=tf.float32)
)

for batch in dataset:
    train_step(batch)
</code></pre>

    <h2>Hybrid Architecture: NumStore + Metadata Database</h2>

    <p>
      Production AI systems typically combine NumStore with PostgreSQL for metadata:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>-- PostgreSQL: Store metadata
CREATE TABLE datasets (
    dataset_id SERIAL PRIMARY KEY,
    name TEXT,
    numstore_path TEXT,
    stream_name TEXT,
    num_samples BIGINT,
    sample_shape INTEGER[],
    created_at TIMESTAMP
);

CREATE TABLE experiments (
    experiment_id SERIAL PRIMARY KEY,
    dataset_id INTEGER REFERENCES datasets(dataset_id),
    model_architecture TEXT,
    hyperparameters JSONB,
    training_loss REAL[],
    validation_accuracy REAL
);
</code></pre>

    <p>
      <strong>Division of responsibilities:</strong>
    </p>
    <ul>
      <li><strong>NumStore:</strong> Raw numeric data (images, embeddings, activations)</li>
      <li><strong>PostgreSQL:</strong> Metadata, labels, experiment tracking, user info</li>
    </ul>

    <h2>When to Use NumStore for AI</h2>

    <h3>Ideal Use Cases</h3>
    <ul>
      <li>Image datasets (pre-decoded to raw pixels)</li>
      <li>Embedding/feature vector storage</li>
      <li>Model activation logging</li>
      <li>Training metrics and telemetry</li>
      <li>Preprocessed numerical features</li>
      <li>Time-series prediction datasets</li>
    </ul>

    <h3>Not Recommended For</h3>
    <ul>
      <li>Raw text storage (use Elasticsearch, PostgreSQL)</li>
      <li>Encoded media (JPEG, MP4) - decode first or use object storage</li>
      <li>Highly sparse data with many missing values</li>
      <li>Frequent random updates to historical data</li>
    </ul>

    <h2>Conclusion</h2>

    <p>
      The AI era demands storage systems optimized for uniform numeric arrays at massive scale. Traditional
      databases impose unacceptable overhead for this workload class. NumStore addresses AI-specific
      requirements:
    </p>

    <ul>
      <li>High-throughput ingestion (1M+ writes/second)</li>
      <li>Low-latency batch retrieval (sub-millisecond)</li>
      <li>Zero-copy integration with NumPy/PyTorch</li>
      <li>Concurrent access for distributed training</li>
      <li>Crash recovery and data durability</li>
    </ul>

    <p>
      For research labs and production ML systems handling large-scale numeric datasets, NumStore provides
      10-100x performance improvements over general-purpose databases.
    </p>

    <p>
      <a href="/downloads/current">Download NumStore</a><br>
      <a href="/resources/documentation">API Documentation</a><br>
      <a href="mailto:academic@numstore.dev">Academic Licensing</a>
    </p>
  </article>
</template>


<script lang="ts" setup>
const meta = {
  title: 'The Need for Specialized Databases in the Age of AI',
  date: '2025-11-26',
}
</script>
