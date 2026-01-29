<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <header class="mb-8 not-prose">
      <time class="text-sm text-cyan-600 font-medium">{{ meta.date }}</time>
      <h1 class="text-4xl font-bold text-gray-900 mt-2 mb-4">{{ meta.title }}</h1>
      <p class="text-xl text-gray-600 leading-relaxed">
        Welcome to the NumStore blog. A space for technical deep-dives, release notes,
        and the occasional war story from building a numeric database from scratch.
      </p>
    </header>

    <h2>What to Expect</h2>

    <p>
      This blog will focus on the things that matter when building high-performance data systems:
    </p>

    <ul>
      <li><strong>Release announcements</strong> with detailed changelogs and migration notes</li>
      <li><strong>Architecture deep-dives</strong> into the R+ tree, rope data structures, and WAL implementation</li>
      <li><strong>Performance analysis</strong> with benchmarks, profiling insights, and optimization techniques</li>
      <li><strong>Integration guides</strong> for Python, Java, and other language bindings</li>
      <li><strong>Use case studies</strong> from real-world deployments in research and industry</li>
    </ul>

    <h2>Coming Up</h2>

    <p>
      In the next few posts, I'll cover:
    </p>

    <ul>
      <li>The v1.0.0 stable release and what's included</li>
      <li>Why I chose R+ trees over B-trees for time-series indexing</li>
      <li>How the contiguous data model enables zero-copy reads</li>
      <li>Benchmarks comparing NumStore to PostgreSQL for oscilloscope data</li>
    </ul>

    <h2>Stay Connected</h2>

    <p>
      If you're interested in numeric databases, time-series storage, or just want to follow along
      as I build NumStore, here's how to keep up:
    </p>

    <ul>
      <li>Check back here for new posts</li>
      <li>Follow the project on <a href="https://github.com/Numstore/numstore" target="_blank" rel="noopener">GitHub</a></li>
      <li>Reach out at <a href="mailto:hello@numstore.dev">hello@numstore.dev</a> with questions or ideas</li>
    </ul>

    <p>
      Thanks for reading. Let's build something fast.
    </p>
  </article>
</template>

<script lang="ts" setup>
export const meta = {
  title: 'Hello, World',
  date: '2025-09-01',
}

export const summary = 'Welcome to the NumStore blog. Expect technical deep-dives into database architecture, performance analysis, and release notes.'
</script>
