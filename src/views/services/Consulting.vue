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
      <h1 class="text-3xl font-bold">Consulting Services</h1>
      <p class="text-gray-700">
        NumStore consulting services provide technical assistance for deployment, optimization,
        and integration of NumStore in production and research environments.
      </p>
    </section>

    <!-- Academic Consulting Notice ----------------------------------------->
    <section class="bg-blue-50 border border-blue-200 rounded-lg p-5 space-y-2">
      <h2 class="text-lg font-semibold text-blue-900">Academic Consulting Programs</h2>
      <p class="text-gray-700">
        Discounted consulting rates and flexible engagement models are available for research institutions.
        Services include optimization of data acquisition systems, storage strategy implementation,
        and performance tuning for scientific computing workloads.
      </p>
      <p class="text-sm text-gray-700">
        Academic consulting inquiries: <a class="underline font-medium" href="mailto:academic@numstore.dev">academic@numstore.dev</a>
      </p>
    </section>

    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Service Areas</h2>
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
