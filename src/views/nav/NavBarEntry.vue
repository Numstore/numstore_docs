<template>
  <!-- Hoverable group wrapper -->
  <div :class="['relative group', groupHoverClass]">

    <!-- Button -->
    <button class="flex items-center px-3 py-2">
      {{ label }}
      <i class="fa-solid fa-caret-down ml-2 text-sm"></i>
    </button>

    <!-- Dropdown -->
    <div
        :class="[
        'absolute left-0 w-40 ',
        'group-hover:opacity-100 invisible group-hover:visible',
        bgClass
      ]"
    >
      <a
          v-for="(item, i) in items"
          :key="i"
          :class="['block px-4 py-2', itemHoverClass]"
          :href="item.href"
      >
        {{ item.text }}
      </a>
    </div>
  </div>
</template>

<script lang="ts" setup>
interface DropdownItem {
  text: string
  href: string
}

/* ---------- props ---------- */
const props = withDefaults(
    defineProps<{
      label: string
      items: DropdownItem[]
      bgClass?: string
      groupHoverClass?: string
      itemHoverClass?: string
    }>(),
    {
      bgClass: 'bg-blue-700',
      groupHoverClass: 'hover:bg-blue-500',
      itemHoverClass: 'hover:bg-blue-800'
    }
)

const {label, items, bgClass, groupHoverClass, itemHoverClass} = props
</script>
