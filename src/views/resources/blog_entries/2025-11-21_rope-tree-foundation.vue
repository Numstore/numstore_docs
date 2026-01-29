<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <header class="mb-8 not-prose">
      <time class="text-sm text-cyan-600 font-medium">{{ meta.date }}</time>
      <h1 class="text-4xl font-bold text-gray-900 mt-2 mb-4">{{ meta.title }}</h1>
    </header>

    <p class="lead text-lg text-gray-700">
      NumStore's architecture combines two fundamental data structures—ropes and R+ trees—to achieve
      both contiguous storage and efficient indexing for numeric time-series data.
    </p>

    <h2>The Core Challenge</h2>

    <p>
      Building a database for time-series data requires balancing two conflicting requirements:
    </p>

    <ol>
      <li><strong>Contiguous storage:</strong> Numeric arrays should be stored sequentially for cache efficiency, zero-copy reads, and fast range queries</li>
      <li><strong>Efficient indexing:</strong> I need O(log n) time to find specific time ranges without scanning the entire dataset</li>
    </ol>

    <p>
      Traditional B-trees (used by most databases) optimize for indexing but destroy data contiguity.
      Simple arrays optimize for contiguity but require O(n) scans.
    </p>

    <p>
      NumStore's solution: <strong>combine rope data structures with R+ tree indexing</strong>.
    </p>

    <h2>Part 1: Rope Data Structure for Contiguous Arrays</h2>

    <h3>What Is a Rope?</h3>

    <p>
      A <strong>rope</strong> is a tree-based data structure for efficiently storing and manipulating large sequences.
      Originally designed for text editors to handle documents with millions of characters, ropes maintain sequences
      in contiguous chunks while allowing efficient insertions and deletions.
    </p>

    <h3>Why Ropes for Numeric Data?</h3>

    <p>
      Instead of storing time-series data as individual samples (with massive per-sample overhead),
      NumStore uses ropes to store <strong>contiguous chunks</strong> of numeric arrays:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>// Traditional approach: each sample is a separate row
[timestamp=T0, value=1.2] → stored at disk location A
[timestamp=T1, value=1.3] → stored at disk location B (scattered)
[timestamp=T2, value=1.4] → stored at disk location C (scattered)
...

