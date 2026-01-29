<script lang="ts" setup>
type Plan = {
  name: string
  bestFor: string
  response: string
  hours: string
  channels: string[]
  highlight?: boolean
}

const plans: Plan[] = [
  {
    name: "Academic Research",
    bestFor: "Universities, research labs, and educational institutions",
    response: "1-2 business days for technical questions",
    hours: "Mon–Fri, 9am–6pm (your local time)",
    channels: ["Email", "Academic Portal"]
  },
  {
    name: "Standard",
    bestFor: "Teams adopting NumStore in non-critical workflows",
    response: "Business-hours response, next-business-day target",
    hours: "Mon–Fri, 9am–6pm (your local time)",
    channels: ["Email", "Customer Portal"]
  },
  {
    name: "Priority",
    bestFor: "Production deployments with uptime needs",
    response: "4 business hours initial response",
    hours: "Mon–Fri, 9am–9pm (your local time)",
    channels: ["Email", "Portal", "Slack Connect"],
    highlight: true
  },
  {
    name: "Enterprise",
    bestFor: "Mission-critical, 24/7 support + architectural guidance",
    response: "1 hour (P1) / 4 hours (P2) / 1 business day (P3)",
    hours: "24×7 for P1; extended business hours for P2/P3",
    channels: ["Email", "Portal", "Slack Connect", "On-call hotline"]
  }
]

const inclusions = [
  "Break/fix support for NumStore core and official bindings",
  "Security advisories, CVE notifications, and upgrade guidance",
  "Best-practice reviews for schema/layout and WAL configuration",
  "Performance tuning tips, profiling templates, and checklists",
  "LTS branches & backports for supported versions",
  "Release notes and migration guides"
]

const priorities = [
  {
    p: "P1",
    label: "Critical outage",
    target: "1h (Enterprise), 4h (Priority), NBD (Standard)",
    desc: "Production down, data at risk, or severe security issue",
    color: "red"
  },
  {
    p: "P2",
    label: "Degraded service",
    target: "4h (Enterprise), same day (Priority), 2 BD (Standard)",
    desc: "Material impact with workaround",
    color: "yellow"
  },
  {
    p: "P3",
    label: "General question",
    target: "1 BD (Enterprise/Priority), 2–3 BD (Standard)",
    desc: "How-to, tuning, minor bugs",
    color: "green"
  }
]
</script>

