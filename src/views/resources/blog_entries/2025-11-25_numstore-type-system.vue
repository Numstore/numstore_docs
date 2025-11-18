<!-- Directory: /blog/entries/2025-11-25_numstore-type-system.vue -->
<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <h1>{{ meta.title }}</h1>

    <p class="lead text-lg text-gray-700">
      NumStore implements a minimal type system focused exclusively on numeric arrays and time-series data.
      This constraint enables performance optimizations that would be impossible in general-purpose databases
      while maintaining type safety and efficient storage utilization.
    </p>

    <h2>Design Philosophy</h2>

    <p>
      The type system enforces a single principle: <strong>all data is stored as typed, contiguous numeric arrays</strong>.
      This eliminates the complexity of schema management, NULL handling, and type coercion present in relational databases,
      while providing the type safety absent from binary blob storage.
    </p>

    <h2>Supported Data Types</h2>

    <p>
      NumStore supports fixed-width numeric types that map directly to hardware representations:
    </p>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Type</th>
          <th class="text-left py-2 pr-4">Size</th>
          <th class="text-left py-2 pr-4">Range</th>
          <th class="text-left py-2">Use Case</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-mono">INT8</td>
          <td class="py-2 pr-4">1 byte</td>
          <td class="py-2 pr-4">-128 to 127</td>
          <td class="py-2">Low-resolution sensor data, flags</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-mono">INT16</td>
          <td class="py-2 pr-4">2 bytes</td>
          <td class="py-2 pr-4">-32,768 to 32,767</td>
          <td class="py-2">Audio samples, ADC readings</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-mono">INT32</td>
          <td class="py-2 pr-4">4 bytes</td>
          <td class="py-2 pr-4">±2.1 billion</td>
          <td class="py-2">Counters, timestamps (ms)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-mono">INT64</td>
          <td class="py-2 pr-4">8 bytes</td>
          <td class="py-2 pr-4">±9.2 quintillion</td>
          <td class="py-2">High-precision timestamps (ns)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-mono">FLOAT32</td>
          <td class="py-2 pr-4">4 bytes</td>
          <td class="py-2 pr-4">±3.4e38 (7 digits)</td>
          <td class="py-2">Sensor data, ML features</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-mono">FLOAT64</td>
          <td class="py-2 pr-4">8 bytes</td>
          <td class="py-2 pr-4">±1.7e308 (15 digits)</td>
          <td class="py-2">Scientific measurements, financial</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-mono">UINT8</td>
          <td class="py-2 pr-4">1 byte</td>
          <td class="py-2 pr-4">0 to 255</td>
          <td class="py-2">Image pixels (RGB channels)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-mono">UINT16</td>
          <td class="py-2 pr-4">2 bytes</td>
          <td class="py-2 pr-4">0 to 65,535</td>
          <td class="py-2">16-bit image depth, port numbers</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-mono">UINT32</td>
          <td class="py-2 pr-4">4 bytes</td>
          <td class="py-2 pr-4">0 to 4.3 billion</td>
          <td class="py-2">Packet counters, IDs</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-mono">UINT64</td>
          <td class="py-2 pr-4">8 bytes</td>
          <td class="py-2 pr-4">0 to 1.8e19</td>
          <td class="py-2">Large-scale counters, hashes</td>
        </tr>
      </tbody>
    </table>

    <h2>Type System Properties</h2>

    <h3>1. Fixed-Width Encoding</h3>

    <p>
      All types use fixed-width representations. Variable-width encodings (strings, JSON, protobuf)
      are not supported. This constraint enables:
    </p>

    <ul>
      <li><strong>O(1) element access:</strong> Element N is at offset <code>N × sizeof(type)</code></li>
      <li><strong>SIMD vectorization:</strong> Aligned, uniform data enables CPU vector instructions</li>
      <li><strong>Zero-copy reads:</strong> Data can be returned as raw pointers without deserialization</li>
      <li><strong>Predictable storage:</strong> N elements = N × sizeof(type) bytes (plus index overhead)</li>
    </ul>

    <h3>2. No NULL Values</h3>

    <p>
      NumStore does not support NULL/missing values within arrays. Applications requiring sparse data
      can use sentinel values (e.g., NaN for floats, INT32_MIN for integers) or separate bitmasks.
    </p>

    <p>
      <strong>Rationale:</strong> NULL handling requires per-element overhead (bit flags or separate storage),
      breaking the contiguous array model and preventing zero-copy reads.
    </p>

    <h3>3. Uniform Arrays (Tensors)</h3>

    <p>
      Each stream stores a single data type. Multi-dimensional data (images, embeddings, matrices) is
      stored as linearized arrays:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>// 224×224×3 image stored as UINT8 stream
