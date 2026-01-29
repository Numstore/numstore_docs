<script lang="ts" setup>
import {ref} from 'vue'

const issueTemplate = `### Summary
A brief, one-sentence summary of the bug.

### Environment
- NumStore version: v1.0.0
- OS: (Ubuntu 22.04, macOS 14, Windows 11)
- CPU: (x86_64, arm64)
- Bindings: (CLI / Python / Java) + version

### Steps to Reproduce
1.
2.
3.

### Expected vs Actual
Expected:
Actual:

### Logs / Output
<paste exact output here>
`

const copied = ref(false)

function copyTemplate() {
  navigator.clipboard?.writeText(issueTemplate).then(() => {
    copied.value = true
    setTimeout(() => copied.value = false, 2000)
  })
}

const severities = [
  { level: "P1", name: "Critical", desc: "Production down, data loss risk, security exposure", color: "red" },
  { level: "P2", name: "High", desc: "Major feature broken, severe performance degradation", color: "yellow" },
  { level: "P3", name: "Normal", desc: "Functional bug, not blocking production", color: "blue" },
  { level: "P4", name: "Low", desc: "Cosmetic, typos, minor docs issues", color: "gray" }
]
</script>

<template>
  <main class="min-h-screen bg-gray-50">
    <!-- Header -->
    <div class="bg-gradient-to-br from-cyan-600 via-cyan-700 to-teal-800 text-white py-16">
      <div class="max-w-4xl mx-auto px-6">
        <h1 class="text-4xl font-bold mb-4">Bug Reporting</h1>
        <p class="text-cyan-100 text-lg max-w-2xl">
          Help improve NumStore by reporting bugs with enough detail to reproduce quickly.
        </p>
      </div>
    </div>

    <div class="max-w-4xl mx-auto px-6 py-12 space-y-10">
      <!-- Where to file -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-4">Where to file</h2>
        <div class="grid md:grid-cols-3 gap-4">
          <a
            href="https://github.com/Numstore/numstore/issues"
            target="_blank"
            rel="noopener"
            class="bg-white rounded-lg border border-gray-200 p-5 hover:border-cyan-300 hover:shadow-sm transition-all group"
          >
            <div class="flex items-center gap-3 mb-2">
              <svg class="w-6 h-6 text-gray-700" fill="currentColor" viewBox="0 0 24 24">
                <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/>
              </svg>
              <span class="font-semibold text-gray-900 group-hover:text-cyan-700">GitHub Issues</span>
            </div>
            <p class="text-sm text-gray-600">Public issue tracker</p>
          </a>

          <a
            href="mailto:bugs@numstore.dev"
            class="bg-white rounded-lg border border-gray-200 p-5 hover:border-cyan-300 hover:shadow-sm transition-all group"
          >
            <div class="flex items-center gap-3 mb-2">
              <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
              </svg>
              <span class="font-semibold text-gray-900 group-hover:text-cyan-700">Email</span>
            </div>
            <p class="text-sm text-gray-600">bugs@numstore.dev</p>
          </a>

          <a
            href="mailto:security@numstore.dev"
            class="bg-white rounded-lg border border-gray-200 p-5 hover:border-red-300 hover:shadow-sm transition-all group"
          >
            <div class="flex items-center gap-3 mb-2">
              <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
              </svg>
              <span class="font-semibold text-gray-900 group-hover:text-red-700">Security</span>
            </div>
            <p class="text-sm text-gray-600">Private disclosure</p>
          </a>
        </div>
      </section>

      <!-- Severity -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-4">Severity levels</h2>
        <div class="grid md:grid-cols-2 gap-3">
          <div v-for="s in severities" :key="s.level" class="bg-white rounded-lg border border-gray-200 p-4 flex items-start gap-3">
            <span
              class="px-2 py-1 text-xs font-bold rounded flex-shrink-0"
              :class="{
                'bg-red-100 text-red-700': s.color === 'red',
                'bg-yellow-100 text-yellow-700': s.color === 'yellow',
                'bg-blue-100 text-blue-700': s.color === 'blue',
                'bg-gray-100 text-gray-700': s.color === 'gray'
              }"
            >{{ s.level }}</span>
            <div>
              <div class="font-medium text-gray-900">{{ s.name }}</div>
              <div class="text-sm text-gray-600">{{ s.desc }}</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Template -->
      <section>
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-2xl font-bold text-gray-900">Issue template</h2>
          <button
            @click="copyTemplate"
            class="inline-flex items-center gap-2 px-4 py-2 bg-cyan-600 text-white text-sm font-medium rounded-lg hover:bg-cyan-700 transition-colors"
          >
            <svg v-if="!copied" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/>
            </svg>
            <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
            </svg>
            {{ copied ? 'Copied!' : 'Copy template' }}
          </button>
        </div>
        <pre class="bg-gray-900 text-gray-300 p-6 rounded-lg text-sm overflow-x-auto">{{ issueTemplate }}</pre>
      </section>

      <!-- Privacy note -->
      <section class="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
        <div class="flex items-start gap-3">
          <svg class="w-5 h-5 text-yellow-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
          </svg>
          <div>
            <div class="font-medium text-yellow-800">Privacy reminder</div>
            <p class="text-sm text-yellow-700">Redact secrets, API keys, and PII before posting. For private data, email directly and mark as confidential.</p>
          </div>
        </div>
      </section>
    </div>
  </main>
</template>
