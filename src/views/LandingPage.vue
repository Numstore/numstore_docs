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
        A database purpose-built for numeric time-series data
      </p>
      <p class="text-lg text-gray-600 mb-8 max-w-3xl mx-auto">
        Store millions of samples per second with sub-millisecond query latency.
        10-100x faster than traditional databases for numeric workloads.
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
              <span>Sustained write rates exceeding 1M samples/second</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>O(log n) range queries with R+ tree spatial indexing</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>ACID transactions with write-ahead logging</span>
            </li>
            <li class="flex items-start">
              <span class="text-green-600 mr-2">✓</span>
              <span>Zero-copy integration with NumPy, Pandas, PyTorch</span>
            </li>
          </ul>
          <ul class="space-y-3">
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
              <span>Battle-tested for scientific instrumentation</span>
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
