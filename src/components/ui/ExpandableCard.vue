<script lang="ts" setup>
import { ref } from 'vue'

const props = defineProps<{
  title: string
  summary?: string
  expanded?: boolean
}>()

const emit = defineEmits<{
  toggle: [expanded: boolean]
}>()

const isExpanded = ref(props.expanded ?? false)

function toggle() {
  isExpanded.value = !isExpanded.value
  emit('toggle', isExpanded.value)
}
</script>

<template>
  <div
    class="bg-white rounded-xl border border-gray-200 overflow-hidden transition-all"
    :class="{ 'ring-2 ring-cyan-400 border-cyan-400': isExpanded }"
  >
    <button
      @click="toggle"
      class="w-full px-6 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors text-left"
    >
      <div class="flex-1">
        <div class="font-semibold text-gray-900">{{ title }}</div>
        <p v-if="summary" class="text-gray-600 text-sm mt-1">{{ summary }}</p>
      </div>
      <svg
        class="w-5 h-5 text-gray-400 transition-transform duration-200 flex-shrink-0 ml-4"
        :class="{ 'rotate-180': isExpanded }"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
      </svg>
    </button>

    <transition
      enter-active-class="transition-all duration-300 ease-out"
      leave-active-class="transition-all duration-200 ease-in"
      enter-from-class="opacity-0 max-h-0"
      enter-to-class="opacity-100 max-h-screen"
      leave-from-class="opacity-100 max-h-screen"
      leave-to-class="opacity-0 max-h-0"
    >
      <div v-if="isExpanded" class="border-t border-gray-100 bg-gray-50 overflow-hidden">
        <div class="p-6">
          <slot></slot>
        </div>
      </div>
    </transition>
  </div>
</template>
