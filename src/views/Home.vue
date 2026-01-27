<script lang="ts" setup>
import {RouterLink} from 'vue-router'
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

    <!-- Features Grid -->
    <section class="py-20 bg-gray-50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="grid md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="bg-white rounded-lg p-8 shadow-sm border border-gray-100">
            <div class="w-12 h-12 bg-cyan-100 rounded-lg flex items-center justify-center mb-5">
              <svg class="w-6 h-6 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-3">Extreme Performance</h3>
            <p class="text-gray-600 leading-relaxed">
              10-100x faster than traditional databases for numeric workloads. Optimized for time-series, tensors, and scientific data.
            </p>
          </div>

          <!-- Feature 2 -->
          <div class="bg-white rounded-lg p-8 shadow-sm border border-gray-100">
            <div class="w-12 h-12 bg-teal-100 rounded-lg flex items-center justify-center mb-5">
              <svg class="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-3">Pure C, Zero Dependencies</h3>
            <p class="text-gray-600 leading-relaxed">
              Written in 100% dependency-free C. Embed into any language—Python, Java, Go, Rust, or your custom stack.
            </p>
          </div>

          <!-- Feature 3 -->
          <div class="bg-white rounded-lg p-8 shadow-sm border border-gray-100">
            <div class="w-12 h-12 bg-emerald-100 rounded-lg flex items-center justify-center mb-5">
              <svg class="w-6 h-6 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-3">Type Safe</h3>
            <p class="text-gray-600 leading-relaxed">
              Define schemas with structs, unions, and enums. Catch data errors at write time, not when your model crashes.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Code Example Section -->
    <section class="py-20 bg-white">
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

    <!-- Use Cases Section -->
    <section class="py-20 bg-gray-50">
      <div class="max-w-6xl mx-auto px-6">
        <h2 class="text-3xl font-bold text-gray-900 text-center mb-4">Built for demanding workloads</h2>
        <p class="text-lg text-gray-600 text-center mb-12 max-w-2xl mx-auto">
          From research labs to production ML pipelines, Numstore handles your most challenging data requirements.
        </p>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="bg-white rounded-lg p-6 border border-gray-200 hover:border-cyan-300 hover:shadow-md transition-all">
            <div class="text-cyan-600 font-semibold mb-2">Machine Learning</div>
            <p class="text-gray-600 text-sm">Training data, feature stores, model checkpoints</p>
          </div>
          <div class="bg-white rounded-lg p-6 border border-gray-200 hover:border-cyan-300 hover:shadow-md transition-all">
            <div class="text-cyan-600 font-semibold mb-2">Scientific Computing</div>
            <p class="text-gray-600 text-sm">Simulation results, experimental data, sensor arrays</p>
          </div>
          <div class="bg-white rounded-lg p-6 border border-gray-200 hover:border-cyan-300 hover:shadow-md transition-all">
            <div class="text-cyan-600 font-semibold mb-2">Time Series</div>
            <p class="text-gray-600 text-sm">IoT telemetry, financial data, monitoring metrics</p>
          </div>
          <div class="bg-white rounded-lg p-6 border border-gray-200 hover:border-cyan-300 hover:shadow-md transition-all">
            <div class="text-cyan-600 font-semibold mb-2">Embedded Systems</div>
            <p class="text-gray-600 text-sm">Edge devices, robotics, automotive applications</p>
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
