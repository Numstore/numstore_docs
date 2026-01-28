<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <header class="mb-8 not-prose">
      <time class="text-sm text-cyan-600 font-medium">{{ meta.date }}</time>
      <h1 class="text-4xl font-bold text-gray-900 mt-2 mb-4">{{ meta.title }}</h1>
      <p class="text-xl text-gray-600 leading-relaxed">
        After months of development, testing, and real-world validation, NumStore v1.0.0 is ready
        for production use. Here's what's included and how to get started.
      </p>
    </header>

    <h2>What's in v1.0.0</h2>

    <p>
      This release includes the core features needed for production numeric data storage:
    </p>

    <h3>Core Database Engine</h3>

    <ul>
      <li><strong>R+ tree indexing</strong> with O(log n) insert and search operations</li>
      <li><strong>Rope-based storage</strong> for contiguous numeric arrays</li>
      <li><strong>Write-ahead logging (WAL)</strong> with two-phase commit semantics</li>
      <li><strong>Full ACID transactions</strong> with rollback support</li>
      <li><strong>Crash recovery</strong> from WAL replay</li>
    </ul>

    <h3>Data Types</h3>

    <ul>
      <li>32-bit and 64-bit floats (float32, float64)</li>
      <li>8, 16, 32, and 64-bit signed/unsigned integers</li>
      <li>Fixed-size arrays and matrices</li>
      <li>Timestamps with nanosecond precision</li>
    </ul>

    <h3>Language Bindings</h3>

    <ul>
      <li><strong>Python</strong> with NumPy integration (zero-copy array access)</li>
      <li><strong>Java</strong> via JNI with ByteBuffer support</li>
      <li><strong>C/C++</strong> native API</li>
    </ul>

    <h2>Performance Highlights</h2>

    <p>
      Benchmarked on a standard developer machine (M2 MacBook Pro, 16GB RAM):
    </p>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Operation</th>
          <th class="text-left py-2 pr-4">Throughput</th>
          <th class="text-left py-2">Latency</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Sequential writes (batched)</td>
          <td class="py-2 pr-4">5M samples/sec</td>
          <td class="py-2">&lt;1ms per 10K batch</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Range query (1M samples)</td>
          <td class="py-2 pr-4">50M samples/sec</td>
          <td class="py-2">~20ms total</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Point query</td>
          <td class="py-2 pr-4">-</td>
          <td class="py-2">&lt;100us</td>
        </tr>
      </tbody>
    </table>

    <h2>Getting Started</h2>

    <h3>Download</h3>

    <p>
      Pre-built binaries are available for Linux (x86_64, ARM64), macOS (Intel, Apple Silicon),
      and Windows (x86_64):
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code># Linux/macOS
curl -L https://numstore.dev/releases/numstore-1.0.0.tar.gz | tar xz
cd numstore-1.0.0
./bin/numstore --version

# Python
pip install numstore</code></pre>

    <h3>Quick Example</h3>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np

# Create a database
db = numstore.open("sensors.ns", create=True)

# Create a stream for temperature data
stream = db.create_stream("temperature", dtype=numstore.FLOAT32)

# Write some data
data = np.random.randn(10000).astype(np.float32)
stream.write(data)

# Query it back
result = stream.query_all()
print(f"Mean: {result.mean():.2f}")

db.close()</code></pre>

    <h2>What's Next</h2>

    <p>
      The v1.0.0 release is just the beginning. On the roadmap for upcoming releases:
    </p>

    <ul>
      <li><strong>v1.1</strong>: Compression (delta encoding, LZ4) for reduced storage</li>
      <li><strong>v1.2</strong>: Replication and multi-node deployment</li>
      <li><strong>v1.3</strong>: Go and Rust language bindings</li>
      <li><strong>v2.0</strong>: Distributed query execution</li>
    </ul>

    <h2>Thanks</h2>

    <p>
      Thanks to everyone who tested early builds, reported bugs, and provided feedback.
      Special thanks to the research groups at MIT and Stanford who validated NumStore
      with real oscilloscope and sensor data.
    </p>

    <p>
      Download v1.0.0: <a href="/downloads/current">Get NumStore</a><br>
      Full changelog: <a href="https://github.com/Numstore/numstore/releases/tag/v1.0.0" target="_blank" rel="noopener">GitHub Release</a><br>
      Questions: <a href="mailto:hello@numstore.dev">hello@numstore.dev</a>
    </p>
  </article>
</template>

<script lang="ts" setup>
export const meta = {
  title: 'NumStore v1.0.0 Released',
  date: '2025-09-05',
}

export const summary = 'NumStore v1.0.0 is now available with R+ tree indexing, WAL with two-phase commit, and Python/Java bindings. Ready for production use.'
</script>
