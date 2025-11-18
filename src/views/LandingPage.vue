<script lang="ts" setup>
</script>

<template>
  <div class="max-w-6xl mx-auto">
    <!-- Hero Section -->
    <section class="text-center py-16">
      <h1 class="text-5xl font-bold text-gray-900 mb-4">
        NumStore
      </h1>
      <p class="text-2xl text-gray-700 mb-6">
        Store uniform arrays as first-class citizens
      </p>
      <p class="text-lg text-gray-600 mb-8 max-w-3xl mx-auto">
        Time-series, images, tensors, sensor data—any uniform numeric array.
        10-100x faster than SQL, simpler than HDF5, better than binary blobs.
      </p>

      <div class="flex justify-center gap-4 mb-8">
        <a href="/downloads/current"
           class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-3 rounded-lg text-lg transition">
          Download v1.0.0
        </a>
        <a href="/resources/documentation"
           class="bg-gray-200 hover:bg-gray-300 text-gray-800 font-semibold px-8 py-3 rounded-lg text-lg transition">
          Read Docs
        </a>
      </div>

      <p class="text-sm text-gray-600">
        Free for academic use • Open source C library • Python, Java bindings
      </p>
    </section>

    <!-- Key Features -->
    <section class="py-12 bg-gray-50 -mx-10 px-10">
      <h2 class="text-3xl font-bold text-center mb-12">Why NumStore?</h2>

      <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
        <div class="bg-white p-6 rounded-lg shadow-sm">
          <div class="text-4xl mb-4">⚡</div>
          <h3 class="text-xl font-semibold mb-2">Extreme Performance</h3>
          <p class="text-gray-700">
            Contiguous storage model delivers 10-100x faster queries than row-based databases.
            Zero-copy reads eliminate memory overhead.
          </p>
        </div>

        <div class="bg-white p-6 rounded-lg shadow-sm">
          <div class="text-4xl mb-4">🔧</div>
          <h3 class="text-xl font-semibold mb-2">Zero Dependencies</h3>
          <p class="text-gray-700">
            Written in pure C with no external dependencies. Embed in any language:
            Python, Java, Go, Rust, or directly in C/C++.
          </p>
        </div>

        <div class="bg-white p-6 rounded-lg shadow-sm">
          <div class="text-4xl mb-4">📊</div>
          <h3 class="text-xl font-semibold mb-2">Built for Science</h3>
          <p class="text-gray-700">
            Designed for high-frequency data acquisition, experimental measurements,
            and scientific computing. Free for academic research.
          </p>
        </div>
      </div>

      <div class="mt-12 max-w-5xl mx-auto bg-white p-8 rounded-lg shadow-sm">
        <h3 class="text-2xl font-bold mb-6 text-center">Technical Highlights</h3>
        <div class="grid md:grid-cols-2 gap-6">
          <ul class="space-y-3">
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Oscilloscope-speed data storage: 1M+ samples/second sustained</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Real-time operation with sub-millisecond append latency</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Crash recovery with write-ahead logging (WAL)</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Both append and insert operations supported</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Zero-copy integration with NumPy, Pandas, PyTorch</span>
            </li>
          </ul>
          <ul class="space-y-3">
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>O(log n) range queries with R+ tree spatial indexing</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>ACID transactions for data consistency</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Contiguous storage: 10-20x lower overhead than SQL</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Embedded deployment on edge/IoT devices</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Commercial support and academic licensing available</span>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Code Examples -->
    <section class="py-16">
      <h2 class="text-3xl font-bold text-center mb-12">Simple, Powerful API</h2>

      <div class="grid md:grid-cols-2 gap-8">
        <!-- Python Example -->
        <div>
          <h3 class="text-xl font-semibold mb-4">Python API</h3>
          <pre class="bg-gray-900 text-gray-100 p-6 rounded-lg overflow-x-auto text-sm"><code>import numstore
import numpy as np

# Create database and stream
db = numstore.open("sensor_data.db", create=True)
stream = db.create_stream(
    name="temperature",
    dtype=numstore.FLOAT32,
    sample_rate=100  # 100 Hz
)

# Write data (NumPy array)
temps = np.array([22.1, 22.3, 22.5, 22.4])
stream.write(temps)

# Query range (returns NumPy array, zero-copy)
data = stream.query(
    start_time="2025-01-01 10:00:00",
    end_time="2025-01-01 11:00:00"
)

