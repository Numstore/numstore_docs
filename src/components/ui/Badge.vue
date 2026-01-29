<script lang="ts" setup>
defineProps<{
  variant?: 'default' | 'success' | 'warning' | 'error' | 'info' | 'cyan'
  size?: 'sm' | 'md'
}>()
</script>

<template>
  <span
    class="inline-flex items-center font-medium rounded"
    :class="[
      {
        'px-1.5 py-0.5 text-xs': size === 'sm' || !size,
        'px-2.5 py-1 text-sm': size === 'md'
      },
      {
        'bg-gray-100 text-gray-700': variant === 'default' || !variant,
        'bg-green-100 text-green-700': variant === 'success',
        'bg-yellow-100 text-yellow-700': variant === 'warning',
        'bg-red-100 text-red-700': variant === 'error',
        'bg-blue-100 text-blue-700': variant === 'info',
        'bg-cyan-100 text-cyan-700': variant === 'cyan'
      }
    ]"
  >
    <slot></slot>
  </span>
</template>
