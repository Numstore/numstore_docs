<script lang="ts" setup>
import {RouterView, RouterLink} from 'vue-router'
import NavBarEntry from "@/views/nav/NavBarEntry.vue";
import NavFooter from "@/views/nav/NavFooter.vue";
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <!-- Header -->
    <header class="bg-white border-b border-gray-200 sticky top-0 z-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6">
        <div class="flex items-center justify-between h-16">
          <!-- Logo -->
          <RouterLink to="/" class="flex items-center gap-3 hover:opacity-80 transition-opacity">
            <img alt="Numstore Logo" class="h-8 w-auto" src="@/assets/logo.png"/>
            <span class="text-xl font-bold text-gray-900">Numstore</span>
          </RouterLink>

          <!-- Navigation -->
          <nav class="hidden md:flex items-center">
            <NavBarEntry
                :items="[
                  { text: 'Current Release', href: '/downloads/current' },
                  { text: 'Archive', href: '/downloads/archive' },
                ]"
                label="Downloads"
                bgClass="bg-white shadow-lg border border-gray-200"
                groupHoverClass="hover:text-cyan-600"
                itemHoverClass="hover:bg-cyan-50 hover:text-cyan-700"
            />

            <NavBarEntry
                :items="[
                  { text: 'Documentation', href: '/resources/documentation' },
                  { text: 'Blog', href: '/resources/blog' },
                  { text: 'References', href: '/resources/references' },
                ]"
                label="Learn"
                bgClass="bg-white shadow-lg border border-gray-200"
                groupHoverClass="hover:text-cyan-600"
                itemHoverClass="hover:bg-cyan-50 hover:text-cyan-700"
            />

            <NavBarEntry
                :items="[
                  { text: 'Enterprise Support', href: '/services/enterprise_support' },
                  { text: 'Consulting', href: '/services/consulting' },
                  { text: 'Training', href: '/services/training' },
                ]"
                label="Services"
                bgClass="bg-white shadow-lg border border-gray-200"
                groupHoverClass="hover:text-cyan-600"
                itemHoverClass="hover:bg-cyan-50 hover:text-cyan-700"
            />

            <NavBarEntry
                :items="[
                  { text: 'Bug Reporting', href: '/community/bug_reporting' },
                  { text: 'Forum', href: '/community/forum' },
                ]"
                label="Community"
                bgClass="bg-white shadow-lg border border-gray-200"
                groupHoverClass="hover:text-cyan-600"
                itemHoverClass="hover:bg-cyan-50 hover:text-cyan-700"
            />

            <NavBarEntry
                :items="[
                  { text: 'Company', href: '/about/company' },
                  { text: 'Contact', href: '/about/contact' },
                ]"
                label="About"
                bgClass="bg-white shadow-lg border border-gray-200"
                groupHoverClass="hover:text-cyan-600"
                itemHoverClass="hover:bg-cyan-50 hover:text-cyan-700"
            />
          </nav>

          <!-- CTA Button -->
          <div class="hidden md:block">
            <RouterLink
                to="/downloads/current"
                class="inline-flex items-center px-4 py-2 bg-cyan-600 text-white text-sm font-medium rounded-md hover:bg-cyan-700 transition-colors"
            >
              Download
            </RouterLink>
          </div>

          <!-- Mobile menu button -->
          <button class="md:hidden p-2 text-gray-600 hover:text-gray-900">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            </svg>
          </button>
        </div>
      </div>
    </header>

    <!-- Body -->
    <main class="flex-1">
      <RouterView/>
    </main>

    <!-- Footer -->
    <NavFooter/>
  </div>
</template>

<style scoped>
</style>
