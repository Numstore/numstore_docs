<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { GradientHeader, LoadingSpinner, Badge, Button, Icon, Card, Callout } from '@/components/ui'

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
    <GradientHeader
      title="Release Archive"
      subtitle="All versions of NumStore, including older releases and LTS branches."
    />

    <div class="max-w-4xl mx-auto px-6 py-12">
      <!-- Loading -->
      <div v-if="loading" class="text-center py-12">
        <LoadingSpinner text="Loading releases..." />
      </div>

      <!-- Error -->
      <Callout v-else-if="error" variant="error">
        {{ error }}
      </Callout>

      <!-- Releases -->
      <div v-else-if="releases.length > 0" class="space-y-4">
        <Card
          v-for="(release, index) in releases"
          :key="release.version"
          padding="none"
          class="overflow-hidden"
        >
          <!-- Version Header -->
          <button
            @click="toggleVersion(release.version)"
            class="w-full px-6 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors"
          >
            <div class="flex items-center gap-3">
              <span class="text-lg font-semibold text-gray-900">v{{ release.version }}</span>
              <Badge v-if="index === 0" variant="success">Latest</Badge>
            </div>
            <Icon
              name="chevron-down"
              class="text-gray-400 transition-transform"
              :class="expandedVersion === release.version ? 'rotate-180' : ''"
            />
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
                  <Icon name="download" class="text-cyan-600" />
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
                  <Icon name="document" class="text-blue-600" />
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
                  <Icon name="cog" class="text-gray-600" />
                  <span class="flex-1 text-gray-700 group-hover:text-cyan-600 transition-colors">{{ file.name }}</span>
                  <span class="text-sm text-gray-500">{{ formatSize(file.size) }}</span>
                </a>
              </div>
            </div>
          </div>
        </Card>

        <!-- Current Release Link -->
        <Card variant="filled" class="flex items-center justify-between">
          <div>
            <div class="font-medium text-gray-900">Want the latest version?</div>
            <div class="text-sm text-gray-600">Go to the downloads page for quick install options.</div>
          </div>
          <Button to="/downloads/current">Current release</Button>
        </Card>
      </div>
    </div>
  </main>
</template>
