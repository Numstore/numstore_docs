<template>
  <div class="relative group">
    <!-- Button -->
    <button :class="['flex items-center px-4 py-2 text-sm font-medium text-gray-700 transition-colors', groupHoverClass]">
      {{ label }}
      <svg class="ml-1 w-4 h-4 text-gray-400 group-hover:text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
      </svg>
    </button>

    <!-- Dropdown -->
    <div
        :class="[
        'absolute left-0 mt-1 w-48 rounded-md py-1 z-50',
        'opacity-0 invisible group-hover:opacity-100 group-hover:visible',
        'transition-all duration-150 ease-out',
        bgClass
      ]"
    >
      <RouterLink
          v-for="(item, i) in items"
          :key="i"
          :class="['block px-4 py-2 text-sm text-gray-700 transition-colors', itemHoverClass]"
          :to="item.href"
      >
        {{ item.text }}
      </RouterLink>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {RouterLink} from "vue-router";

interface DropdownItem {
  text: string
  href: string
}

withDefaults(
    defineProps<{
      label: string
      items: DropdownItem[]
      bgClass?: string
      groupHoverClass?: string
      itemHoverClass?: string
    }>(),
    {
      bgClass: 'bg-white shadow-lg border border-gray-200',
      groupHoverClass: 'hover:text-cyan-600',
      itemHoverClass: 'hover:bg-cyan-50 hover:text-cyan-700'
    }
)
</script>
