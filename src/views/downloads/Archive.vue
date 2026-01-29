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
const releases = ref<Release[]>([])
const expandedVersion = ref<string | null>(null)

function formatSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
}

function toggleVersion(version: string) {
  expandedVersion.value = expandedVersion.value === version ? null : version
}

onMounted(async () => {
  try {
    const response = await fetch('/releases.json')
    if (!response.ok) {
      throw new Error(`Failed to load releases: ${response.statusText}`)
    }
    const manifest: ReleasesManifest = await response.json()

    if (manifest.releases && manifest.releases.length > 0) {
      releases.value = manifest.releases
      // Expand latest by default
      if (releases.value.length > 0) {
        expandedVersion.value = releases.value[0].version
      }
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
        <h1 class="text-4xl font-bold mb-4">Release Archive</h1>
        <p class="text-cyan-100 text-lg max-w-2xl">
          All versions of NumStore, including older releases and LTS branches.
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

      <!-- Releases -->
      <div v-else-if="releases.length > 0" class="space-y-4">
        <div
          v-for="(release, index) in releases"
          :key="release.version"
          class="bg-white rounded-xl border border-gray-200 overflow-hidden"
        >
          <!-- Version Header -->
          <button
            @click="toggleVersion(release.version)"
            class="w-full px-6 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors"
          >
            <div class="flex items-center gap-3">
              <span class="text-lg font-semibold text-gray-900">v{{ release.version }}</span>
              <span
                v-if="index === 0"
                class="px-2 py-0.5 bg-green-100 text-green-700 text-xs font-medium rounded"
              >
                Latest
              </span>
            </div>
            <svg
              class="w-5 h-5 text-gray-400 transition-transform"
              :class="expandedVersion === release.version ? 'rotate-180' : ''"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
            </svg>
          </button>

          <!-- Expanded Content -->
          <div
            v-if="expandedVersion === release.version"
            class="px-6 pb-6 space-y-6 border-t border-gray-100"
          >
            <!-- Library Files -->
            <div v-if="release.library.length > 0" class="pt-4">
              <h3 class="font-medium text-gray-900 mb-3">Library</h3>
              <div class="space-y-2">
                <a
                  v-for="file in release.library"
                  :key="file.path"
                  :href="`/${file.path}`"
                  class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors group"
                >
                  <svg class="w-5 h-5 text-cyan-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"/>
                  </svg>
                  <span class="flex-1 text-gray-700 group-hover:text-cyan-600 transition-colors">{{ file.name }}</span>
                  <span class="text-sm text-gray-500">{{ formatSize(file.size) }}</span>
                </a>
              </div>
            </div>

            <!-- Documentation -->
            <div v-if="release.docs.length > 0">
              <h3 class="font-medium text-gray-900 mb-3">Documentation</h3>
              <div class="space-y-2">
                <a
                  v-for="file in release.docs"
                  :key="file.path"
                  :href="`/${file.path}`"
                  target="_blank"
                  class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors group"
                >
                  <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                  </svg>
                  <span class="flex-1 text-gray-700 group-hover:text-cyan-600 transition-colors">{{ file.name }}</span>
                  <span class="text-sm text-gray-500">{{ formatSize(file.size) }}</span>
                </a>
              </div>
            </div>

            <!-- Artifacts -->
            <div v-if="release.artifacts.length > 0">
              <h3 class="font-medium text-gray-900 mb-3">Additional Tools</h3>
              <div class="space-y-2">
                <a
                  v-for="file in release.artifacts"
                  :key="file.path"
                  :href="`/${file.path}`"
                  class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors group"
                >
                  <svg class="w-5 h-5 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
                  </svg>
                  <span class="flex-1 text-gray-700 group-hover:text-cyan-600 transition-colors">{{ file.name }}</span>
                  <span class="text-sm text-gray-500">{{ formatSize(file.size) }}</span>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Current Release Link -->
        <div class="bg-gray-100 rounded-xl p-6 flex items-center justify-between">
          <div>
            <div class="font-medium text-gray-900">Want the latest version?</div>
            <div class="text-sm text-gray-600">Go to the downloads page for quick install options.</div>
          </div>
          <RouterLink
            to="/downloads/current"
            class="px-4 py-2 bg-cyan-600 text-white rounded-lg hover:bg-cyan-700 transition-colors"
          >
            Current release
          </RouterLink>
        </div>
      </div>
    </div>
  </main>
</template>
