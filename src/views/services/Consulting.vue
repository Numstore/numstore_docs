<script lang="ts" setup>
const offerings = [
  { title: "Architecture reviews", desc: "Storage layout, WAL, recovery, and durability design" },
  { title: "Performance tuning", desc: "Ingest optimization, query performance, memory and I/O profiling" },
  { title: "Migrations & upgrades", desc: "Zero/low-downtime migrations with rollback plans" },
  { title: "Observability setup", desc: "Logs, metrics, tracing, and dashboard configuration" },
  { title: "Capacity planning", desc: "Growth projections and cost modeling" },
  { title: "Security reviews", desc: "CVE posture, supply chain analysis, and hardening" }
]

const engagementModels = [
  { name: "Advisory", desc: "Hourly or block-based consulting for specific questions" },
  { name: "Fixed-scope", desc: "Statement of work with defined deliverables and timeline" },
  { name: "Embedded", desc: "Weekly or monthly allocation as part of your team" }
]

const deliverables = [
  "Written report with findings and prioritized recommendations",
  "Issue backlog with task breakdown and severity/impact",
  "Benchmarks, profiles, and reproducible test scripts",
  "Runbooks and operational checklists"
]
</script>

<template>
  <main class="min-h-screen bg-gray-50">
    <!-- Header -->
    <div class="bg-gradient-to-br from-cyan-600 via-cyan-700 to-teal-800 text-white py-16">
      <div class="max-w-4xl mx-auto px-6">
        <h1 class="text-4xl font-bold mb-4">Consulting</h1>
        <p class="text-cyan-100 text-lg max-w-2xl">
          Pragmatic help to ship, scale, and stabilize NumStore in real systems—from commercial
          deployments to cutting-edge research environments.
        </p>
      </div>
    </div>

    <div class="max-w-4xl mx-auto px-6 py-12 space-y-12">
      <!-- Academic Notice -->
      <section class="bg-blue-50 border border-blue-200 rounded-xl p-6">
        <div class="flex items-start gap-4">
          <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
            <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
            </svg>
          </div>
          <div>
            <h2 class="text-lg font-semibold text-blue-900 mb-2">Academic & Research Consulting</h2>
            <p class="text-gray-700 mb-3">
              Research institutions qualify for <strong>discounted consulting rates</strong> and flexible engagement models.
              I've helped labs optimize data collection pipelines and scale NumStore for scientific computing.
            </p>
            <a href="mailto:academic@numstore.dev" class="inline-flex items-center text-blue-600 font-medium hover:text-blue-700">
              Contact academic@numstore.dev
              <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
              </svg>
            </a>
          </div>
        </div>
      </section>

      <!-- What I do -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-6">What I do</h2>
        <div class="grid md:grid-cols-2 gap-4">
          <div v-for="item in offerings" :key="item.title" class="bg-white rounded-lg border border-gray-200 p-5">
            <h3 class="font-semibold text-gray-900 mb-1">{{ item.title }}</h3>
            <p class="text-sm text-gray-600">{{ item.desc }}</p>
          </div>
        </div>
      </section>

      <!-- Engagement Models -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Engagement models</h2>
        <div class="grid md:grid-cols-3 gap-4">
          <div v-for="model in engagementModels" :key="model.name" class="bg-white rounded-lg border border-gray-200 p-5 text-center">
            <div class="w-12 h-12 bg-cyan-100 rounded-lg flex items-center justify-center mx-auto mb-3">
              <svg class="w-6 h-6 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h3 class="font-semibold text-gray-900 mb-1">{{ model.name }}</h3>
            <p class="text-sm text-gray-600">{{ model.desc }}</p>
          </div>
        </div>
      </section>

      <!-- Deliverables -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Deliverables</h2>
        <div class="bg-white rounded-lg border border-gray-200 p-6">
          <ul class="space-y-3">
            <li v-for="item in deliverables" :key="item" class="flex items-start gap-3">
              <svg class="w-5 h-5 text-cyan-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <span class="text-gray-700">{{ item }}</span>
            </li>
          </ul>
        </div>
      </section>

      <!-- CTA -->
      <section class="bg-gray-900 rounded-2xl p-8 text-center">
        <h2 class="text-2xl font-bold text-white mb-3">Get in touch</h2>
        <p class="text-gray-400 mb-6 max-w-lg mx-auto">
          Describe your project, timeline, and goals. I'll respond with availability and a proposal.
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="mailto:consulting@numstore.dev" class="px-6 py-3 bg-cyan-600 text-white font-medium rounded-lg hover:bg-cyan-700 transition-colors">
            Email consulting@numstore.dev
          </a>
          <RouterLink to="/about/contact" class="px-6 py-3 bg-gray-700 text-white font-medium rounded-lg hover:bg-gray-600 transition-colors">
            Book a call
          </RouterLink>
        </div>
      </section>
    </div>
  </main>
</template>
