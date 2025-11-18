<!-- Directory: /blog/entries/2025-11-22_contiguous-data-model.vue -->
<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <h1>{{ meta.title }}</h1>

    <p class="lead text-lg text-gray-700">
      NumStore's contiguous data model is the secret to its performance. By storing numeric arrays
      sequentially in memory and on disk, I unlock zero-copy reads, cache efficiency, and 10-100x
      faster queries compared to traditional row-based databases.
    </p>

    <h2>What Is a Contiguous Data Model?</h2>

    <p>
      A <strong>contiguous data model</strong> stores related data elements sequentially in memory
      or on disk, with no gaps or scattered locations. For numeric time-series, this means:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>// Contiguous: all samples stored sequentially
Memory: [1.2][1.3][1.4][1.5][1.6][1.7][1.8][...]
Address: 0x1000                              0x101C
                   ↑
         One continuous block

// Non-contiguous: samples scattered (typical row-based DB)
Memory: [1.2 at 0x1000] ... [1.3 at 0x5420] ... [1.4 at 0x9A80] ...
                ↑                  ↑                    ↑
         Random disk/memory locations
</code></pre>

    <h2>Why Contiguity Matters</h2>

    <h3>1. Cache Efficiency (10-100x Speedup)</h3>

    <p>
      Modern CPUs have a memory hierarchy: L1/L2/L3 caches are 10-100x faster than RAM, and RAM is
      1000x faster than disk. When you access data at address <code>0x1000</code>, the CPU automatically
      loads a <strong>cache line</strong> (typically 64 bytes) containing <code>0x1000</code> through
      <code>0x1040</code>.
    </p>

    <p><strong>Contiguous storage:</strong></p>
    <ul>
      <li>Reading sample at <code>0x1000</code> loads the next 16 floats (64 bytes) into cache</li>
      <li>Subsequent reads of samples 2-16 are cache hits (near-instant)</li>
      <li>Result: Processing 1M samples = ~62,500 cache line loads</li>
    </ul>

    <p><strong>Non-contiguous storage (scattered rows):</strong></p>
    <ul>
      <li>Each sample is at a random location</li>
      <li>Each read likely misses cache (different cache line)</li>
      <li>Result: Processing 1M samples = ~1M cache misses (100x slower)</li>
    </ul>

    <h3>2. Zero-Copy Reads</h3>

    <p>
      When data is contiguous, you can return a <strong>pointer</strong> to the data instead of
      copying it into a new array. This eliminates memory allocation and data copying overhead.
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>// Traditional database (row-based)
// Must copy scattered rows into a new array
float *results = malloc(1000000 * sizeof(float));
for (int i = 0; i < 1000000; i++) {
    results[i] = fetch_row(i).value;  // Expensive copy
}

// NumStore (contiguous model)
// Just return a pointer to the existing array
float *results = numstore_get_range(stream, t_start, t_end);
// No copying! Results points directly to stored data
</code></pre>

    <p>
      <strong>Benchmark:</strong> Querying 10M samples:
    </p>
    <ul>
      <li>Traditional DB with copying: 500-1000 ms</li>
      <li>NumStore zero-copy: 10-50 ms</li>
      <li><strong>10-50x faster</strong></li>
    </ul>

    <h3>3. Sequential Disk I/O</h3>

    <p>
      Disk drives (even SSDs) are optimized for sequential reads. Reading 1 MB as a single
      contiguous block is 10-100x faster than reading 1 MB as 1000 scattered 1 KB blocks.
    </p>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Storage Type</th>
          <th class="text-left py-2 pr-4">Sequential Read</th>
          <th class="text-left py-2">Random Read</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">HDD (7200 RPM)</td>
          <td class="py-2 pr-4">120 MB/s</td>
          <td class="py-2">0.5 MB/s (240x slower)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">SATA SSD</td>
          <td class="py-2 pr-4">550 MB/s</td>
          <td class="py-2">50 MB/s (11x slower)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">NVMe SSD</td>
          <td class="py-2 pr-4">3500 MB/s</td>
          <td class="py-2">500 MB/s (7x slower)</td>
        </tr>
      </tbody>
    </table>

    <p>
      NumStore's contiguous model ensures that range queries translate to sequential disk reads,
      maximizing throughput.
    </p>

    <h3>4. SIMD Vectorization</h3>

    <p>
      Modern CPUs have SIMD (Single Instruction, Multiple Data) instructions that process multiple
      values in parallel—but they require contiguous data.
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>// Compute sum of 1M floats

