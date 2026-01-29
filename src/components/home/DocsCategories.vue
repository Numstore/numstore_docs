<script lang="ts" setup>
import { RouterLink } from 'vue-router'

const categories = [
  { title: 'API Reference', link: '/resources/documentation#api', description: 'Complete function reference for the C API, data types, and error handling.', icon: 'document' },
  { title: 'Network Protocol', link: '/resources/documentation#protocol', description: 'TCP/UDP wire format, connection handling, and client-server communication.', icon: 'terminal' },
  { title: 'Language Reference', link: '/resources/documentation#language', description: 'Query syntax, schema definitions, type system, and expression grammar.', icon: 'book' },
  { title: 'CLI Tool', link: '/resources/documentation#cli', description: 'Command-line interface for database management, import/export, and debugging.', icon: 'terminal' },
  { title: 'Python Usage', link: '/resources/documentation#python', description: 'Python bindings, NumPy integration, and Pythonic API patterns.', icon: 'code' },
  { title: 'Java Usage', link: '/resources/documentation#java', description: 'JNI bindings, memory management, and integration with JVM applications.', icon: 'code' },
  { title: 'Configuration', link: '/resources/documentation#config', description: 'Server settings, tuning parameters, and deployment configuration.', icon: 'cog' }
]
</script>

<template>
  <section class="py-20 bg-white border-t border-gray-100">
    <div class="max-w-6xl mx-auto px-6">
      <div class="text-center mb-12">
        <h2 class="text-3xl font-bold text-gray-900 mb-4">Documentation</h2>
        <p class="text-lg text-gray-600 max-w-2xl mx-auto">
          Everything you need to integrate Numstore into your applications.
        </p>
      </div>
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        <RouterLink
          v-for="category in categories"
          :key="category.title"
          :to="category.link"
          class="group block p-6 bg-gray-50 rounded-lg border border-gray-200 hover:border-cyan-400 hover:bg-cyan-50 transition-all"
        >
          <div class="flex items-center mb-3">
            <svg v-if="category.icon === 'document'" class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
            </svg>
            <svg v-else-if="category.icon === 'terminal'" class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            <svg v-else-if="category.icon === 'book'" class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
            </svg>
            <svg v-else-if="category.icon === 'code'" class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
            </svg>
            <svg v-else-if="category.icon === 'cog'" class="w-6 h-6 text-cyan-600 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
            <h3 class="font-semibold text-gray-900 group-hover:text-cyan-700">{{ category.title }}</h3>
          </div>
          <p class="text-sm text-gray-600">{{ category.description }}</p>
        </RouterLink>

        <!-- View All Docs -->
        <RouterLink
          to="/resources/documentation"
          class="group flex items-center justify-center p-6 bg-cyan-600 rounded-lg hover:bg-cyan-700 transition-colors"
        >
          <span class="text-white font-semibold mr-2">View All Docs</span>
          <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
          </svg>
        </RouterLink>
      </div>
    </div>
  </section>
</template>
