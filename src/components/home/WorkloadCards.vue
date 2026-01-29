<script lang="ts" setup>
import { ref } from 'vue'

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
</template>
