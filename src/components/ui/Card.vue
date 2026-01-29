<script lang="ts" setup>
defineProps<{
  hoverable?: boolean
  padding?: 'none' | 'sm' | 'md' | 'lg'
  variant?: 'default' | 'outlined' | 'filled'
}>()
</script>

<template>
  <div
    class="bg-white rounded-xl border transition-all"
    :class="[
      hoverable ? 'hover:shadow-lg hover:border-cyan-300 cursor-pointer' : '',
      {
        'p-0': padding === 'none',
        'p-4': padding === 'sm',
        'p-6': padding === 'md' || !padding,
        'p-8': padding === 'lg'
      },
      {
        'border-gray-200': variant === 'default' || !variant,
        'border-gray-300': variant === 'outlined',
        'border-gray-100 bg-gray-50': variant === 'filled'
      }
    ]"
  >
    <slot></slot>
  </div>
</template>
