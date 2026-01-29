<script lang="ts" setup>
import { RouterLink } from 'vue-router'
</script>

<template>
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
</template>
