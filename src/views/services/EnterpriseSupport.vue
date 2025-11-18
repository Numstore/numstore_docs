<script lang="ts" setup>
type Plan = {
  name: string
  bestFor: string
  response: string
  hours: string
  channels: string[]
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
    channels: ["Email", "Portal", "Slack Connect (shared channel)"]
  },
  {
    name: "Enterprise",
    bestFor: "Mission-critical, 24/7 support + architectural guidance",
    response: "1 hour (P1) / 4 hours (P2) / 1 business day (P3)",
    hours: "24×7 for P1; extended business hours for P2/P3",
    channels: ["Email", "Portal", "Slack Connect", "On-call hotline (P1)"]
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

const onboarding = [
  "Kickoff call (goals, SLAs, stakeholders, environments)",
  "Environment review (dev/stage/prod topology)",
  "Observability checklist (logs, metrics, tracing)",
  "Runbook & escalation paths (P1/P2/P3)",
  "Quarterly architecture review (Enterprise)"
]

const priorities = [
  {
    p: "P1 – Critical outage",
    target: "1h (Enterprise), 4h (Priority), NBD (Standard)",
    desc: "Production down, data at risk, or severe security issue"
  },
  {
    p: "P2 – Degraded service",
    target: "4h (Enterprise), same day (Priority), 2 BD (Standard)",
    desc: "Material impact with workaround"
  },
  {
    p: "P3 – General question",
    target: "1 BD (Enterprise/Priority), 2–3 BD (Standard)",
    desc: "How-to, tuning, minor bugs"
  }
]
</script>

<template>
  <main class="max-w-3xl mx-auto px-6 py-12 space-y-10">
    <!-- Header -------------------------------------------------------------->
    <section class="space-y-2">
      <h1 class="text-3xl font-bold">Commercial Support</h1>
      <p class="text-gray-600">
        NumStore offers commercial support contracts with defined service level agreements,
        technical assistance for production deployments, and access to maintenance updates.
      </p>
    </section>

    <!-- Academic Notice ---------------------------------------------------->
    <section class="bg-blue-50 border border-blue-200 rounded-lg p-5 space-y-2">
      <h2 class="text-lg font-semibold text-blue-900">Academic Support Programs</h2>
      <p class="text-gray-700">
        No-cost and discounted support plans are available for academic institutions,
        research laboratories, and educational projects. Academic support includes
        technical assistance for scientific computing and data acquisition systems.
      </p>
      <p class="text-sm text-gray-700">
        Academic support inquiries: <a class="underline font-medium" href="mailto:academic@numstore.dev">academic@numstore.dev</a>
      </p>
    </section>

    <!-- What's Included ----------------------------------------------------->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">What’s included</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li v-for="(item, i) in inclusions" :key="i">{{ item }}</li>
      </ul>
    </section>

    <!-- Plans (simple list, not cards) ------------------------------------->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Plans</h2>
      <ul class="list-disc pl-6 space-y-4">
        <li v-for="p in plans" :key="p.name" class="space-y-1">
          <strong>{{ p.name }}</strong>
          <div class="text-gray-700">{{ p.bestFor }}</div>
          <div><span class="font-medium">Initial response:</span> {{ p.response }}</div>
          <div><span class="font-medium">Support hours:</span> {{ p.hours }}</div>
          <div><span class="font-medium">Channels:</span> {{ p.channels.join(", ") }}</div>
        </li>
      </ul>
    </section>

    <!-- SLAs (plain table style with semantic HTML) ------------------------>
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">SLA Targets</h2>
      <div class="overflow-x-auto">
        <table class="w-full border-collapse text-sm">
          <thead>
          <tr class="text-left border-b">
            <th class="py-2 pr-4">Priority</th>
            <th class="py-2 pr-4">Target response</th>
            <th class="py-2 pr-4">Definition</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="row in priorities" :key="row.p" class="border-b">
            <td class="py-2 pr-4 whitespace-nowrap font-medium">{{ row.p }}</td>
            <td class="py-2 pr-4 whitespace-nowrap">{{ row.target }}</td>
            <td class="py-2 pr-4">{{ row.desc }}</td>
          </tr>
          </tbody>
        </table>
      </div>
      <p class="text-gray-600 text-sm">
        Targets shown are time to first response. Resolution times depend on issue complexity and customer environment.
      </p>
    </section>

    <!-- Onboarding ---------------------------------------------------------->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Onboarding</h2>
      <ol class="list-decimal pl-6 space-y-1">
        <li v-for="(step, i) in onboarding" :key="i">{{ step }}</li>
      </ol>
    </section>

    <!-- Contact CTA --------------------------------------------------------->
    <section class="space-y-2">
      <h2 class="text-xl font-semibold">Support Inquiries</h2>
      <p class="text-gray-700">
        For information on support contracts, include details about your deployment environment,
        SLA requirements, and timeline.
      </p>
      <ul class="list-disc pl-6 space-y-1">
        <li>
          Email:
          <a class="underline" href="mailto:support@numstore.dev">support@numstore.dev</a>
        </li>
        <li>
          Contact form:
          <a class="underline" href="/about/contact">/about/contact</a>
        </li>
        <li>
          Documentation:
          <a class="underline" href="/resources/documentation">/resources/documentation</a>
        </li>
      </ul>
    </section>

    <!-- FAQ (no JS, native details/summary) -------------------------------->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">FAQ</h2>
      <details>
        <summary class="cursor-pointer font-medium">Are custom SLAs available?</summary>
        <div class="mt-2 text-gray-700">
          Enterprise support contracts can include custom response times, availability hours, and escalation procedures.
        </div>
      </details>
      <details>
        <summary class="cursor-pointer font-medium">What versions are supported?</summary>
        <div class="mt-2 text-gray-700">
          Support is provided for current releases and designated long-term support (LTS) branches.
          Critical fixes are backported to supported LTS versions.
        </div>
      </details>
      <details>
        <summary class="cursor-pointer font-medium">How are critical issues escalated?</summary>
        <div class="mt-2 text-gray-700">
          Enterprise support contracts include on-call access and dedicated communication channels.
          P1 issues can be escalated through the support hotline or Slack Connect channel.
        </div>
      </details>
    </section>
  </main>
</template>

<style scoped>
/* keep it minimal and readable */
</style>
