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
        <h2 class="text-xl font-bold text-gray-800 mb-4">Why Numstore?</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-sm">
          <div class="flex flex-col">
            <div class="font-semibold text-blue-700 mb-2">Pure C, Zero Dependencies</div>
            <p class="text-gray-700">Embedded database written in 100% dependency-free C. Integrate into any language—Python, Java, Go, Rust, or your custom stack.</p>
          </div>
          <div class="flex flex-col">
            <div class="font-semibold text-blue-700 mb-2">Early Adoption Advantage</div>
            <p class="text-gray-700">Join now during early development. Influence feature roadmap, get direct access to the maintainer, and shape the future of numeric data storage.</p>
          </div>
          <div class="flex flex-col">
            <div class="font-semibold text-blue-700 mb-2">Extreme Performance</div>
            <p class="text-gray-700">Optimized for time-series and numeric workloads. <strong>10-100x faster</strong> than traditional oscilloscope data readers and general-purpose databases for numeric operations.</p>
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