size_t pixels_per_image = 224 * 224 * 3;  // 150,528 elements
uint8_t *image_data = malloc(pixels_per_image);
// Fill with RGB values...
numstore_write(stream, image_data, pixels_per_image);

// Read back and reshape
uint8_t *retrieved = numstore_query(stream, start, end);
// Application reshapes to [224, 224, 3] as needed
</code></pre>

    <p>
      NumStore stores the raw array; applications handle reshaping and dimension metadata externally
      (e.g., in PostgreSQL metadata tables or configuration files).
    </p>

    <h2>Type Safety Guarantees</h2>

    <h3>Write-Time Type Checking</h3>

    <p>
      Stream creation specifies a fixed type that cannot be changed:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>// Python
stream = db.create_stream(
    name="temperature",
    dtype=numstore.FLOAT32,  # Type declaration
    sample_rate=100
)

# This succeeds
stream.write(np.array([22.1, 22.3], dtype=np.float32))

# This raises TypeError - type mismatch
stream.write(np.array([1, 2, 3], dtype=np.int32))
</code></pre>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>// C
numstore_stream *stream = numstore_create_stream(
    db, "temperature", NUMSTORE_FLOAT32, 100.0
);

// This succeeds
float values[] = {22.1, 22.3, 22.5};
numstore_write(stream, values, 3);

// This fails at compile time (type mismatch)
int32_t ints[] = {1, 2, 3};
// numstore_write(stream, ints, 3);  // Compiler error
</code></pre>

    <h3>Read-Time Type Preservation</h3>

    <p>
      Queries return typed arrays matching the stream's declared type:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Python - returns NumPy array with correct dtype
data = stream.query(start, end)
assert data.dtype == np.float32

# C - application must use correct pointer type
float *data;
size_t count;
numstore_query(stream, start, end, &data, &count);
// Data is guaranteed to be float32[]
</code></pre>

    <h2>Type System vs. Alternatives</h2>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Approach</th>
          <th class="text-left py-2 pr-4">Type Safety</th>
          <th class="text-left py-2 pr-4">Storage Overhead</th>
          <th class="text-left py-2">Zero-Copy Possible?</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">NumStore (typed arrays)</td>
          <td class="py-2 pr-4">Strong (enforced)</td>
          <td class="py-2 pr-4">0 bytes/element</td>
          <td class="py-2">Yes</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Binary blobs (SQL BYTEA)</td>
          <td class="py-2 pr-4">None (application-level)</td>
          <td class="py-2 pr-4">~32 bytes/blob (header)</td>
          <td class="py-2">No (must extract)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Row-based DB (SQL REAL)</td>
          <td class="py-2 pr-4">Strong (enforced)</td>
          <td class="py-2 pr-4">~40 bytes/row</td>
          <td class="py-2">No (scattered rows)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">HDF5</td>
          <td class="py-2 pr-4">Strong (enforced)</td>
          <td class="py-2 pr-4">~16 bytes/chunk</td>
          <td class="py-2">Yes (with constraints)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Filesystem (raw files)</td>
          <td class="py-2 pr-4">None (filename convention)</td>
          <td class="py-2 pr-4">0 bytes/element</td>
          <td class="py-2">Yes (mmap)</td>
        </tr>
      </tbody>
    </table>

    <h2>Choosing the Correct Type</h2>

    <h3>Precision vs. Storage Trade-offs</h3>

    <p>
      Example: Storing temperature sensor data with ±0.1°C accuracy over [-40°C, 125°C] range:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Option 1: FLOAT32
  - Storage: 4 bytes/sample
  - Precision: ~7 decimal digits (far exceeds requirement)
  - Range: ±3.4e38 (far exceeds requirement)
  - Verdict: Wasteful

Option 2: INT16 (scaled)
  - Storage: 2 bytes/sample (50% savings)
  - Encoding: stored_value = (temp_celsius + 40) * 10
  - Range: -40°C to 6493.5°C (sufficient)
  - Precision: 0.1°C (exact requirement)
  - Verdict: Optimal
</code></pre>

    <p>
      For 1 billion samples over 1 year:
    </p>

    <ul>
      <li>FLOAT32: 4 GB storage</li>
      <li>INT16: 2 GB storage (50% reduction)</li>
    </ul>

    <h3>Type Selection Guidelines</h3>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Data Characteristic</th>
          <th class="text-left py-2">Recommended Type</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Continuous measurements (voltage, temp)</td>
          <td class="py-2 font-mono">FLOAT32</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">High-precision scientific data</td>
          <td class="py-2 font-mono">FLOAT64</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Discrete counts &lt; 2 billion</td>
          <td class="py-2 font-mono">INT32</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Large counters, nanosecond timestamps</td>
          <td class="py-2 font-mono">INT64</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Image RGB channels</td>
          <td class="py-2 font-mono">UINT8</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Audio samples (CD quality)</td>
          <td class="py-2 font-mono">INT16</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">ML embeddings (word2vec, BERT)</td>
          <td class="py-2 font-mono">FLOAT32</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Boolean flags (packed)</td>
          <td class="py-2 font-mono">UINT8</td>
        </tr>
      </tbody>
    </table>

    <h2>Working with Multi-Dimensional Data</h2>

    <h3>Storing Images</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np
