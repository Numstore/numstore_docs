<script lang="ts" setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'

const props = defineProps<{
  to?: string
  href?: string
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost'
  size?: 'sm' | 'md' | 'lg'
  disabled?: boolean
}>()

const classes = computed(() => [
  'inline-flex items-center justify-center font-semibold rounded-md transition-colors',
  {
    // Size
    'px-4 py-2 text-sm': props.size === 'sm',
    'px-6 py-3 text-base': props.size === 'md' || !props.size,
    'px-8 py-4 text-lg': props.size === 'lg',
    // Variants
    'bg-cyan-600 text-white hover:bg-cyan-700': props.variant === 'primary' || !props.variant,
    'bg-white text-cyan-700 hover:bg-cyan-50': props.variant === 'secondary',
    'border-2 border-current text-cyan-600 hover:bg-cyan-50': props.variant === 'outline',
    'text-cyan-600 hover:bg-cyan-50': props.variant === 'ghost',
    // Disabled
    'opacity-50 cursor-not-allowed': props.disabled
  }
])

const component = computed(() => {
  if (props.to) return RouterLink
  if (props.href) return 'a'
  return 'button'
})

const linkProps = computed(() => {
  if (props.to) return { to: props.to }
  if (props.href) return { href: props.href, target: '_blank', rel: 'noopener noreferrer' }
  return {}
})
</script>

<template>
  <component :is="component" v-bind="linkProps" :class="classes" :disabled="disabled">
    <slot></slot>
  </component>
</template>
