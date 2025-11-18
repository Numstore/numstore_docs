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
      <h1 class="text-3xl font-bold">About The Company</h1>
      <p class="text-gray-700">
        The Company builds dependable software for numeric and systems workloads, including the
        NumStore database. We focus on correctness, performance, and developer ergonomics—with a
        special commitment to advancing academic research and scientific computing.
      </p>
    </section>

    <!-- Academic Mission -->
    <section class="space-y-3 bg-blue-50 p-6 rounded-lg border border-blue-200">
      <h2 class="text-xl font-semibold text-blue-900">Academic Research Program</h2>
      <p class="text-gray-700">
        NumStore was built with researchers in mind. We believe in supporting the scientific community
        and understand the unique constraints of academic environments.
      </p>
      <ul class="list-disc pl-6 space-y-1">
        <li><strong>Free for qualifying educational projects</strong> — Students and academic labs can use NumStore at no cost for research purposes</li>
        <li><strong>Heavily discounted licenses</strong> — Research institutions receive significant pricing reductions</li>
        <li><strong>Direct technical support</strong> — Academic users get priority access to our engineering team</li>
        <li><strong>Co-development opportunities</strong> — We partner with research groups to add features that advance science</li>
      </ul>
      <p class="text-sm text-gray-700">
        Contact us at <a class="underline font-medium" href="mailto:academic@numstore.dev">academic@numstore.dev</a> to discuss your research needs and eligibility.
      </p>
    </section>

    <!-- What we do -->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">What we do</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li v-for="(h, i) in highlights" :key="i">{{ h }}</li>
      </ul>
    </section>

    <!-- Offerings -->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Offerings</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li v-for="(o, i) in offerings" :key="i">{{ o }}</li>
      </ul>
      <p class="text-sm text-gray-700">
        See <a class="underline" href="/services/enterprise_support">Enterprise Support</a>,
        <a class="underline" href="/services/consulting">Consulting</a>, and
        <a class="underline" href="/services/training">Training</a> for details.
      </p>
    </section>

    <!-- Values -->
    <section class="space-y-3">
      <h2 class="text-xl font-semibold">Our values</h2>
      <ul class="list-disc pl-6 space-y-1">
        <li v-for="(v, i) in values" :key="i">{{ v }}</li>
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
        <li>Email: <a class="underline" href="mailto:hello@thecompany.com">hello@thecompany.com</a></li>
        <li>General inquiries: <a class="underline" href="/about/contact">/about/contact</a></li>
        <li>Docs & updates: <a class="underline" href="/resources/documentation">/resources/documentation</a> ·
          <a class="underline" href="/blog">/blog</a></li>
      </ul>
      <p class="text-xs text-gray-600">
        For security issues, please email <a class="underline" href="mailto:security@thecompany.com">security@thecompany.com</a>.
      </p>
    </section>
  </main>
</template>

<style scoped>
/* minimal and readable */
</style>