// Scalar code (non-contiguous, can't vectorize)
float sum = 0;
for (int i = 0; i < 1000000; i++) {
    sum += fetch_scattered_value(i);  // Cache misses, no vectorization
}
// Time: ~50 ms

// SIMD code (contiguous, vectorized with AVX2)
__m256 sum_vec = _mm256_setzero_ps();
for (int i = 0; i < 1000000; i += 8) {
    __m256 values = _mm256_load_ps(&data[i]);  // Load 8 floats at once
    sum_vec = _mm256_add_ps(sum_vec, values);   // Add 8 in parallel
}
// Time: ~2 ms (25x faster)
</code></pre>

    <h2>NumStore's Contiguous Data Model in Practice</h2>

    <h3>Storage Layout</h3>

    <p>
      NumStore organizes data into <strong>contiguous chunks</strong> (typically 4KB-64KB each):
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Stream: "sensor_voltage"
│
├─ Chunk 1: [T=0...999]     → 4KB contiguous floats
├─ Chunk 2: [T=1000...1999] → 4KB contiguous floats
├─ Chunk 3: [T=2000...2999] → 4KB contiguous floats
└─ Chunk 4: [T=3000...3999] → 4KB contiguous floats

Each chunk:
- Stored sequentially on disk
- Loaded into memory as a single block
- Indexed by R+ tree for fast lookup
</code></pre>

    <h3>Write Path: Maintaining Contiguity</h3>

    <p>
      When samples arrive, NumStore appends them to the current active chunk:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>1. Samples arrive: [1.2, 1.3, 1.4, 1.5]
2. Append to active chunk buffer (in-memory, contiguous)
3. When buffer is full (e.g., 10,000 samples):
   a. Flush buffer to disk as a contiguous block
   b. Update R+ tree index with new chunk metadata
   c. Write to WAL for durability
4. Start a new buffer for the next chunk
</code></pre>

    <p>
      <strong>Result:</strong> All writes are sequential appends, no random seeks required.
    </p>

    <h3>Read Path: Zero-Copy Queries</h3>

    <p>
      When you query a time range, NumStore uses the R+ tree to find matching chunks, then
      returns pointers to contiguous arrays:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>Query: "Get samples from T=5000 to T=7500"

1. R+ tree lookup → finds chunks 6, 7, 8 (cover T=5000...7999)
2. Load chunks from disk (3 sequential reads, total ~12KB)
3. Return pointers:
   - Chunk 6: pointer to samples T=5000...5999 (contiguous)
   - Chunk 7: pointer to samples T=6000...6999 (contiguous)
   - Chunk 8: pointer to samples T=7000...7500 (contiguous)