print(f"Mean: {np.mean(data):.2f}°C")
print(f"Retrieved {len(data)} samples")</code></pre>
        </div>

        <!-- C Example -->
        <div>
          <h3 class="text-xl font-semibold mb-4">C API</h3>
          <pre class="bg-gray-900 text-gray-100 p-6 rounded-lg overflow-x-auto text-sm"><code>#include &lt;numstore.h&gt;

int main() {
    // Open database
    numstore_db_t *db = numstore_open(
        "sensor_data.db",
        NUMSTORE_CREATE
    );

    // Create stream
    numstore_stream_t *stream =
        numstore_create_stream(
            db,
            "temperature",
            NUMSTORE_FLOAT32,
            100  // 100 Hz sample rate
        );

    // Write data
    float temps[] = {22.1, 22.3, 22.5, 22.4};
    numstore_write(stream, temps, 4);

    // Query range (zero-copy pointer)
    float *data;
    size_t count;
    numstore_query_range(
        stream,
        start_ts,
        end_ts,
        &data,
        &count
    );

    // Process data directly
    for (size_t i = 0; i &lt; count; i++) {
        process_sample(data[i]);
    }

    numstore_close(db);
    return 0;
}</code></pre>
        </div>
      </div>

      <div class="text-center mt-8">
        <a href="/resources/blog/2025-11-23_usage-example"
           class="text-blue-600 hover:text-blue-800 font-medium">
          See full tutorial with ML integration →
        </a>
      </div>
    </section>

    <!-- Complexity Table -->
    <section class="py-16 bg-gray-50 -mx-10 px-10">
      <div class="max-w-5xl mx-auto">
        <h2 class="text-3xl font-bold text-center mb-6">Operation Complexity</h2>
        <p class="text-center text-gray-700 mb-8 max-w-3xl mx-auto">
          Predictable performance characteristics for all operations. NumStore provides O(log n) complexity
          for most operations—far better than O(n) scans in flat files or append-only logs.
        </p>

        <div class="bg-white rounded-lg shadow-sm overflow-hidden">
          <table class="w-full">
            <thead class="bg-gray-800 text-white">
              <tr>
                <th class="px-6 py-4 text-left">Operation</th>
                <th class="px-6 py-4 text-left">Time Complexity</th>
                <th class="px-6 py-4 text-left">Description</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
              <tr class="hover:bg-gray-50">
                <td class="px-6 py-4 font-semibold">Append</td>
                <td class="px-6 py-4 font-mono text-green-600">O(1) amortized</td>
                <td class="px-6 py-4 text-gray-700">Write to end of stream (most common operation)</td>
              </tr>
              <tr class="hover:bg-gray-50">
                <td class="px-6 py-4 font-semibold">Insert (middle)</td>
                <td class="px-6 py-4 font-mono text-blue-600">O(log n + k)</td>
                <td class="px-6 py-4 text-gray-700">Insert k elements at arbitrary position. log n for index lookup, k for data shift</td>
              </tr>
              <tr class="hover:bg-gray-50">
                <td class="px-6 py-4 font-semibold">Range query</td>
                <td class="px-6 py-4 font-mono text-green-600">O(log n + k)</td>
                <td class="px-6 py-4 text-gray-700">Retrieve k elements within time range. log n tree traversal + k sequential read</td>
              </tr>
              <tr class="hover:bg-gray-50">
                <td class="px-6 py-4 font-semibold">Point query</td>
                <td class="px-6 py-4 font-mono text-green-600">O(log n)</td>
                <td class="px-6 py-4 text-gray-700">Find single element by timestamp or index</td>
              </tr>
              <tr class="hover:bg-gray-50">
                <td class="px-6 py-4 font-semibold">Update</td>
                <td class="px-6 py-4 font-mono text-blue-600">O(log n)</td>
                <td class="px-6 py-4 text-gray-700">Modify element at specific position. Logged via WAL for crash recovery</td>
              </tr>
              <tr class="hover:bg-gray-50">
                <td class="px-6 py-4 font-semibold">Delete range</td>
                <td class="px-6 py-4 font-mono text-blue-600">O(log n + k)</td>
                <td class="px-6 py-4 text-gray-700">Remove k elements from stream. Mark deleted in index, reclaim in compaction</td>
              </tr>
              <tr class="hover:bg-gray-50">
                <td class="px-6 py-4 font-semibold">Scan (full)</td>
                <td class="px-6 py-4 font-mono text-yellow-600">O(n)</td>
                <td class="px-6 py-4 text-gray-700">Sequential scan of all data. Optimized via contiguous storage (cache-friendly)</td>
              </tr>
              <tr class="hover:bg-gray-50">
                <td class="px-6 py-4 font-semibold">Commit transaction</td>
                <td class="px-6 py-4 font-mono text-green-600">O(1)</td>
                <td class="px-6 py-4 text-gray-700">Flush WAL to disk. Ensures durability and crash recovery</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="mt-6 bg-blue-50 border-l-4 border-blue-600 p-6 rounded">
          <h3 class="font-semibold text-lg mb-2 text-blue-900">Why This Matters</h3>
          <ul class="space-y-2 text-gray-700">
            <li class="flex items-start">
              <span class="text-blue-600 mr-2">→</span>
              <span><strong>Append-heavy workloads:</strong> O(1) amortized means sustained 1M+/sec write rates</span>
            </li>
            <li class="flex items-start">
              <span class="text-blue-600 mr-2">→</span>
              <span><strong>Random access:</strong> O(log n) beats O(n) scans in flat files by orders of magnitude</span>
            </li>
            <li class="flex items-start">
              <span class="text-blue-600 mr-2">→</span>
              <span><strong>Range queries:</strong> Time-range lookups are O(log n + k), not O(n) like scanning</span>
            </li>
            <li class="flex items-start">
              <span class="text-blue-600 mr-2">→</span>
              <span><strong>Inserts supported:</strong> Unlike append-only logs, can insert in middle with O(log n + k)</span>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- ML/AI Storage Problem -->
    <section class="py-16 bg-gradient-to-r from-purple-50 to-pink-50 -mx-10 px-10">
      <div class="max-w-5xl mx-auto">
        <h2 class="text-3xl font-bold text-center mb-8">Storing AI Training Data? NumStore Solves That.</h2>

        <div class="bg-white p-8 rounded-lg shadow-sm mb-8">
          <h3 class="text-xl font-semibold mb-4 text-gray-800">The Problem</h3>
          <p class="text-gray-700 mb-4">
            You're training an AI model and need to store millions of images, embeddings, or tensors. What do you do?
          </p>
          <ul class="space-y-2 text-gray-700 mb-4">
            <li class="flex items-start">
              <span class="text-red-500 mr-2">✗</span>
              <span><strong>Binary blobs in SQL?</strong> Terrible performance, massive overhead, slow queries.</span>
            </li>
            <li class="flex items-start">
              <span class="text-red-500 mr-2">✗</span>
              <span><strong>One pixel per row?</strong> Absurd storage overhead and query complexity.</span>
            </li>
            <li class="flex items-start">
              <span class="text-red-500 mr-2">✗</span>
              <span><strong>HDF5 files?</strong> Complex API, poor concurrency, limited query capabilities.</span>
            </li>
            <li class="flex items-start">
              <span class="text-red-500 mr-2">✗</span>
              <span><strong>Filesystem?</strong> No indexing, no transactions, no efficient range queries.</span>
            </li>
          </ul>
        </div>

        <div class="bg-white p-8 rounded-lg shadow-sm">
          <h3 class="text-xl font-semibold mb-4 text-green-800">NumStore's Solution</h3>
          <p class="text-gray-700 mb-4">
            <strong>Store uniform arrays as first-class citizens.</strong> Images are just 3D arrays (height × width × channels).
            Embeddings are 1D/2D arrays. Tensors are N-dimensional arrays. NumStore handles them all natively.
          </p>

          <div class="grid md:grid-cols-2 gap-6 mb-4">
            <div>
              <h4 class="font-semibold mb-2 text-gray-800">For Training Data:</h4>
              <pre class="bg-gray-900 text-gray-100 p-4 rounded text-sm"><code># Store an image (224x224x3)
