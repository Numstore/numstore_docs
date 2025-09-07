<script lang="ts" setup>
import {RouterView} from 'vue-router'
import NavBarEntry from "@/views/nav/NavBarEntry.vue";
import NavFooter from "@/views/nav/NavFooter.vue";
</script>

<template>
  <div class="flex flex-col min-h-screen">
    <!-- Header -->
    <header class="ml-10">

      <!-- Left Justified Logo SPACE Right Justified Links -->
      <div class="flex flex-row items-center items-end justify-start py-10">

        <!-- Logo -->
        <div class="flex flex-col">
          <h1 class="font-bold">The Database for Machine Learning</h1>

          <div class="flex flex-row align-bottom">

            <a href="/">
              <div class="flex items-center py-2" href="/">
                <img alt="Logo" class="h-12 pr-3 w-auto" src="@/assets/logo.png"/>
                <h1 class="text-4xl font-bold">Numstore</h1>
              </div>
            </a>
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

          <!-- Collapsing search bar -->
          <div class="flex flex-row-reverse items-center bg-gray-100
              text-gray-600 w-8 focus-within:w-64 overflow-hidden">

            <!-- Search Button -->
            <button class="p-2 focus:outline-none" onclick="this.nextElementSibling.focus()" type="button">
              <i class="fa-solid fa-magnifying-glass"></i>
            </button>

            <!-- Input -->
            <input class="flex-grow bg-transparent px-3 py-2 text-sm focus:outline-none"
                   placeholder="Search..."
                   type="text"
            />
          </div>
        </div>
      </div>
    </header>

    <!-- Body -->
    <div class="flex-1 m-10">
      <RouterView/>
    </div>

    <!-- Footer -->
    <NavFooter/>

    <!-- Footer -->
    <div class="bg-green-300 text-center text-sm">
      Copyright © 2001-2025, Lincke Solutions LLC.
    </div>
  </div>
</template>

<style scoped>
</style>
