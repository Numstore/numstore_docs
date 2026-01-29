<script lang="ts" setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'

const props = defineProps<{
  to?: string
  href?: string
  title: string
  description?: string
  icon?: string
}>()

const component = computed(() => {
  if (props.to) return RouterLink
  if (props.href) return 'a'
  return 'div'
})

const linkProps = computed(() => {
  if (props.to) return { to: props.to }
  if (props.href) return { href: props.href, target: '_blank', rel: 'noopener noreferrer' }
  return {}
})
</script>

<template>
  <component
    :is="component"
    v-bind="linkProps"
    class="group block p-6 bg-gray-50 rounded-lg border border-gray-200 hover:border-cyan-400 hover:bg-cyan-50 transition-all"
  >
    <div class="flex items-center mb-3">
      <slot name="icon">
        <div v-if="icon" class="w-6 h-6 text-cyan-600 mr-3">
          <!-- Icon slot or default -->
        </div>
      </slot>
      <h3 class="font-semibold text-gray-900 group-hover:text-cyan-700 transition-colors">{{ title }}</h3>
    </div>
    <p v-if="description" class="text-sm text-gray-600">{{ description }}</p>
    <slot></slot>
  </component>
</template>