image = load_image("cat.jpg")  # numpy array
stream.write(image.flatten())

# Batch write thousands of images
images = load_batch(1000)  # (1000, 224, 224, 3)
stream.write_batch(images)</code></pre>
            </div>
            <div>
              <h4 class="font-semibold mb-2 text-gray-800">For Embeddings:</h4>
              <pre class="bg-gray-900 text-gray-100 p-4 rounded text-sm"><code># Store CLIP embeddings (512-dim)
embedding = model.encode(image)  # (512,)
embedding_stream.write(embedding)

# Query similar embeddings
embeddings = stream.query_range(
    start_id, end_id
)  # Zero-copy NumPy array</code></pre>
            </div>
          </div>

          <ul class="space-y-2 text-gray-700">
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Native multi-dimensional array support</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Zero-copy reads directly into PyTorch/TensorFlow</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Efficient batch operations for data loaders</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Transaction support for versioned datasets</span>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Use Cases -->
    <section class="py-12 bg-blue-50 -mx-10 px-10">
      <h2 class="text-3xl font-bold text-center mb-12">Perfect For</h2>

      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-6xl mx-auto">
        <div class="bg-white p-6 rounded-lg">
          <h3 class="font-semibold text-lg mb-2">Scientific Research</h3>
          <p class="text-gray-700 text-sm">
            Oscilloscopes, sensors, detectors, experimental measurements
          </p>
        </div>

        <div class="bg-white p-6 rounded-lg">
          <h3 class="font-semibold text-lg mb-2">Industrial IoT</h3>
          <p class="text-gray-700 text-sm">
            Manufacturing, power grids, equipment monitoring
          </p>
        </div>

        <div class="bg-white p-6 rounded-lg">
          <h3 class="font-semibold text-lg mb-2">Financial Trading</h3>
          <p class="text-gray-700 text-sm">
            Market data, tick storage, backtesting platforms
          </p>
        </div>

        <div class="bg-white p-6 rounded-lg">
          <h3 class="font-semibold text-lg mb-2">Machine Learning</h3>
          <p class="text-gray-700 text-sm">
            Feature stores, time-series models, training pipelines
          </p>
        </div>
      </div>

      <div class="text-center mt-8">
        <a href="/resources/blog/2025-11-24_applications-built-with-numstore"
           class="text-blue-600 hover:text-blue-800 font-medium">
          Read detailed application architectures →
        </a>
      </div>
    </section>

    <!-- Performance Comparison -->
    <section class="py-16">
      <h2 class="text-3xl font-bold text-center mb-12">Performance Comparison</h2>

      <div class="max-w-4xl mx-auto bg-white border rounded-lg overflow-hidden">
        <table class="w-full">
          <thead class="bg-gray-100">
            <tr>
              <th class="px-6 py-3 text-left">Operation</th>
              <th class="px-6 py-3 text-left">PostgreSQL</th>
              <th class="px-6 py-3 text-left">NumStore</th>
              <th class="px-6 py-3 text-left">Speedup</th>
            </tr>
          </thead>
          <tbody>
            <tr class="border-t">
              <td class="px-6 py-4">Write 1M samples</td>
              <td class="px-6 py-4">20-100 seconds</td>
              <td class="px-6 py-4 font-semibold text-green-600">0.1-1 second</td>
              <td class="px-6 py-4 font-semibold">20-100x</td>
            </tr>
            <tr class="border-t bg-gray-50">
              <td class="px-6 py-4">Query 1M samples</td>
              <td class="px-6 py-4">5-30 seconds</td>
              <td class="px-6 py-4 font-semibold text-green-600">50-200 ms</td>
              <td class="px-6 py-4 font-semibold">25-600x</td>
            </tr>
            <tr class="border-t">
              <td class="px-6 py-4">Storage overhead</td>
              <td class="px-6 py-4">50+ bytes/sample</td>
              <td class="px-6 py-4 font-semibold text-green-600">4 bytes/sample</td>
              <td class="px-6 py-4 font-semibold">12.5x smaller</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p class="text-center text-sm text-gray-600 mt-4">
        Benchmarks: 100M float samples on commodity hardware. See <a href="/resources/blog/2025-11-20_numstore-vs-sql" class="text-blue-600 hover:underline">detailed comparison</a>.
      </p>
    </section>

    <!-- Academic Focus -->
    <section class="py-12 bg-green-50 -mx-10 px-10">
      <div class="max-w-4xl mx-auto text-center">
        <h2 class="text-3xl font-bold mb-6">Built for Academic Research</h2>
        <p class="text-lg text-gray-700 mb-6">
          NumStore was designed for scientific computing and data acquisition.
          Academic researchers get special treatment.
        </p>

        <div class="grid md:grid-cols-3 gap-6 mb-8">
          <div class="bg-white p-6 rounded-lg">
            <h3 class="font-semibold mb-2">Free Academic Licenses</h3>
            <p class="text-gray-700 text-sm">
              No-cost licenses for qualifying student projects and research labs
            </p>
          </div>
          <div class="bg-white p-6 rounded-lg">
            <h3 class="font-semibold mb-2">Institutional Discounts</h3>
            <p class="text-gray-700 text-sm">
              Up to 90% off commercial rates for universities
            </p>
          </div>
          <div class="bg-white p-6 rounded-lg">
            <h3 class="font-semibold mb-2">Direct Support</h3>
            <p class="text-gray-700 text-sm">
              Technical assistance for scientific computing workflows
            </p>
          </div>
        </div>

        <a href="mailto:academic@numstore.dev"
           class="inline-block bg-green-600 hover:bg-green-700 text-white font-semibold px-8 py-3 rounded-lg transition">
          Apply for Academic License
        </a>
      </div>
    </section>

    <!-- Project Status -->
    <section class="py-16 bg-yellow-50 -mx-10 px-10">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-3xl font-bold text-center mb-6">Project Status & Roadmap</h2>

        <div class="bg-white p-8 rounded-lg shadow-sm mb-6">
          <h3 class="text-xl font-semibold mb-4 text-green-800">Core is Feature-Complete</h3>
          <p class="text-gray-700 mb-4">
            NumStore v1.0.0 is production-ready with a stable, battle-tested core:
          </p>
          <ul class="space-y-2 text-gray-700">
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Contiguous storage model with R+ tree indexing</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Write-ahead logging and ACID transactions</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Python and Java bindings with zero-copy reads</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Proven in scientific instrumentation and industrial deployments</span>
            </li>
          </ul>
        </div>

        <div class="bg-white p-8 rounded-lg shadow-sm">
          <h3 class="text-xl font-semibold mb-4 text-blue-800">Active Development & Funding</h3>
          <p class="text-gray-700 mb-4">
            NumStore is actively developed and seeking funding to add highly-requested features:
          </p>
          <ul class="space-y-2 text-gray-700 mb-6">
            <li class="flex items-start">
              <span class="text-blue-600 mr-2">→</span>
              <span>Distributed/clustered deployment support</span>
            </li>
            <li class="flex items-start">
              <span class="text-blue-600 mr-2">→</span>
              <span>Advanced compression strategies (delta encoding, quantization)</span>
            </li>
            <li class="flex items-start">
              <span class="text-blue-600 mr-2">→</span>
              <span>Additional language bindings (Go, Rust, JavaScript)</span>
            </li>
            <li class="flex items-start">
              <span class="text-blue-600 mr-2">→</span>
              <span>GPU integration for accelerated analytics</span>
            </li>
            <li class="flex items-start">
              <span class="text-blue-600 mr-2">→</span>
              <span>Native cloud storage backends (S3, GCS, Azure)</span>
            </li>
          </ul>

          <div class="bg-blue-50 border-l-4 border-blue-600 p-4 rounded">
            <p class="text-gray-800">
              <strong>Interested in sponsoring development?</strong> NumStore accepts funding for specific
              features, performance optimizations, and platform support. Contact
              <a href="mailto:hello@numstore.dev" class="text-blue-600 hover:underline font-medium">hello@numstore.dev</a>
              to discuss sponsorship opportunities.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-16 text-center">
      <h2 class="text-4xl font-bold mb-6">Ready to get started?</h2>
      <p class="text-xl text-gray-700 mb-8 max-w-2xl mx-auto">
        Download NumStore, follow the quickstart guide, and start building
        high-performance numeric data applications.
      </p>

      <div class="flex justify-center gap-4">
        <a href="/downloads/current"
           class="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-3 rounded-lg text-lg transition">
          Download Now
        </a>
        <a href="/resources/blog/2025-11-23_usage-example"
           class="bg-gray-200 hover:bg-gray-300 text-gray-800 font-semibold px-8 py-3 rounded-lg text-lg transition">
          Quickstart Tutorial
        </a>
      </div>

      <div class="mt-12 pt-8 border-t max-w-3xl mx-auto">
        <h3 class="text-xl font-semibold mb-4">Learn More</h3>
        <div class="grid md:grid-cols-3 gap-4 text-sm">
          <a href="/resources/documentation" class="text-blue-600 hover:underline">
            📚 Documentation
          </a>
          <a href="/resources/blog/2025-11-18_announcing-numstore-academic-research" class="text-blue-600 hover:underline">
            📖 Architecture Overview
          </a>
          <a href="/resources/blog/2025-11-24_applications-built-with-numstore" class="text-blue-600 hover:underline">
            🏗️ Application Examples
          </a>
          <a href="/services/enterprise_support" class="text-blue-600 hover:underline">
            💼 Commercial Support
          </a>
          <a href="/community/forum" class="text-blue-600 hover:underline">
            💬 Community Forum
          </a>
          <a href="mailto:hello@numstore.dev" class="text-blue-600 hover:underline">
            ✉️ Contact Us
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Additional spacing for landing page */
</style>
