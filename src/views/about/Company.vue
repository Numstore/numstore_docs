<script lang="ts" setup>
const highlights = [
  "Reliable low-level data systems and tooling",
  "Performance-first engineering with simple, predictable UX",
  "Clear documentation, pragmatic APIs, and long-term support",
  "Academic research-friendly with special programs for universities and research institutions"
]

const values = [
  "Simplicity over complexity",
  "Reliability and correctness",
  "Transparency with customers",
  "Sustainable, long-term maintenance",
  "Supporting academic research and open science"
]

const offerings = [
  "NumStore database and bindings",
  "Academic Research Program (free/discounted licenses for qualifying institutions)",
  "Enterprise Support (SLAs, LTS, hotfixes)",
  "Consulting (architecture, performance, migrations)",
  "Training (operators, developers, internals)"
]

const timeline = [
  {when: "2025", what: "Initial public releases of NumStore and early adopter program"},
  {when: "2026", what: "Planned LTS branch and expanded language integrations"}
]
</script>

<template>
  <main class="max-w-3xl mx-auto px-6 py-12 space-y-10">
    <!-- Header -->
    <section class="space-y-2">
      <h1 class="text-3xl font-bold">About NumStore</h1>
      <p class="text-gray-700">
        NumStore is a specialized database system designed for numeric time-series data and scientific computing workloads.
        The system prioritizes write throughput, query performance, and storage efficiency for contiguous numeric arrays.
      </p>
    </section>

    <!-- Design Goals -->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Design Goals</h2>
      <p class="text-gray-700">
        NumStore addresses limitations in traditional relational databases when handling high-frequency numeric data streams.
        Conventional row-based storage introduces significant overhead for numeric arrays, while NumStore's contiguous storage
        model eliminates per-sample metadata and enables direct memory access patterns. The system targets applications requiring
        sustained write rates exceeding 1 million samples per second with sub-millisecond query latency.
      </p>
    </section>

    <!-- Academic Licensing -->
    <section class="space-y-3 bg-blue-50 p-6 rounded-lg border border-blue-200">
      <h2 class="text-xl font-semibold text-blue-900">Academic Licensing</h2>
      <p class="text-gray-700">
        NumStore provides licensing options for academic and research institutions. The system is designed
        to support scientific computing workflows including data acquisition, experimental measurement, and
        computational research.
      </p>
      <ul class="list-disc pl-6 space-y-1">
        <li>No-cost licenses available for qualifying educational and research projects</li>
        <li>Discounted institutional licenses for universities and research organizations</li>
        <li>Technical support for academic users</li>
        <li>Collaboration on domain-specific features for scientific applications</li>
      </ul>
      <p class="text-sm text-gray-700">
        For academic licensing inquiries: <a class="underline font-medium" href="mailto:academic@numstore.dev">academic@numstore.dev</a>
      </p>
    </section>

    <!-- Technical Characteristics -->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Technical Characteristics</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li>Dependency-free C implementation with stable API surface</li>
        <li>Contiguous storage optimized for sequential numeric access</li>
        <li>R+ tree spatial indexing for temporal range queries</li>
        <li>Write-ahead logging with ACID transaction support</li>
      </ul>
    </section>

    <!-- Available Services -->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Available Services</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li>NumStore database and language bindings (Python, Java)</li>
        <li>Academic licensing program for research institutions</li>
        <li>Commercial support contracts with defined SLAs</li>
        <li>Architecture consulting and performance optimization</li>
        <li>Training for operators and developers</li>
      </ul>
      <p class="text-sm text-gray-700">
        See <a class="underline" href="/services/enterprise_support">Support</a>,
        <a class="underline" href="/services/consulting">Consulting</a>, and
        <a class="underline" href="/services/training">Training</a> for details.
      </p>
    </section>

    <!-- Development Philosophy -->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Development Philosophy</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li>Correctness and reliability over feature complexity</li>
        <li>Predictable performance characteristics</li>
        <li>Minimal dependencies and clear API boundaries</li>
        <li>Long-term stability and backward compatibility</li>
      </ul>
    </section>

    <!-- Timeline (simple) -->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Timeline</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li v-for="t in timeline" :key="t.when">
          <strong>{{ t.when }}:</strong> {{ t.what }}
        </li>
      </ul>
    </section>

    <!-- Contact -->
    <section class="space-y-2">
      <h2 class="text-xl font-semibold">Contact</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li>Email: <a class="underline" href="mailto:hello@numstore.dev">hello@numstore.dev</a></li>
        <li>General inquiries: <a class="underline" href="/about/contact">/about/contact</a></li>
        <li>Docs & updates: <a class="underline" href="/resources/documentation">/resources/documentation</a> ·
          <a class="underline" href="/blog">/blog</a></li>
      </ul>
      <p class="text-xs text-gray-600">
        For security issues, please email <a class="underline" href="mailto:security@numstore.dev">security@numstore.dev</a>.
      </p>
    </section>
  </main>
</template>

<style scoped>
/* minimal and readable */
</style>
