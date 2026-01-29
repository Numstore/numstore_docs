<template>
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
</template>

<style scoped>
pre {
  line-height: 1.6;
}
</style>