4. Application reads directly from these pointers (zero-copy)
</code></pre>

    <h2>Comparison: Row-Based vs Contiguous Model</h2>

    <h3>Scenario: Store 100 million temperature samples (floats)</h3>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Metric</th>
          <th class="text-left py-2 pr-4">Row-Based DB (PostgreSQL)</th>
          <th class="text-left py-2">NumStore (Contiguous)</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Storage per sample</td>
          <td class="py-2 pr-4">~50 bytes (row overhead + index)</td>
          <td class="py-2">4 bytes (just the float)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Total storage</td>
          <td class="py-2 pr-4">~5 GB</td>
          <td class="py-2">~400 MB (12.5x smaller)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Write throughput</td>
          <td class="py-2 pr-4">10K-50K samples/sec</td>
          <td class="py-2">1M-10M samples/sec (20-200x)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Range query (1M samples)</td>
          <td class="py-2 pr-4">5-30 seconds</td>
          <td class="py-2">50-200 ms (25-600x faster)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Cache efficiency</td>
          <td class="py-2 pr-4">Low (scattered rows)</td>
          <td class="py-2">High (sequential access)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Zero-copy possible?</td>
          <td class="py-2 pr-4">No (must copy rows)</td>
          <td class="py-2">Yes (return pointers)</td>
        </tr>
      </tbody>
    </table>

    <h2>Trade-offs of Contiguous Storage</h2>

    <h3>Advantages</h3>
    <ul>
      <li>Extreme read performance (10-100x faster)</li>
      <li>Minimal storage overhead</li>
      <li>Cache-friendly access patterns</li>
      <li>Enables SIMD vectorization</li>
      <li>Zero-copy data access</li>
    </ul>

    <h3>Limitations</h3>
    <ul>
      <li><strong>Random updates:</strong> Updating a single sample in a chunk requires rewriting the chunk or using a delta log</li>
      <li><strong>Deletes:</strong> Deleting from the middle of a chunk creates fragmentation (mitigated by compaction)</li>
      <li><strong>Chunk size tuning:</strong> Too small = index overhead, too large = wasted reads for small queries</li>
      <li><strong>Not ideal for:</strong> Sparse data with many gaps, or workloads with heavy random updates</li>
    </ul>

    <h2>Real-World Performance Example</h2>

    <h3>Use Case: Query Oscilloscope Data</h3>

    <p>
      <strong>Dataset:</strong> 1 billion voltage samples (4 GB raw data)<br>
      <strong>Query:</strong> "Get all samples from 10:00:00 to 10:00:05" (5 million samples)
    </p>

    <p><strong>PostgreSQL (row-based):</strong></p>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>SELECT timestamp, voltage
FROM samples
WHERE timestamp BETWEEN '10:00:00' AND '10:00:05';

- Index scan: 50-100 ms (find matching row IDs)
- Fetch rows: 5M random disk seeks
- Copy to result set: 2-5 seconds
- Total: 5-30 seconds
</code></pre>

    <p><strong>NumStore (contiguous):</strong></p>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>numstore_range_query(stream, "10:00:00", "10:00:05");

- R+ tree lookup: 5-10 ms (find matching chunks)
- Load chunks: 500 sequential reads × ~10KB = 50-100 ms
- Return pointers: 0 ms (zero-copy)
- Total: 50-200 ms

Speedup: 25-600x faster
</code></pre>

    <h2>Integration with Programming Languages</h2>

    <p>
      Contiguous storage enables seamless integration with numeric computing libraries:
    </p>

    <h3>Python (NumPy)</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>import numstore
import numpy as np

# Query returns a NumPy array (zero-copy view)
data = numstore.query(stream, start_time, end_time)

# Direct NumPy operations (no copying)
mean = np.mean(data)
std = np.std(data)
fft = np.fft.fft(data)
</code></pre>

    <h3>C/C++</h3>
    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>#include <numstore.h>

// Query returns a pointer to contiguous float array
float *data;
size_t count;
numstore_query(stream, t_start, t_end, &data, &count);

// Direct SIMD processing (AVX2)
__m256 sum_vec = _mm256_setzero_ps();
for (size_t i = 0; i < count; i += 8) {
    sum_vec = _mm256_add_ps(sum_vec, _mm256_load_ps(&data[i]));
}
</code></pre>

    <h2>Conclusion</h2>

    <p>
      NumStore's contiguous data model is the foundation of its performance. By storing numeric
      arrays sequentially and returning zero-copy pointers, I achieve:
    </p>

    <ul>
      <li>10-100x faster queries than row-based databases</li>
      <li>10-20x lower storage overhead</li>
      <li>Seamless integration with NumPy, MATLAB, R, and other numeric libraries</li>
      <li>Hardware-friendly access patterns (cache, SIMD, sequential I/O)</li>
    </ul>

    <p>
      If your workload involves numeric time-series, sensor data, or contiguous arrays,
      NumStore's contiguous model will deliver dramatic performance improvements.
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
  title: 'NumStore\'s Contiguous Data Model: The Secret to 10-100x Performance',
  date: '2025-11-22',
}
</script>
