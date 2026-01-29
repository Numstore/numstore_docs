<script lang="ts" setup>
defineProps<{
  videoId?: string
}>()
</script>

<template>
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
            :src="`https://www.youtube.com/embed/${videoId || 'dQw4w9WgXcQ'}`"
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
</template>
