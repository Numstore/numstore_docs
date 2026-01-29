<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'

interface FileInfo {
  name: string
  path: string
  size: number
  modified: string
}

interface Release {
  version: string
  library: FileInfo[]
  docs: FileInfo[]
  artifacts: FileInfo[]
}

interface ReleasesManifest {
  generated_at: string
  total_releases: number
  latest_version: string
  releases: Release[]
}

const loading = ref(true)
const error = ref<string | null>(null)
const currentRelease = ref<Release | null>(null)

function formatSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
}

function getFileIcon(name: string) {
  if (name.endsWith('.tar.gz') || name.endsWith('.zip')) return 'archive'
  if (name.endsWith('.pdf') || name.endsWith('.html')) return 'doc'
  return 'file'
}

onMounted(async () => {
  try {
    const response = await fetch('/releases.json')
    if (!response.ok) {
      throw new Error(`Failed to load releases: ${response.statusText}`)
    }
    const manifest: ReleasesManifest = await response.json()

    if (manifest.releases && manifest.releases.length > 0) {
      currentRelease.value = manifest.releases[0]
    } else {
      error.value = 'No releases found'
    }
  } catch (e) {
    error.value = e instanceof Error ? e.message : 'Failed to load releases'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <main class="min-h-screen bg-gray-50">
    <!-- Header -->
    <div class="bg-gradient-to-br from-cyan-600 via-cyan-700 to-teal-800 text-white py-16">
      <div class="max-w-4xl mx-auto px-6">
        <h1 class="text-4xl font-bold mb-4">Download NumStore</h1>
        <p class="text-cyan-100 text-lg max-w-2xl">
          Get the latest stable release with pre-built binaries for all major platforms.
        </p>
      </div>
    </div>

    <div class="max-w-4xl mx-auto px-6 py-12">
      <!-- Loading -->
      <div v-if="loading" class="text-center py-12">
        <div class="inline-flex items-center gap-3 text-gray-600">
          <svg class="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          Loading releases...
        </div>
      </div>

      <!-- Error -->
      <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-xl p-6 text-center">
        <svg class="w-12 h-12 text-red-400 mx-auto mb-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
        </svg>
        <p class="text-red-700">{{ error }}</p>
      </div>

      <!-- Release Content -->
      <div v-else-if="currentRelease" class="space-y-8">
        <!-- Version Badge -->
        <div class="flex items-center gap-4">
          <span class="px-4 py-2 bg-cyan-100 text-cyan-800 font-bold rounded-lg text-lg">
            v{{ currentRelease.version }}
          </span>
          <span class="text-gray-500">Current stable release</span>
        </div>

        <!-- Quick Install -->
        <section class="bg-gray-900 rounded-xl p-6">
          <h2 class="text-white font-semibold mb-3">Quick install</h2>
          <div class="font-mono text-sm text-gray-300 bg-gray-800 rounded-lg p-4 overflow-x-auto">
            <span class="text-gray-500"># Using curl</span><br>
            curl -sSL https://get.numstore.dev | sh<br><br>
            <span class="text-gray-500"># Or with pip</span><br>
            pip install numstore
          </div>
        </section>

        <!-- Library Files -->
        <section v-if="currentRelease.library.length > 0">
          <h2 class="text-xl font-bold text-gray-900 mb-4">Library</h2>
          <div class="grid gap-3">
            <a
              v-for="file in currentRelease.library"
              :key="file.path"
              :href="`/${file.path}`"
              class="flex items-center gap-4 bg-white rounded-lg border border-gray-200 p-4 hover:border-cyan-300 hover:shadow-sm transition-all group"
            >
              <div class="w-10 h-10 bg-cyan-100 rounded-lg flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"/>
                </svg>
              </div>
              <div class="flex-1 min-w-0">
                <div class="font-medium text-gray-900 group-hover:text-cyan-600 transition-colors truncate">{{ file.name }}</div>
                <div class="text-sm text-gray-500">{{ formatSize(file.size) }}</div>
              </div>
              <svg class="w-5 h-5 text-gray-400 group-hover:text-cyan-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
              </svg>
            </a>
          </div>
        </section>

        <!-- Documentation -->
        <section v-if="currentRelease.docs.length > 0">
          <h2 class="text-xl font-bold text-gray-900 mb-4">Documentation</h2>
          <div class="grid gap-3">
            <a
              v-for="file in currentRelease.docs"
              :key="file.path"
              :href="`/${file.path}`"
              target="_blank"
              class="flex items-center gap-4 bg-white rounded-lg border border-gray-200 p-4 hover:border-cyan-300 hover:shadow-sm transition-all group"
            >
              <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
              </div>
              <div class="flex-1 min-w-0">
                <div class="font-medium text-gray-900 group-hover:text-cyan-600 transition-colors truncate">{{ file.name }}</div>
                <div class="text-sm text-gray-500">{{ formatSize(file.size) }}</div>
              </div>
              <svg class="w-5 h-5 text-gray-400 group-hover:text-cyan-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
              </svg>
            </a>
          </div>
        </section>

        <!-- Additional Tools -->
        <section v-if="currentRelease.artifacts.length > 0">
          <h2 class="text-xl font-bold text-gray-900 mb-4">Additional Tools</h2>
          <div class="grid gap-3">
            <a
              v-for="file in currentRelease.artifacts"
              :key="file.path"
              :href="`/${file.path}`"
              class="flex items-center gap-4 bg-white rounded-lg border border-gray-200 p-4 hover:border-cyan-300 hover:shadow-sm transition-all group"
            >
              <div class="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center flex-shrink-0">
                <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
              </div>
              <div class="flex-1 min-w-0">
                <div class="font-medium text-gray-900 group-hover:text-cyan-600 transition-colors truncate">{{ file.name }}</div>
                <div class="text-sm text-gray-500">{{ formatSize(file.size) }}</div>
              </div>
              <svg class="w-5 h-5 text-gray-400 group-hover:text-cyan-600 transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
              </svg>
            </a>
          </div>
        </section>

        <!-- Archive Link -->
        <div class="bg-gray-100 rounded-xl p-6 flex items-center justify-between">
          <div>
            <div class="font-medium text-gray-900">Looking for older versions?</div>
            <div class="text-sm text-gray-600">Browse all previous releases in the archive.</div>
          </div>
          <RouterLink
            to="/downloads/archive"
            class="px-4 py-2 bg-white border border-gray-300 rounded-lg text-gray-700 hover:border-cyan-300 transition-colors"
          >
            View archive
          </RouterLink>
        </div>
      </div>
    </div>
  </main>
</template>
