<script lang="ts" setup>
defineProps<{
  title: string
  subtitle?: string
  size?: 'sm' | 'md' | 'lg'
}>()
</script>

<template>
  <div class="bg-gradient-to-br from-cyan-600 via-cyan-700 to-teal-800 text-white" :class="{
    'py-12': size === 'sm',
    'py-16': size === 'md' || !size,
    'py-24 md:py-32': size === 'lg'
  }">
    <div class="max-w-4xl mx-auto px-6">
      <h1 class="font-bold mb-4" :class="{
        'text-2xl md:text-3xl': size === 'sm',
        'text-3xl md:text-4xl': size === 'md' || !size,
        'text-4xl md:text-5xl lg:text-6xl': size === 'lg'
      }">
        <slot name="title">{{ title }}</slot>
      </h1>
      <p v-if="subtitle || $slots.subtitle" class="text-cyan-100 max-w-2xl" :class="{
        'text-base': size === 'sm',
        'text-lg': size === 'md' || !size,
        'text-xl md:text-2xl': size === 'lg'
      }">
        <slot name="subtitle">{{ subtitle }}</slot>
      </p>
      <slot></slot>
    </div>
  </div>
</template>
