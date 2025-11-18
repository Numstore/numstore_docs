<!-- Directory: /blog/entries/2025-11-18_announcing-numstore-academic-research.vue -->
<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <h1>{{ meta.title }}</h1>

    <p class="lead text-lg text-gray-700">
      NumStore is a specialized database system designed for numeric time-series data and scientific computing workloads.
      This document outlines the system architecture, academic licensing programs, and deployment considerations.
    </p>

    <h2>Design Motivation</h2>

    <p>
      Traditional relational databases introduce significant overhead when handling high-frequency numeric data streams.
      NumStore addresses specific limitations in conventional database systems for applications including:
    </p>

    <ul>
      <li>High-frequency data acquisition from instrumentation (oscilloscopes, sensors, detectors)</li>
      <li>Experimental measurement storage with temporal ordering requirements</li>
      <li>Large-scale simulation output management</li>
      <li>Time-series analysis for scientific computing</li>
    </ul>

    <p>
      The system provides:
    </p>

    <ul>
      <li>Sustained write performance exceeding 1M samples/second</li>
      <li>Contiguous storage eliminating per-sample overhead</li>
      <li>Language bindings for Python, Java, and C</li>
      <li>ACID transaction guarantees with write-ahead logging</li>
    </ul>

    <h2>Academic Licensing</h2>

    <p>NumStore provides academic licensing options:</p>

    <ul>
      <li>No-cost licenses for student projects and academic research labs</li>
      <li>Discounted institutional licenses for universities (up to 90% reduction from commercial rates)</li>
      <li>Technical support for academic deployments</li>
      <li>Collaboration on domain-specific features</li>
    </ul>

    <p>
      Academic licensing inquiries: <a href="mailto:academic@numstore.dev">academic@numstore.dev</a>
    </p>

    <h2>Commercial Applications</h2>

    <p>
      NumStore supports both research and production deployments. Commercial use cases include:
    </p>

    <ul>
      <li>IoT and industrial sensor data collection</li>
      <li>Financial time-series and market data storage</li>
      <li>Telemetry and observability systems</li>
      <li>Machine learning feature stores</li>
      <li>High-frequency trading data pipelines</li>
    </ul>

    <h2>Technical Architecture</h2>

    <h3>1. Dependency-Free C Implementation</h3>
    <p>
      NumStore is implemented in standard C with no external dependencies. Language bindings
      provide access through a stable C API, enabling integration with Python, Java, Go, Rust,
      MATLAB, R, and other environments.
    </p>

    <h3>2. Contiguous Storage Model</h3>
    <p>
      Numeric arrays are stored in contiguous memory blocks, enabling:
    </p>
    <ul>
      <li>Zero-copy data access for reduced latency</li>
      <li>Efficient cache utilization through sequential access patterns</li>
      <li>SIMD vectorization for analytical operations</li>
      <li>Direct memory mapping for high-performance queries</li>
    </ul>

    <h3>3. Performance Characteristics</h3>
    <p>
      Benchmark results show 10-100x performance improvements over row-based databases for
      numeric-heavy workloads. For data acquisition at 1 MHz sampling rates, NumStore maintains
      sub-millisecond write latency where traditional databases experience multi-second delays
      or dropped samples.
    </p>

    <h2>System Components</h2>

    <p>NumStore implements:</p>

    <ul>
      <li><strong>R+ tree spatial indexing</strong> — O(log n) range queries on temporal data</li>
      <li><strong>Rope-based data structures</strong> — Efficient contiguous array management</li>
      <li><strong>Write-ahead logging</strong> — ACID guarantees with two-phase commit</li>
      <li><strong>Contiguous data model</strong> — Optimized for numeric arrays and time-series</li>
      <li><strong>Transaction support</strong> — Full rollback capabilities for experimental workflows</li>
    </ul>

    <p>
      Additional technical documentation available in the architecture and implementation blog posts.
    </p>

    <h2>Getting Started</h2>

    <p>
      To evaluate NumStore:
    </p>

    <ol>
      <li>Download from <a href="/downloads/current">downloads page</a></li>
      <li>Review documentation for installation and API reference</li>
      <li>For academic licensing, contact <a href="mailto:academic@numstore.dev">academic@numstore.dev</a> with:
        <ul>
          <li>Institution and research area</li>
          <li>Use case description</li>
          <li>Deployment timeline</li>
        </ul>
      </li>
    </ol>

    <h2>Support and Contact</h2>

    <p>
      For technical questions and deployment assistance:
    </p>

    <ul>
      <li>General inquiries: <a href="mailto:hello@numstore.dev">hello@numstore.dev</a></li>
      <li>Academic licensing: <a href="mailto:academic@numstore.dev">academic@numstore.dev</a></li>
      <li>Commercial support: <a href="mailto:enterprise@numstore.dev">enterprise@numstore.dev</a></li>
    </ul>
  </article>
</template>


<script lang="ts" setup>
const meta = {
  title: 'NumStore: Database System for Numeric Time-Series Data',
  date: '2025-11-18',
}
</script>
