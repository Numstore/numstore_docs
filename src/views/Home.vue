<script lang="ts" setup>
import {RouterLink} from 'vue-router'
import {ref} from 'vue'

// For expandable workload cards
const expandedWorkload = ref<string | null>(null)

const workloads = [
  {
    id: 'ml',
    title: 'Machine Learning',
    summary: 'Training data, feature stores, model checkpoints',
    details: 'NumStore provides zero-copy reads that feed directly into NumPy, PyTorch, or TensorFlow. Store training datasets, feature vectors, and embedding arrays with minimal serialization overhead. Perfect for feature stores that need sub-millisecond lookup times during model serving.',
    useCase: 'A recommendation engine storing 100M user embedding vectors, serving 10,000 predictions/sec with <5ms latency per lookup.'
  },
  {
    id: 'scientific',
    title: 'Scientific Computing',
    summary: 'Simulation results, experimental data, sensor arrays',
    details: 'Research labs collect massive amounts of numeric data from instruments—oscilloscopes, spectrometers, particle detectors. NumStore handles high-throughput writes with sub-millisecond latency and native time-series indexing.',
    useCase: 'A physics lab storing 10TB of particle detector data per day, with instant replay of any 1-second window for analysis.'
  },
  {
    id: 'timeseries',
    title: 'Time Series',
    summary: 'IoT telemetry, financial data, monitoring metrics',
    details: 'Contiguous storage model preserves temporal ordering. R+ tree indexing enables fast range queries by timestamp. WAL ensures no data loss during high-volume ingestion from thousands of sources.',
    useCase: 'A trading platform storing 1M tick events/sec with microsecond precision, supporting instant backtesting over years of history.'
  },
  {
    id: 'embedded',
    title: 'Embedded Systems',
    summary: 'Edge devices, robotics, automotive applications',
    details: 'Pure C with zero external dependencies means NumStore runs anywhere—from Raspberry Pi to industrial PLCs. Minimal memory footprint (~500KB) with configurable buffer sizes for constrained environments.',
    useCase: 'An autonomous vehicle logging 100 sensor streams at 100Hz each, with local storage and batch upload when connected.'
  }
]

function toggleWorkload(id: string) {
  expandedWorkload.value = expandedWorkload.value === id ? null : id
}
</script>

