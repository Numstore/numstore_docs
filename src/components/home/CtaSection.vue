<script lang="ts" setup>
import { RouterLink } from 'vue-router'
</script>

<template>
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
</template>