// NumStore rope approach: contiguous chunks
Chunk 1: [1.2, 1.3, 1.4, 1.5, ..., 2.1]  // 10,000 samples, contiguous
Chunk 2: [2.1, 2.2, 2.3, 2.4, ..., 3.0]  // 10,000 samples, contiguous
...
</code></pre>

    <h3>Rope Structure in NumStore</h3>

    <p>
      Each rope node contains:
    </p>

    <ul>
      <li><strong>Data chunks:</strong> Leaf nodes store contiguous arrays of numeric samples (typically 4KB-64KB per chunk)</li>
      <li><strong>Metadata:</strong> Each chunk knows its time range, sample count, and data type</li>
      <li><strong>Tree structure:</strong> Internal nodes organize chunks hierarchically for efficient traversal</li>
    </ul>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>struct RopeNode {
    // For leaf nodes
    float *data;           // Contiguous array of samples
    size_t count;          // Number of samples in this chunk
    timestamp_t start_time;
    timestamp_t end_time;

    // For internal nodes
    RopeNode *left;
    RopeNode *right;
    size_t total_samples;  // Total in subtree
};
</code></pre>

    <h3>Benefits of Ropes</h3>

    <ol>
      <li><strong>Contiguity:</strong> Individual chunks are stored contiguously, enabling fast sequential reads</li>
      <li><strong>Cache efficiency:</strong> Reading 10,000 samples = reading one contiguous block, not 10,000 scattered locations</li>
      <li><strong>Zero-copy reads:</strong> Return a pointer to the chunk, no need to copy data into a new array</li>
      <li><strong>Efficient appends:</strong> Add new chunks to the end without reorganizing existing data</li>
    </ol>

    <h2>Part 2: R+ Tree Indexing for Fast Range Queries</h2>

    <h3>What Is an R+ Tree?</h3>

    <p>
      An <strong>R+ tree</strong> (R-plus tree) is a spatial indexing structure designed for multidimensional data.
      Originally developed for geographic information systems (GIS), R+ trees excel at range queries like
      "find all points within this bounding box."
    </p>

    <p>
      For time-series data, I use R+ trees to index <strong>temporal ranges</strong>—treating time as a 1D spatial dimension.
    </p>

    <h3>Why R+ Trees Instead of B-Trees?</h3>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Feature</th>
          <th class="text-left py-2 pr-4">B-Tree</th>
          <th class="text-left py-2">R+ Tree</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Optimized for</td>
          <td class="py-2 pr-4">Point queries (exact key lookup)</td>
          <td class="py-2">Range queries (find all in interval)</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Range query</td>
          <td class="py-2 pr-4">Must visit multiple nodes, possibly scattered</td>
          <td class="py-2">Optimized path, prunes non-overlapping subtrees</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Spatial data</td>
          <td class="py-2 pr-4">Not designed for 2D/3D ranges</td>
          <td class="py-2">Native support for spatial/temporal ranges</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4 font-semibold">Insert cost</td>
          <td class="py-2 pr-4">Moderate (rebalancing)</td>
          <td class="py-2">Slightly higher (bounding box updates)</td>
        </tr>
      </tbody>
    </table>

    <h3>R+ Tree Structure in NumStore</h3>

    <p>
      Each R+ tree node contains:
    </p>

    <ul>
      <li><strong>Bounding box:</strong> The time range (start_time, end_time) covered by this subtree</li>
      <li><strong>Child pointers:</strong> References to child nodes or leaf rope chunks</li>
      <li><strong>Statistics:</strong> Min/max values, sample count, compression metadata</li>
    </ul>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>struct RTreeNode {
    // Bounding box (time range for this subtree)
    timestamp_t start_time;
    timestamp_t end_time;

    // Statistics
    float min_value;
    float max_value;
    size_t total_samples;

    // Children
    bool is_leaf;
    union {
        RTreeNode *children[MAX_FANOUT];  // Internal node
        RopeNode *data_chunk;             // Leaf → points to rope chunk
    };
};
</code></pre>

    <h3>How R+ Tree Range Queries Work</h3>

    <p><strong>Query:</strong> "Get all samples between T=1000 and T=2000"</p>

    <ol>
      <li><strong>Start at root:</strong> Check if root's bounding box [T=0, T=10000] overlaps query [T=1000, T=2000]</li>
      <li><strong>Prune non-overlapping children:</strong> Skip subtrees whose bounding boxes don't overlap the query range</li>
      <li><strong>Descend recursively:</strong> Visit only children whose ranges overlap [T=1000, T=2000]</li>
      <li><strong>Reach leaf nodes:</strong> Return pointers to rope chunks that contain matching samples</li>
      <li><strong>Read contiguous data:</strong> Each rope chunk is contiguous, so I read sequential blocks</li>
    </ol>

    <p>
      <strong>Time complexity:</strong> O(log n) tree traversal + O(k) where k = number of matching samples (sequential read)
    </p>

    <h2>Combining Ropes and R+ Trees</h2>

    <p>
      NumStore's architecture integrates both structures:
    </p>

    <pre class="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto"><code>┌─────────────────────────────────────────┐
