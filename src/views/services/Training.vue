<script lang="ts" setup>
const tracks = [
  {
    name: "Operator Essentials",
    length: "1 day",
    audience: "SREs / DevOps",
    color: "cyan",
    takeaways: [
      "Install, configure, and upgrade NumStore",
      "Backups, WAL, and recovery drills",
      "Observability & on-call runbooks"
    ]
  },
  {
    name: "Developer Fundamentals",
    length: "1 day",
    audience: "Backend / Data engineers",
    color: "teal",
    takeaways: [
      "Data modeling for numeric workloads",
      "Client libraries & transactions",
      "Performance-aware read/write patterns"
    ]
  },
  {
    name: "Performance & Internals",
    length: "2 days",
    audience: "Leads / Architects",
    color: "emerald",
    takeaways: [
      "Pager, buffer, and WAL internals",
      "Benchmarking & profiling methodology",
      "Capacity planning and tuning"
    ]
  }
]

const formats = [
  { name: "Remote live", desc: "Zoom/Meet with interactive labs and Q&A" },
  { name: "On-site workshop", desc: "Whiteboard sessions + hands-on exercises" },
  { name: "Private cohort", desc: "Curriculum tailored to your stack and use cases" }
]

const materials = [
  "Slides & lab guides (PDF)",
  "Sample datasets and workloads",
  "Reference configs, dashboards, and scripts",
  "Certificate of completion (optional)"
]
</script>

<template>
  <main class="min-h-screen bg-gray-50">
    <!-- Header -->
    <div class="bg-gradient-to-br from-cyan-600 via-cyan-700 to-teal-800 text-white py-16">
      <div class="max-w-4xl mx-auto px-6">
        <h1 class="text-4xl font-bold mb-4">Training</h1>
        <p class="text-cyan-100 text-lg max-w-2xl">
          Short, practical courses to ramp up teams on NumStore operations, development, and performance.
        </p>
      </div>
    </div>

    <div class="max-w-4xl mx-auto px-6 py-12 space-y-12">
      <!-- Tracks -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Training tracks</h2>
        <div class="grid md:grid-cols-3 gap-6">
          <div v-for="track in tracks" :key="track.name" class="bg-white rounded-xl border border-gray-200 overflow-hidden">
            <div
              class="px-5 py-3"
              :class="{
                'bg-cyan-600': track.color === 'cyan',
                'bg-teal-600': track.color === 'teal',
                'bg-emerald-600': track.color === 'emerald'
              }"
            >
              <h3 class="font-semibold text-white">{{ track.name }}</h3>
              <p class="text-white/80 text-sm">{{ track.length }} · {{ track.audience }}</p>
            </div>
            <div class="p-5">
              <p class="text-sm text-gray-500 mb-3">You'll learn:</p>
              <ul class="space-y-2">
                <li v-for="item in track.takeaways" :key="item" class="flex items-start gap-2 text-sm">
                  <svg class="w-4 h-4 text-cyan-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  </svg>
                  <span class="text-gray-700">{{ item }}</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <!-- Formats -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Delivery formats</h2>
        <div class="grid md:grid-cols-3 gap-4">
          <div v-for="format in formats" :key="format.name" class="bg-white rounded-lg border border-gray-200 p-5">
            <h3 class="font-semibold text-gray-900 mb-1">{{ format.name }}</h3>
            <p class="text-sm text-gray-600">{{ format.desc }}</p>
          </div>
        </div>
      </section>

      <!-- Materials -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-6">What's included</h2>
        <div class="bg-white rounded-lg border border-gray-200 p-6">
          <ul class="grid md:grid-cols-2 gap-3">
            <li v-for="item in materials" :key="item" class="flex items-start gap-3">
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
        <h2 class="text-2xl font-bold text-white mb-3">Request a session</h2>
        <p class="text-gray-400 mb-6 max-w-lg mx-auto">
          Include your preferred dates, time zone, group size, and any custom topics (e.g., k8s, Prometheus, specific language bindings).
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="mailto:training@numstore.dev" class="px-6 py-3 bg-cyan-600 text-white font-medium rounded-lg hover:bg-cyan-700 transition-colors">
            Email training@numstore.dev
          </a>
          <RouterLink to="/about/contact" class="px-6 py-3 bg-gray-700 text-white font-medium rounded-lg hover:bg-gray-600 transition-colors">
            Book a call
          </RouterLink>
        </div>
      </section>
    </div>
  </main>
</template>
