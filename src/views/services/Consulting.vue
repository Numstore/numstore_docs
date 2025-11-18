<script lang="ts" setup>
const offerings = [
  "Architecture reviews (storage layout, WAL, recovery, durability)",
  "Performance tuning & benchmarking (ingest, query, memory, IO)",
  "Migrations & upgrades (zero/low-downtime, rollback plans)",
  "Observability setup (logs, metrics, tracing, dashboards)",
  "Capacity planning & cost modeling",
  "Security reviews (CVE posture, supply chain, hardening)"
]

const engagementModels = [
  "Advisory (hourly/blocks)",
  "Fixed-scope engagement (statement of work)",
  "Embedded engineer (weekly/monthly allocation)"
]

const deliverables = [
  "Written report with findings and prioritized recommendations",
  "Issue backlog with task breakdown and severity/impact",
  "Benchmarks, profiles, and reproducible test scripts",
  "Runbooks and operational checklists"
]
</script>

<template>
  <main class="max-w-3xl mx-auto px-6 py-12 space-y-10">
    <section class="space-y-2">
      <h1 class="text-3xl font-bold">Consulting</h1>
      <p class="text-gray-700">
        Pragmatic help to ship, scale, and stabilize NumStore in real systems—from commercial deployments
        to cutting-edge research environments.
      </p>
    </section>

    <!-- Academic Consulting Notice ----------------------------------------->
    <section class="bg-blue-50 border border-blue-200 rounded-lg p-5 space-y-2">
      <h2 class="text-lg font-semibold text-blue-900">Academic & Research Consulting</h2>
      <p class="text-gray-700">
        Research institutions qualify for <strong>discounted consulting rates</strong> and flexible engagement
        models. I've helped labs optimize data collection pipelines, implement custom storage strategies
        for experimental data, and scale NumStore for large-scale scientific computing.
      </p>
      <p class="text-sm text-gray-700">
        Contact <a class="underline font-medium" href="mailto:academic@numstore.dev">academic@numstore.dev</a>
        to discuss your research computing needs.
      </p>
    </section>

    <section class="space-y-3">
      <h2 class="text-xl font-semibold">What I do</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li v-for="(item, i) in offerings" :key="i">{{ item }}</li>
      </ul>
    </section>

    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Engagement models</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li v-for="(m, i) in engagementModels" :key="i">{{ m }}</li>
      </ul>
    </section>

    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Deliverables</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li v-for="(d, i) in deliverables" :key="i">{{ d }}</li>
      </ul>
    </section>

    <section class="space-y-2">
      <h2 class="text-xl font-semibold">Get in touch</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li>Email: <a class="underline" href="mailto:consulting@numstore.dev">consulting@numstore.dev</a></li>
        <li>Book a call: <a class="underline" href="/about/contact">/about/contact</a></li>
        <li>Enterprise Support: <a class="underline"
                                   href="/services/enterprise_support">/services/enterprise_support</a></li>
      </ul>
    </section>
  </main>
</template>
