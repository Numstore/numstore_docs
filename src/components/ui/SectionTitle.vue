<script lang="ts" setup>
defineProps<{
  title: string
  subtitle?: string
  centered?: boolean
}>()
</script>

<template>
  <div :class="centered ? 'text-center' : ''" class="mb-12">
    <h2 class="text-3xl font-bold text-gray-900 mb-4">
      <slot name="title">{{ title }}</slot>
    </h2>
    <p v-if="subtitle || $slots.subtitle" class="text-lg text-gray-600 max-w-2xl" :class="centered ? 'mx-auto' : ''">
      <slot name="subtitle">{{ subtitle }}</slot>
    </p>
    <slot></slot>
  </div>
</template>