<template>
  <main class="min-h-screen bg-gray-50">
    <!-- Header -->
    <div class="bg-gradient-to-br from-cyan-600 via-cyan-700 to-teal-800 text-white py-16">
      <div class="max-w-4xl mx-auto px-6">
        <h1 class="text-4xl font-bold mb-4">Enterprise Support</h1>
        <p class="text-cyan-100 text-lg max-w-2xl">
          Keep NumStore reliable in production with guaranteed response targets, escalation paths,
          and direct support access.
        </p>
      </div>
    </div>

    <div class="max-w-4xl mx-auto px-6 py-12 space-y-12">
      <!-- Academic Notice -->
      <section class="bg-blue-50 border border-blue-200 rounded-xl p-6">
        <div class="flex items-start gap-4">
          <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
            <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/>
            </svg>
          </div>
          <div>
            <h2 class="text-lg font-semibold text-blue-900 mb-2">Academic & Research Institutions</h2>
            <p class="text-gray-700 mb-3">
              I offer <strong>free or heavily discounted</strong> support plans for qualifying academic institutions,
              research labs, and educational projects.
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

      <!-- What's Included -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-6">What's included</h2>
        <div class="grid md:grid-cols-2 gap-4">
          <div v-for="item in inclusions" :key="item" class="flex items-start gap-3 p-4 bg-white rounded-lg border border-gray-200">
            <div class="w-8 h-8 bg-cyan-100 rounded-lg flex items-center justify-center flex-shrink-0">
              <svg class="w-4 h-4 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
              </svg>
            </div>
            <span class="text-gray-700">{{ item }}</span>
          </div>
        </div>
      </section>

      <!-- Plans -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Plans</h2>
        <div class="grid md:grid-cols-2 gap-6">
          <div
            v-for="plan in plans"
            :key="plan.name"
            class="bg-white rounded-xl border p-6"
            :class="plan.highlight ? 'border-cyan-400 ring-2 ring-cyan-100' : 'border-gray-200'"
          >
            <div class="flex items-center justify-between mb-3">
              <h3 class="text-lg font-semibold text-gray-900">{{ plan.name }}</h3>
              <span v-if="plan.highlight" class="px-2 py-1 bg-cyan-100 text-cyan-700 text-xs font-medium rounded">Popular</span>
            </div>
            <p class="text-sm text-gray-600 mb-4">{{ plan.bestFor }}</p>
            <div class="space-y-2 text-sm">
              <div class="flex items-start gap-2">
                <span class="text-gray-500 w-24 flex-shrink-0">Response:</span>
                <span class="text-gray-700">{{ plan.response }}</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-gray-500 w-24 flex-shrink-0">Hours:</span>
                <span class="text-gray-700">{{ plan.hours }}</span>
              </div>
              <div class="flex items-start gap-2">
                <span class="text-gray-500 w-24 flex-shrink-0">Channels:</span>
                <span class="text-gray-700">{{ plan.channels.join(", ") }}</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- SLA Targets -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-6">SLA Targets</h2>
        <div class="space-y-4">
          <div v-for="row in priorities" :key="row.p" class="bg-white rounded-lg border border-gray-200 p-4">
            <div class="flex items-center gap-3 mb-2">
              <span
                class="px-2 py-1 text-xs font-bold rounded"
                :class="{
                  'bg-red-100 text-red-700': row.color === 'red',
                  'bg-yellow-100 text-yellow-700': row.color === 'yellow',
                  'bg-green-100 text-green-700': row.color === 'green'
                }"
              >{{ row.p }}</span>
              <span class="font-semibold text-gray-900">{{ row.label }}</span>
            </div>
            <p class="text-sm text-gray-600 mb-2">{{ row.desc }}</p>
            <p class="text-sm text-gray-500">Target: {{ row.target }}</p>
          </div>
        </div>
      </section>

      <!-- FAQ -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-6">FAQ</h2>
        <div class="space-y-4">
          <details class="bg-white rounded-lg border border-gray-200 p-4 group">
            <summary class="cursor-pointer font-medium text-gray-900 flex items-center justify-between">
              Do you offer custom SLAs?
              <svg class="w-5 h-5 text-gray-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </summary>
            <p class="mt-3 text-gray-600">
              Yes. Enterprise plans can include custom hours, contacts, and response targets.
            </p>
          </details>
          <details class="bg-white rounded-lg border border-gray-200 p-4 group">
            <summary class="cursor-pointer font-medium text-gray-900 flex items-center justify-between">
              What versions are supported?
              <svg class="w-5 h-5 text-gray-400 group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </summary>
            <p class="mt-3 text-gray-600">
              Current and LTS releases. I backport critical fixes to supported LTS branches.
            </p>
          </details>
        </div>
      </section>

      <!-- CTA -->
      <section class="bg-gray-900 rounded-2xl p-8 text-center">
        <h2 class="text-2xl font-bold text-white mb-3">Get started</h2>
        <p class="text-gray-400 mb-6 max-w-lg mx-auto">
          Tell me about your deployment, SLA needs, and timeline.
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <a href="mailto:support@numstore.dev" class="px-6 py-3 bg-cyan-600 text-white font-medium rounded-lg hover:bg-cyan-700 transition-colors">
            Email support@numstore.dev
          </a>
          <RouterLink to="/about/contact" class="px-6 py-3 bg-gray-700 text-white font-medium rounded-lg hover:bg-gray-600 transition-colors">
            Book a call
          </RouterLink>
        </div>
      </section>
    </div>
  </main>
</template>
