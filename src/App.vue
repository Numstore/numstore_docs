<script lang="ts" setup>
import {RouterView} from 'vue-router'
import NavBarEntry from "@/views/nav/NavBarEntry.vue";
import NavFooter from "@/views/nav/NavFooter.vue";
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <!-- Header -->
    <header>

      <!-- Left Justified Logo SPACE Right Justified Links -->
      <div class="flex flex-row items-center items-end justify-start py-10">

        <!-- Logo -->
        <div class="flex flex-col ml-5">
          <h1 class="font-bold text-lg">The Database for Machine Learning</h1>

          <div class="flex flex-row align-bottom">
            <RouterLink to="/">
              <div class="flex items-center py-2" href="/">
                <img alt="Logo" class="h-12 pr-3 w-auto" src="@/assets/logo.png"/>
                <h1 class="text-4xl font-bold">Numstore</h1>
              </div>
            </RouterLink>
          </div>

          <!-- Academic & Research Focus -->
          <div class="mt-2 text-sm text-gray-700 max-w-2xl">
            <p class="font-semibold text-blue-700">A database for numeric time-series data</p>
            <p class="text-xs mt-1">Academic licenses available • Discounted pricing for research institutions</p>
          </div>
        </div>

        <!-- Nav -->
        <div class="flex text-sm font-medium items-center flex-1 justify-between bg-blue-200">

          <nav class="flex">

            <NavBarEntry
                :items="[
                    { text: 'Current', href: '/downloads/current' },
                    { text: 'Archive', href: '/downloads/archive' },
                    ]"
                label="Downloads"
            />

            <NavBarEntry
                :items="[
                    { text: 'Documentation', href: '/resources/documentation' },
                    { text: 'Blog', href: '/resources/blog' },
                    { text: 'References', href: '/resources/references' },
                    ]"
                label="Resources"
            />

            <NavBarEntry
                :items="[
                    { text: 'Enterprise Support', href: '/services/enterprise_support' },
                    { text: 'Consulting', href: '/services/consulting' },
                    { text: 'Training', href: '/services/training' },
                    ]"
                label="Services"
            />

            <NavBarEntry
                :items="[
                    { text: 'Bug Reporting', href: '/community/bug_reporting' },
                    { text: 'Forum', href: '/community/forum' },
                    ]"
                label="Community"
            />

            <NavBarEntry
                :items="[
                    { text: 'Company', href: '/about/company' },
                    { text: 'Contact', href: '/about/contact' },
                    ]"
                label="About"
            />
          </nav>
        </div>
      </div>
    </header>

    <!-- Key Features Banner -->
    <div class="bg-gradient-to-r from-blue-50 to-indigo-50 border-y border-blue-200 py-6 px-10">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-xl font-bold text-gray-800 mb-4">Features</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
          <div class="flex flex-col">
            <div class="font-semibold text-blue-700 mb-2">Dependency-Free C Implementation</div>
            <p class="text-gray-700">Written in standard C with no external dependencies. Provides bindings for Python, Java, and other languages through a stable C API.</p>
          </div>
          <div class="flex flex-col">
            <div class="font-semibold text-blue-700 mb-2">Contiguous Storage Model</div>
            <p class="text-gray-700">Stores numeric arrays in contiguous memory blocks, enabling zero-copy reads and efficient cache utilization for sequential access patterns.</p>
          </div>
          <div class="flex flex-col">
            <div class="font-semibold text-blue-700 mb-2">R+ Tree Indexing</div>
            <p class="text-gray-700">Implements R+ tree spatial indexing for O(log n) range queries on time-series data. Optimized for high-throughput numeric workloads.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Body -->
    <div class="flex-1 m-10">
      <RouterView/>
    </div>

    <!-- Footer -->
    <NavFooter/>
  </div>
</template>

<style scoped>
</style>
