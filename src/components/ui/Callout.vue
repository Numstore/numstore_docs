<script lang="ts" setup>
import Icon from './Icon.vue'

defineProps<{
  variant?: 'info' | 'warning' | 'error' | 'success' | 'tip'
  title?: string
}>()
</script>

<template>
  <div
    class="rounded-lg p-4 border"
    :class="{
      'bg-blue-50 border-blue-200': variant === 'info' || !variant,
      'bg-yellow-50 border-yellow-200': variant === 'warning',
      'bg-red-50 border-red-200': variant === 'error',
      'bg-green-50 border-green-200': variant === 'success',
      'bg-cyan-50 border-cyan-200': variant === 'tip'
    }"
  >
    <div class="flex items-start">
      <Icon
        :name="variant === 'warning' ? 'warning' : variant === 'error' ? 'error' : 'info'"
        class="flex-shrink-0 mt-0.5 mr-3"
        :class="{
          'text-blue-600': variant === 'info' || !variant,
          'text-yellow-600': variant === 'warning',
          'text-red-600': variant === 'error',
          'text-green-600': variant === 'success',
          'text-cyan-600': variant === 'tip'
        }"
      />
      <div class="flex-1">
        <div
          v-if="title"
          class="font-medium text-sm mb-1"
          :class="{
            'text-blue-800': variant === 'info' || !variant,
            'text-yellow-800': variant === 'warning',
            'text-red-800': variant === 'error',
            'text-green-800': variant === 'success',
            'text-cyan-800': variant === 'tip'
          }"
        >
          {{ title }}
        </div>
        <div
          class="text-sm"
          :class="{
            'text-blue-700': variant === 'info' || !variant,
            'text-yellow-700': variant === 'warning',
            'text-red-700': variant === 'error',
            'text-green-700': variant === 'success',
            'text-cyan-700': variant === 'tip'
          }"
        >
          <slot></slot>
        </div>
      </div>
    </div>
  </div>
</template>