<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-cyan-600 via-cyan-700 to-teal-800 text-white">
      <div class="max-w-6xl mx-auto px-6 py-24 md:py-32">
        <div class="max-w-3xl">
          <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-6 leading-tight">
            Build fast, efficient<br/>numeric applications
          </h1>
          <p class="text-xl md:text-2xl text-cyan-100 mb-10 leading-relaxed">
            Numstore is an embedded database designed for machine learning and scientific computing.
            Pure C, zero dependencies, extreme performance.
          </p>
          <div class="flex flex-wrap gap-4">
            <RouterLink
                to="/downloads/current"
                class="inline-flex items-center px-6 py-3 bg-white text-cyan-700 font-semibold rounded-md hover:bg-cyan-50 transition-colors"
            >
              Download
              <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"/>
              </svg>
            </RouterLink>
            <RouterLink
                to="/resources/documentation"
                class="inline-flex items-center px-6 py-3 border-2 border-white text-white font-semibold rounded-md hover:bg-white/10 transition-colors"
            >
              Get Started
              <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </RouterLink>
          </div>
        </div>
      </div>
    </section>

    <!-- Video Demo Section -->
    <section class="py-16 bg-gray-900">
      <div class="max-w-6xl mx-auto px-6">
        <div class="text-center mb-10">
          <h2 class="text-3xl font-bold text-white mb-4">See Numstore in Action</h2>
          <p class="text-gray-400 text-lg max-w-2xl mx-auto">
            Watch how Numstore handles millions of numeric records with blazing fast performance.
          </p>
        </div>
        <div class="relative max-w-4xl mx-auto">
          <div class="aspect-video bg-gray-800 rounded-xl overflow-hidden shadow-2xl border border-gray-700">
            <iframe
              class="w-full h-full"
              src="https://www.youtube.com/embed/dQw4w9WgXcQ"
              title="Numstore Demo"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              allowfullscreen
            ></iframe>
          </div>
          <div class="absolute -bottom-4 -right-4 w-24 h-24 bg-cyan-500/20 rounded-full blur-2xl"></div>
          <div class="absolute -top-4 -left-4 w-32 h-32 bg-teal-500/20 rounded-full blur-2xl"></div>
        </div>
      </div>
    </section>

    <!-- Features Grid -->
    <section class="py-20 bg-gray-50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="grid md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <RouterLink
            to="/resources/blog/2025-11-22_contiguous-data-model"
            class="bg-white rounded-lg p-8 shadow-sm border border-gray-100 hover:border-cyan-300 hover:shadow-lg transition-all group"
          >
            <div class="w-12 h-12 bg-cyan-100 rounded-lg flex items-center justify-center mb-5 group-hover:bg-cyan-200 transition-colors">
              <svg class="w-6 h-6 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-3 group-hover:text-cyan-700 transition-colors">Extreme Performance</h3>
            <p class="text-gray-600 leading-relaxed">
              10-100x faster than traditional databases for numeric workloads. Optimized for time-series, tensors, and scientific data.
            </p>
            <span class="inline-flex items-center text-cyan-600 text-sm mt-4 font-medium">
              Learn more
              <svg class="ml-1 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </span>
          </RouterLink>

          <!-- Feature 2 -->
          <RouterLink
            to="/resources/blog/2025-11-19_numstore-usages"
            class="bg-white rounded-lg p-8 shadow-sm border border-gray-100 hover:border-teal-300 hover:shadow-lg transition-all group"
          >
            <div class="w-12 h-12 bg-teal-100 rounded-lg flex items-center justify-center mb-5 group-hover:bg-teal-200 transition-colors">
              <svg class="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-3 group-hover:text-teal-700 transition-colors">Pure C, Zero Dependencies</h3>
            <p class="text-gray-600 leading-relaxed">
              Written in 100% dependency-free C. Embed into any language—Python, Java, Go, Rust, or your custom stack.
            </p>
            <span class="inline-flex items-center text-teal-600 text-sm mt-4 font-medium">
              Learn more
              <svg class="ml-1 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </span>
          </RouterLink>

          <!-- Feature 3 -->
          <RouterLink
            to="/resources/blog/2025-11-23_usage-example"
            class="bg-white rounded-lg p-8 shadow-sm border border-gray-100 hover:border-emerald-300 hover:shadow-lg transition-all group"
          >
            <div class="w-12 h-12 bg-emerald-100 rounded-lg flex items-center justify-center mb-5 group-hover:bg-emerald-200 transition-colors">
              <svg class="w-6 h-6 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-3 group-hover:text-emerald-700 transition-colors">Type Safe</h3>
            <p class="text-gray-600 leading-relaxed">
              Define schemas with structs, unions, and enums. Catch data errors at write time, not when your model crashes.
            </p>
            <span class="inline-flex items-center text-emerald-600 text-sm mt-4 font-medium">
              Learn more
              <svg class="ml-1 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </span>
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- Documentation Categories Section (Go-style) -->
    <section class="py-20 bg-white border-t border-gray-100">
      <div class="max-w-6xl mx-auto px-6">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900 mb-4">Documentation</h2>
          <p class="text-lg text-gray-600 max-w-2xl mx-auto">
            Everything you need to integrate Numstore into your applications.
          </p>
        </div>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <!-- API Reference -->
          <RouterLink to="/resources/documentation#api" class="group block p-6 bg-gray-50 rounded-lg border border-gray-200 hover:border-cyan-400 hover:bg-cyan-50 transition-all">
            <div class="flex items-center mb-3">
              <svg class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
              </svg>
              <h3 class="font-semibold text-gray-900 group-hover:text-cyan-700">API Reference</h3>
            </div>
            <p class="text-sm text-gray-600">Complete function reference for the C API, data types, and error handling.</p>
          </RouterLink>

          <!-- Network Protocol -->
          <RouterLink to="/resources/documentation#protocol" class="group block p-6 bg-gray-50 rounded-lg border border-gray-200 hover:border-cyan-400 hover:bg-cyan-50 transition-all">
            <div class="flex items-center mb-3">
              <svg class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
              <h3 class="font-semibold text-gray-900 group-hover:text-cyan-700">Network Protocol</h3>
            </div>
            <p class="text-sm text-gray-600">TCP/UDP wire format, connection handling, and client-server communication.</p>
          </RouterLink>

          <!-- Language Reference -->
          <RouterLink to="/resources/documentation#language" class="group block p-6 bg-gray-50 rounded-lg border border-gray-200 hover:border-cyan-400 hover:bg-cyan-50 transition-all">
            <div class="flex items-center mb-3">
              <svg class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
              </svg>
              <h3 class="font-semibold text-gray-900 group-hover:text-cyan-700">Language Reference</h3>
            </div>
            <p class="text-sm text-gray-600">Query syntax, schema definitions, type system, and expression grammar.</p>
          </RouterLink>

          <!-- CLI Tool -->
          <RouterLink to="/resources/documentation#cli" class="group block p-6 bg-gray-50 rounded-lg border border-gray-200 hover:border-cyan-400 hover:bg-cyan-50 transition-all">
            <div class="flex items-center mb-3">
              <svg class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
              </svg>
              <h3 class="font-semibold text-gray-900 group-hover:text-cyan-700">CLI Tool</h3>
            </div>
            <p class="text-sm text-gray-600">Command-line interface for database management, import/export, and debugging.</p>
          </RouterLink>

          <!-- Python Usage -->
          <RouterLink to="/resources/documentation#python" class="group block p-6 bg-gray-50 rounded-lg border border-gray-200 hover:border-cyan-400 hover:bg-cyan-50 transition-all">
            <div class="flex items-center mb-3">
              <svg class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
              </svg>
              <h3 class="font-semibold text-gray-900 group-hover:text-cyan-700">Python Usage</h3>
            </div>
            <p class="text-sm text-gray-600">Python bindings, NumPy integration, and Pythonic API patterns.</p>
          </RouterLink>

          <!-- Java Usage -->
          <RouterLink to="/resources/documentation#java" class="group block p-6 bg-gray-50 rounded-lg border border-gray-200 hover:border-cyan-400 hover:bg-cyan-50 transition-all">
            <div class="flex items-center mb-3">
              <svg class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
              </svg>
              <h3 class="font-semibold text-gray-900 group-hover:text-cyan-700">Java Usage</h3>
            </div>
            <p class="text-sm text-gray-600">JNI bindings, memory management, and integration with JVM applications.</p>
          </RouterLink>

          <!-- Configuration -->
          <RouterLink to="/resources/documentation#config" class="group block p-6 bg-gray-50 rounded-lg border border-gray-200 hover:border-cyan-400 hover:bg-cyan-50 transition-all">
            <div class="flex items-center mb-3">
              <svg class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
              <h3 class="font-semibold text-gray-900 group-hover:text-cyan-700">Configuration</h3>
            </div>
            <p class="text-sm text-gray-600">Server settings, tuning parameters, and deployment configuration.</p>
          </RouterLink>

          <!-- View All Docs -->
          <RouterLink to="/resources/documentation" class="group flex items-center justify-center p-6 bg-cyan-600 rounded-lg hover:bg-cyan-700 transition-colors">
            <span class="text-white font-semibold mr-2">View All Docs</span>
            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
            </svg>
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- Code Example Section -->
    <section class="py-20 bg-gray-50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
          <div>
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Simple, expressive API</h2>
            <p class="text-lg text-gray-600 mb-6 leading-relaxed">
              Numstore's API is designed to be intuitive. Define your schema, write data, and query with minimal boilerplate.
            </p>
            <ul class="space-y-4">
              <li class="flex items-start">
                <svg class="w-6 h-6 text-cyan-600 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span class="text-gray-700">Schema-first design with compile-time validation</span>
              </li>
              <li class="flex items-start">
                <svg class="w-6 h-6 text-cyan-600 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span class="text-gray-700">Zero-copy reads for maximum throughput</span>
              </li>
              <li class="flex items-start">
                <svg class="w-6 h-6 text-cyan-600 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
                <span class="text-gray-700">Native support for multidimensional arrays</span>
              </li>
            </ul>
          </div>
          <div class="bg-gray-900 rounded-xl p-6 shadow-2xl">
            <div class="flex items-center gap-2 mb-4">
              <div class="w-3 h-3 rounded-full bg-red-500"></div>
              <div class="w-3 h-3 rounded-full bg-yellow-500"></div>
              <div class="w-3 h-3 rounded-full bg-green-500"></div>
              <span class="ml-4 text-gray-400 text-sm font-mono">example.py</span>
            </div>
            <pre class="text-sm text-gray-300 font-mono overflow-x-auto"><code><span class="text-purple-400">import</span> numstore