from PIL import Image

# Create stream for image data
db = numstore.open("image_dataset.db", create=True)
stream = db.create_stream(
    name="training_images",
    dtype=numstore.UINT8,
    sample_rate=1.0  # Not time-series, use arbitrary rate
)

# Store images as linearized arrays
img = Image.open("cat.jpg").resize((224, 224))
pixels = np.array(img, dtype=np.uint8).flatten()  # [224*224*3] = 150528
stream.write(pixels)

# Store metadata separately (SQL, JSON file, etc.)
metadata = {
    "image_0": {"shape": [224, 224, 3], "label": "cat"}
}

# Retrieve and reshape
retrieved = stream.query(start=0, count=150528)
image_array = retrieved.reshape(224, 224, 3)
</code></pre>

    <h3>Storing Embedding Vectors</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>// Store BERT embeddings (768-dimensional)
numstore_stream *embeddings = numstore_create_stream(
    db, "bert_embeddings", NUMSTORE_FLOAT32, 1.0
);

// Write embedding for document 0
float embedding[768];
// ... compute embedding ...
numstore_write(embeddings, embedding, 768);

// Write embedding for document 1
// ... compute next embedding ...
numstore_write(embeddings, embedding, 768);

// Retrieve embedding for document N
float *doc_embedding;
size_t count;
numstore_query_by_index(embeddings, N * 768, (N + 1) * 768, &doc_embedding, &count);
// doc_embedding is now a 768-element float array
</code></pre>

    <h2>Type System Limitations</h2>

    <h3>Not Suitable For:</h3>

    <ul>
      <li><strong>Variable-length data:</strong> Strings, JSON, protobuf (use PostgreSQL or MongoDB)</li>
      <li><strong>Sparse data with NULLs:</strong> Applications requiring explicit NULL handling</li>
      <li><strong>Schema evolution:</strong> Changing types requires creating new streams and migrating data</li>
      <li><strong>Mixed-type records:</strong> Heterogeneous data (use row-based databases)</li>
    </ul>

    <h3>When to Use External Metadata Storage:</h3>

    <p>
      NumStore stores only numeric arrays. Applications typically use a companion database for metadata:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>-- PostgreSQL metadata table
CREATE TABLE streams (
    stream_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    dtype TEXT NOT NULL,
    dimensions INTEGER[],  -- e.g., [224, 224, 3] for images
    created_at TIMESTAMP,
    description TEXT
);

CREATE TABLE experiments (
    experiment_id SERIAL PRIMARY KEY,
    stream_id INTEGER REFERENCES streams(stream_id),
    start_index BIGINT,
    end_index BIGINT,
    parameters JSONB
);
</code></pre>

    <h2>Performance Implications</h2>

    <p>
      The minimal type system directly enables NumStore's performance characteristics:
    </p>

    <ul>
      <li><strong>No type coercion overhead:</strong> Data is stored and retrieved in native format</li>
      <li><strong>No NULL checking:</strong> Removes conditional branches from hot paths</li>
      <li><strong>Aligned memory access:</strong> Fixed-width types enable hardware-aligned reads</li>
      <li><strong>Compiler optimization:</strong> Strong typing allows aggressive inlining and vectorization</li>
    </ul>

    <h2>Conclusion</h2>

    <p>
      NumStore's type system sacrifices generality for performance and simplicity. The constraint to
      fixed-width numeric arrays enables:
    </p>

    <ul>
      <li>Zero-copy data access</li>
      <li>Predictable storage utilization</li>
      <li>SIMD vectorization opportunities</li>
      <li>Direct integration with NumPy, PyTorch, and other numeric libraries</li>
    </ul>

    <p>
      For workloads involving uniform numeric data (time-series, images, tensors, embeddings), this
      specialized type system delivers order-of-magnitude performance improvements over general-purpose
      databases.
    </p>

    <p>
      <a href="/downloads/current">Download NumStore</a><br>
      <a href="/resources/documentation">Read the Docs</a><br>
      <a href="mailto:hello@numstore.dev">Contact Us</a>
    </p>
  </article>
</template>


<script lang="ts" setup>
const meta = {
  title: 'NumStore\'s Simple Type System: Fixed-Width Numeric Arrays',
  date: '2025-11-25',
}
</script>