│          R+ Tree Index                  │  ← Efficient range queries
│   (time-based spatial indexing)         │     O(log n) lookup
└──────────────┬──────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────┐
│          Rope Data Structure            │  ← Contiguous storage
│   (chunked numeric arrays)              │     Fast sequential reads
└─────────────────────────────────────────┘
</code></pre>

    <p>
      <strong>Workflow example:</strong>
    </p>

    <ol>
      <li><strong>Write path:</strong> Incoming samples → append to rope chunk → update R+ tree bounding boxes → commit to WAL</li>
      <li><strong>Read path:</strong> Query [T1, T2] → R+ tree finds matching chunks → return contiguous rope arrays → zero-copy to application</li>
    </ol>

    <h2>Performance Characteristics</h2>

    <table class="w-full border-collapse text-sm my-6">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <th class="text-left py-2 pr-4">Operation</th>
          <th class="text-left py-2 pr-4">Time Complexity</th>
          <th class="text-left py-2">Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Append samples</td>
          <td class="py-2 pr-4">O(1) amortized</td>
          <td class="py-2">Append to current rope chunk</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Range query (time)</td>
          <td class="py-2 pr-4">O(log n + k)</td>
          <td class="py-2">R+ tree traversal + sequential reads</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Point query</td>
          <td class="py-2 pr-4">O(log n)</td>
          <td class="py-2">R+ tree to find containing chunk</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Update sample</td>
          <td class="py-2 pr-4">O(log n)</td>
          <td class="py-2">Find chunk, update in-place, write to WAL</td>
        </tr>
        <tr class="border-b border-gray-200">
          <td class="py-2 pr-4">Delete range</td>
          <td class="py-2 pr-4">O(log n + k)</td>
          <td class="py-2">Mark chunks deleted, update R+ tree</td>
        </tr>
      </tbody>
    </table>

    <h2>Real-World Benefits</h2>

    <p><strong>Scenario:</strong> Query 5 million samples from a dataset of 1 billion samples</p>

    <p><strong>Traditional B-tree database:</strong></p>
    <ul>
      <li>5M random disk seeks to scattered row locations</li>
      <li>Reconstruct 5M rows in memory</li>
      <li>Time: 10-30 seconds</li>
    </ul>

    <p><strong>NumStore (Rope + R+ Tree):</strong></p>
    <ul>
      <li>O(log n) R+ tree traversal to find ~500 rope chunks (10K samples each)</li>
      <li>500 sequential reads of contiguous blocks</li>
      <li>Zero-copy return to application</li>
      <li>Time: 50-200 milliseconds</li>
    </ul>

    <p>
      <strong>Speedup: 50-600x faster</strong>
    </p>

    <h2>Trade-offs and Future Work</h2>

    <h3>Current Limitations</h3>
    <ul>
      <li><strong>Write overhead:</strong> Maintaining R+ tree bounding boxes adds slight overhead compared to pure append-only logs</li>
      <li><strong>Chunk size tuning:</strong> Optimal chunk size depends on workload; too small = index overhead, too large = wasted reads</li>
      <li><strong>Fragmentation:</strong> Deletes and updates can fragment rope chunks over time (mitigated by compaction)</li>
    </ul>

    <h3>Future Optimizations</h3>
    <ul>
      <li><strong>Adaptive chunk sizing:</strong> Automatically adjust chunk size based on access patterns</li>
      <li><strong>Compression:</strong> Apply lightweight compression (delta encoding, run-length) to rope chunks</li>
      <li><strong>Tiered storage:</strong> Hot data in memory ropes, cold data in compressed disk ropes</li>
      <li><strong>Multi-dimensional R+ trees:</strong> Support multi-sensor data with spatial + temporal indexing</li>
    </ul>

    <h2>Academic References</h2>

    <p>
      The rope + R+ tree architecture builds on decades of data structure research:
    </p>

    <ul>
      <li><strong>Ropes:</strong> Boehm, H., Atkinson, R., & Plass, M. (1995). "Ropes: an alternative to strings." Software—Practice and Experience.</li>
      <li><strong>R-trees:</strong> Guttman, A. (1984). "R-trees: A dynamic index structure for spatial searching." SIGMOD.</li>
      <li><strong>R+ trees:</strong> Sellis, T., Roussopoulos, N., & Faloutsos, C. (1987). "The R+-tree: A dynamic index for multi-dimensional objects." VLDB.</li>
    </ul>

    <h2>Try It Yourself</h2>

    <p>
      NumStore's rope + R+ tree implementation is open for exploration. Download NumStore and run
      benchmarks with your own time-series workloads:
    </p>

    <p>
      <a href="/downloads/current">Download NumStore</a><br>
      <a href="/resources/documentation">Read the Documentation</a><br>
      <a href="mailto:hello@numstore.dev">Contact Us</a>
    </p>

    <p class="text-sm text-gray-600 mt-8">
      <em>
        This post provides a conceptual overview of NumStore's data structure design. Implementation
        details may vary. For academic collaborations or deeper technical discussions, contact
        <a href="mailto:academic@numstore.dev">academic@numstore.dev</a>.
      </em>
    </p>
  </article>
</template>


<script lang="ts" setup>
export const meta = {
  title: 'NumStore Architecture: Rope + R+ Tree Data Structure Foundation',
  date: '2025-11-21',
}

export const summary = 'Deep dive into NumStore\'s core architecture: how rope data structures provide contiguous storage while R+ trees enable O(log n) range queries.'
</script>