<span class="text-gray-500"># Define your schema</span>
schema = numstore.Schema({
    <span class="text-green-400">"timestamp"</span>: numstore.F64,
    <span class="text-green-400">"sensors"</span>: numstore.Array(numstore.F32, [<span class="text-orange-400">1024</span>]),
    <span class="text-green-400">"label"</span>: numstore.String,
})

<span class="text-gray-500"># Create database and write data</span>
db = numstore.open(<span class="text-green-400">"readings.ns"</span>, schema)
db.write({
    <span class="text-green-400">"timestamp"</span>: <span class="text-orange-400">1706380800.0</span>,
    <span class="text-green-400">"sensors"</span>: sensor_data,
    <span class="text-green-400">"label"</span>: <span class="text-green-400">"calibration"</span>,
})

<span class="text-gray-500"># Query with zero-copy reads</span>
<span class="text-purple-400">for</span> record <span class="text-purple-400">in</span> db.query(timestamp__gt=<span class="text-orange-400">1706380000</span>):
    process(record.sensors)</code></pre>
          </div>
        </div>
      </div>
    </section>

    <!-- Use Cases Section (Expandable) -->
    <section class="py-20 bg-white">
      <div class="max-w-6xl mx-auto px-6">
        <h2 class="text-3xl font-bold text-gray-900 text-center mb-4">Built for demanding workloads</h2>
        <p class="text-lg text-gray-600 text-center mb-12 max-w-2xl mx-auto">
          From research labs to production ML pipelines, Numstore handles your most challenging data requirements.
          Click on each card to learn more.
        </p>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div
            v-for="workload in workloads"
            :key="workload.id"
            @click="toggleWorkload(workload.id)"
            class="bg-white rounded-lg border border-gray-200 hover:border-cyan-300 hover:shadow-lg transition-all cursor-pointer overflow-hidden"
            :class="{ 'ring-2 ring-cyan-400 border-cyan-400': expandedWorkload === workload.id }"
          >
            <div class="p-6">
              <div class="flex items-center justify-between mb-2">
                <div class="text-cyan-600 font-semibold">{{ workload.title }}</div>
                <svg
                  class="w-5 h-5 text-gray-400 transition-transform duration-200"
                  :class="{ 'rotate-180': expandedWorkload === workload.id }"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                </svg>
              </div>
              <p class="text-gray-600 text-sm">{{ workload.summary }}</p>
            </div>
            <transition
              enter-active-class="transition-all duration-300 ease-out"
              leave-active-class="transition-all duration-200 ease-in"
              enter-from-class="opacity-0 max-h-0"
              enter-to-class="opacity-100 max-h-96"
              leave-from-class="opacity-100 max-h-96"
              leave-to-class="opacity-0 max-h-0"
            >
              <div v-if="expandedWorkload === workload.id" class="border-t border-gray-100 bg-gray-50 overflow-hidden">
                <div class="p-6 space-y-4">
                  <p class="text-gray-700 text-sm leading-relaxed">{{ workload.details }}</p>
                  <div class="bg-cyan-50 border border-cyan-200 rounded-lg p-4">
                    <div class="flex items-start">
                      <svg class="w-5 h-5 text-cyan-600 mr-2 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                      </svg>
                      <div>
                        <div class="text-cyan-800 font-medium text-sm mb-1">Example Use Case</div>
                        <p class="text-cyan-700 text-sm">{{ workload.useCase }}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </section>

    <!-- GitHub Repos Section -->
    <section class="py-16 bg-gray-900">
      <div class="max-w-6xl mx-auto px-6">
        <div class="text-center mb-10">
          <h2 class="text-3xl font-bold text-white mb-4">Open Source</h2>
          <p class="text-gray-400 text-lg max-w-2xl mx-auto">
            Numstore is open source. Explore the code, contribute, or build your own integrations.
          </p>
        </div>
        <div class="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
          <!-- Main Numstore Repo -->
          <a
            href="https://github.com/Numstore/numstore"
            target="_blank"
            rel="noopener noreferrer"
            class="group block bg-gray-800 rounded-xl p-6 border border-gray-700 hover:border-cyan-500 hover:bg-gray-800/80 transition-all"
          >
            <div class="flex items-start justify-between mb-4">
              <div class="flex items-center">
                <svg class="w-8 h-8 text-gray-300 mr-3" fill="currentColor" viewBox="0 0 24 24">
                  <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/>
                </svg>
                <div>
                  <h3 class="text-white font-semibold text-lg group-hover:text-cyan-400 transition-colors">Numstore/numstore</h3>
                  <p class="text-gray-500 text-sm">Core database engine</p>
                </div>
              </div>
              <svg class="w-5 h-5 text-gray-500 group-hover:text-cyan-400 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
              </svg>
            </div>
            <p class="text-gray-400 text-sm mb-4">
              The core Numstore database written in pure C. High-performance numeric storage with zero dependencies.
            </p>
            <div class="flex items-center gap-4 text-sm">
              <span class="flex items-center text-gray-500">
                <span class="w-3 h-3 rounded-full bg-gray-400 mr-1.5"></span>
                C
              </span>
              <span class="flex items-center text-gray-500">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/>
                </svg>
                Star on GitHub
              </span>
            </div>
          </a>

          <!-- More Repos Coming Soon -->
          <div class="group block bg-gray-800/50 rounded-xl p-6 border border-dashed border-gray-700">
            <div class="flex items-start justify-between mb-4">
              <div class="flex items-center">
                <svg class="w-8 h-8 text-gray-500 mr-3" fill="currentColor" viewBox="0 0 24 24">
                  <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/>
                </svg>
                <div>
                  <h3 class="text-gray-400 font-semibold text-lg">More repositories</h3>
                  <p class="text-gray-600 text-sm">Coming soon</p>
                </div>
              </div>
            </div>
            <p class="text-gray-500 text-sm mb-4">
              Additional language bindings, tools, and integrations will be available here soon.
            </p>
            <div class="flex items-center gap-2 text-cyan-500 text-sm">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/>
              </svg>
              Stay tuned for updates
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-20 bg-gradient-to-r from-cyan-700 to-teal-700 text-white">
      <div class="max-w-4xl mx-auto px-6 text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-6">Ready to get started?</h2>
        <p class="text-xl text-cyan-100 mb-10">
          Join developers building the next generation of data-intensive applications.
        </p>
        <div class="flex flex-wrap justify-center gap-4">
          <RouterLink
              to="/downloads/current"
              class="inline-flex items-center px-8 py-4 bg-white text-cyan-700 font-semibold rounded-md hover:bg-cyan-50 transition-colors text-lg"
          >
            Download Numstore
          </RouterLink>
          <RouterLink
              to="/resources/blog"
              class="inline-flex items-center px-8 py-4 border-2 border-white text-white font-semibold rounded-md hover:bg-white/10 transition-colors text-lg"
          >
            Read the Blog
          </RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
pre {
  line-height: 1.6;
}
</style>
