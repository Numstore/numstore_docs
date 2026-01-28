<template>
  <article class="prose max-w-3xl mx-auto px-6 py-12">
    <header class="mb-8 not-prose">
      <time class="text-sm text-cyan-600 font-medium">{{ meta.date }}</time>
      <h1 class="text-4xl font-bold text-gray-900 mt-2 mb-4">{{ meta.title }}</h1>
    </header>

    <p class="lead text-lg text-gray-700">
      Today, I'm excited to announce a major shift in how I'm positioning NumStore:
      as a database purpose-built for academic research and scientific computing—while
      remaining powerful enough for demanding enterprise workloads.
    </p>

    <h2>Why Academic Research?</h2>

    <p>
      NumStore was born from a simple observation: researchers working with time-series data,
      sensor readings, experimental measurements, and numeric datasets face unique challenges
      that traditional databases weren't designed to solve.
    </p>

    <p>
      Whether you're capturing oscilloscope traces, storing particle collision data, recording
      environmental sensor readings, or managing large-scale simulation outputs, you need:
    </p>

    <ul>
      <li><strong>Extreme write performance</strong> for continuous data collection</li>
      <li><strong>Efficient numeric storage</strong> without the overhead of general-purpose formats</li>
      <li><strong>Simple integration</strong> into existing research workflows and languages</li>
      <li><strong>Reliability</strong> you can trust with irreplaceable experimental data</li>
    </ul>

    <p>
      NumStore delivers on all of these—and I want to make it accessible to every researcher
      who could benefit from it.
    </p>

    <h2>Academic Research Program</h2>

    <p>Starting today, I'm launching my Academic Research Program with:</p>

    <ul>
      <li><strong>Free licenses</strong> for qualifying student projects and academic labs</li>
      <li><strong>Heavily discounted pricing</strong> for research institutions (up to 90% off commercial rates)</li>
      <li><strong>Direct technical support</strong> with priority access to me directly</li>
      <li><strong>Co-development opportunities</strong> for research groups with specialized needs</li>
    </ul>

    <p>
      I believe groundbreaking research shouldn't be limited by software licensing costs.
      If you're using NumStore to advance science, I want to support you.
    </p>

    <h2>Built for Researchers, Scaled for Business</h2>

    <p>
      While I'm emphasizing academic use, NumStore remains a production-ready database for
      commercial applications. The same features that make it ideal for research—high performance,
      reliability, and flexibility—make it excellent for:
    </p>

    <ul>
      <li>IoT and industrial sensor data collection</li>
      <li>Financial time-series and market data</li>
      <li>Telemetry and observability systems</li>
      <li>Machine learning feature stores and training data</li>
      <li>High-frequency trading and analytics pipelines</li>
    </ul>

    <h2>What Makes NumStore Different</h2>

    <h3>1. Pure C, Zero Dependencies</h3>
    <p>
      NumStore is written in 100% dependency-free C. This means you can embed it in any
      environment—Python, Java, Go, Rust, MATLAB, R, or custom C/C++ applications. No complex
      runtime dependencies, no version conflicts, just clean integration.
    </p>

    <h3>2. Early Adoption Advantage</h3>
    <p>
      I'm in the early stages of development, which is actually an opportunity. Join now and:
    </p>
    <ul>
      <li>Influence the feature roadmap based on your research needs</li>
      <li>Get direct access to maintainers and engineers</li>
      <li>Shape the future of numeric data storage</li>
      <li>Establish yourself as an early expert in the ecosystem</li>
    </ul>

    <h3>3. Extreme Performance</h3>
    <p>
      NumStore is optimized for what researchers do most: collecting and querying numeric data.
      In benchmarks against traditional oscilloscope data readers and general-purpose databases,
      NumStore shows <strong>10-100x performance improvements</strong> for numeric-heavy workloads.
    </p>

    <p>
      For a typical use case—streaming 1M samples/second from a data acquisition system—NumStore
      can ingest and index data with sub-millisecond latency while traditional solutions struggle
      with multi-second delays or dropped samples.
    </p>

    <h2>Technical Foundation</h2>

    <p>NumStore is built on solid computer science fundamentals:</p>

    <ul>
      <li><strong>R+ tree engine</strong> with O(log n) insert and search operations</li>
      <li><strong>Rope-based data structure</strong> for efficient contiguous numeric storage</li>
      <li><strong>Write-ahead logging (WAL)</strong> with two-phase commit semantics</li>
      <li><strong>Contiguous data model</strong> optimized for numeric arrays and time-series</li>
      <li><strong>Full rollback support</strong> for experimental workflows</li>
    </ul>

    <p>
      I'll be publishing detailed blog posts about each of these architectural decisions in
      the coming weeks.
    </p>

    <h2>Get Started Today</h2>

    <p>
      Ready to try NumStore in your research? Here's how to get started:
    </p>

    <ol>
      <li><strong>Download NumStore</strong> from my <a href="/downloads/current">downloads page</a></li>
      <li><strong>Check the documentation</strong> for installation and quickstart guides</li>
      <li><strong>Apply for academic access</strong> by emailing <a href="mailto:academic@numstore.dev">academic@numstore.dev</a> with:
        <ul>
          <li>Your institution and research area</li>
          <li>A brief description of your use case</li>
          <li>Your timeline and requirements</li>
        </ul>
      </li>
    </ol>

    <h2>Looking Forward</h2>

    <p>
      This is just the beginning. I'm committed to building the best database for numeric
      and time-series data, and I want to do it in partnership with the research community.
    </p>

    <p>
      Whether you're running a physics experiment, collecting environmental data, training
      machine learning models, or building the next generation of scientific instruments,
      I'd love to hear from you.
    </p>

    <p>
      Welcome to NumStore. Let's advance science together.
    </p>

    <hr class="my-8">

    <p class="text-sm text-gray-600">
      <strong>Contact:</strong><br>
      Academic inquiries: <a href="mailto:academic@numstore.dev">academic@numstore.dev</a><br>
      General questions: <a href="mailto:hello@numstore.dev">hello@numstore.dev</a><br>
      Enterprise: <a href="mailto:enterprise@numstore.dev">enterprise@numstore.dev</a>
    </p>
  </article>
</template>


<script lang="ts" setup>
export const meta = {
  title: 'Announcing NumStore: Built for Academic Research, Scaled for Business',
  date: '2025-11-18',
}

export const summary = 'Introducing the NumStore Academic Research Program with free licenses for students, discounted pricing for institutions, and direct technical support for researchers.'
</script>
