<script lang="ts" setup>
defineProps<{
  items: string[]
  iconColor?: string
}>()
</script>

<template>
  <ul class="space-y-4">
    <li v-for="item in items" :key="item" class="flex items-start">
      <svg
        class="w-6 h-6 mr-3 flex-shrink-0"
        :class="iconColor || 'text-cyan-600'"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
      </svg>
      <span class="text-gray-700">{{ item }}</span>
    </li>
  </ul>
</template>
