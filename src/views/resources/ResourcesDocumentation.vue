<script lang="ts" setup>
import ROOT from "./autogen/ROOT.vue";
</script>

<template>
  <div class="w-[64rem] mx-auto gap-8">
    <ROOT/>
  </div>
</template>

<style scoped>
@reference "tailwindcss";
h1 {
  @apply text-4xl font-bold leading-tight;
}

h2 {
  @apply text-3xl font-bold leading-tight;
}

h3 {
  @apply text-2xl font-bold leading-tight;
}

h4 {
  @apply text-xl  font-bold leading-tight;
}

</style>
