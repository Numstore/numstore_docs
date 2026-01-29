<script lang="ts" setup>
import {computed, ref} from 'vue'
import {RouterLink} from 'vue-router'

type Category = { id: string; name: string; desc: string; icon: string }
type Thread = {
  id: string
  title: string
  category: string
  author: string
  replies: number
  lastActivity: string
  url?: string
}

const categories: Category[] = [
  {id: 'announcements', name: 'Announcements', desc: 'Releases and important updates.', icon: 'megaphone'},
  {id: 'help', name: 'Help', desc: 'Ask questions and get support.', icon: 'question'},
  {id: 'howto', name: 'How-To', desc: 'Tips, scripts, and best practices.', icon: 'lightbulb'},
  {id: 'feedback', name: 'Feedback', desc: 'Feature requests and product feedback.', icon: 'chat'},
]

const threads = ref<Thread[]>([
  {
    id: 't1',
    title: 'NumStore v1.0.0 Released',
    category: 'announcements',
    author: 'team',
    replies: 12,
    lastActivity: '2025-09-05',
    url: '/resources/blog/2025-09-05_release-1-0-0'
  },
  {
    id: 't2',
    title: 'WAL tuning for high-ingest workloads',
    category: 'howto',
    author: 'alex',
    replies: 7,
    lastActivity: '2025-09-03'
  },
  {
    id: 't3',
    title: 'Install fails on Ubuntu 22.04',
    category: 'help',
    author: 'sam',
    replies: 4,
    lastActivity: '2025-09-02'
  },
  {
    id: 't4',
    title: 'Request: read-only role with snapshot export',
    category: 'feedback',
    author: 'jordan',
    replies: 3,
    lastActivity: '2025-08-28'
  },
])

const q = ref('')
const cat = ref<string | 'all'>('all')

const filtered = computed(() => {
  const query = q.value.trim().toLowerCase()
  return threads.value
      .filter(t => (cat.value === 'all' ? true : t.category === cat.value))
      .filter(t => {
        if (!query) return true
        return (
            t.title.toLowerCase().includes(query) ||
            t.author.toLowerCase().includes(query)
        )
      })
      .sort((a, b) => (a.lastActivity < b.lastActivity ? 1 : -1))
})

const newTopic = ref({
  title: '',
  category: 'help' as string,
  body: ''
})

function submitTopic() {
  if (!newTopic.value.title.trim()) return
  const id = 't' + (threads.value.length + 1)
  threads.value.unshift({
    id,
    title: newTopic.value.title.trim(),
    category: newTopic.value.category,
    author: 'you',
    replies: 0,
    lastActivity: new Date().toISOString().slice(0, 10),
  })
  newTopic.value = {title: '', category: 'help', body: ''}
}

function getCategoryColor(id: string) {
  const colors: Record<string, string> = {
    announcements: 'bg-purple-100 text-purple-700',
    help: 'bg-blue-100 text-blue-700',
    howto: 'bg-green-100 text-green-700',
    feedback: 'bg-orange-100 text-orange-700'
  }
  return colors[id] || 'bg-gray-100 text-gray-700'
}
</script>

<template>
  <main class="min-h-screen bg-gray-50">
    <!-- Header -->
    <div class="bg-gradient-to-br from-cyan-600 via-cyan-700 to-teal-800 text-white py-16">
      <div class="max-w-5xl mx-auto px-6">
        <h1 class="text-4xl font-bold mb-4">Community Forum</h1>
        <p class="text-cyan-100 text-lg max-w-2xl">
          Ask questions, share tips, and discuss NumStore with the community.
        </p>
      </div>
    </div>

    <div class="max-w-5xl mx-auto px-6 py-12 space-y-10">
      <!-- Categories -->
      <section>
        <h2 class="text-2xl font-bold text-gray-900 mb-4">Categories</h2>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <button
            v-for="c in categories"
            :key="c.id"
            @click="cat = c.id"
            class="bg-white rounded-lg border border-gray-200 p-5 text-left hover:border-cyan-300 hover:shadow-sm transition-all"
            :class="cat === c.id ? 'border-cyan-400 ring-2 ring-cyan-100' : ''"
          >
            <div class="w-10 h-10 rounded-lg flex items-center justify-center mb-3" :class="getCategoryColor(c.id)">
              <svg v-if="c.icon === 'megaphone'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z"/>
              </svg>
              <svg v-else-if="c.icon === 'question'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
              <svg v-else-if="c.icon === 'lightbulb'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/>
              </svg>
              <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
              </svg>
            </div>
            <div class="font-semibold text-gray-900">{{ c.name }}</div>
            <div class="text-sm text-gray-600 mt-1">{{ c.desc }}</div>
          </button>
        </div>
        <button
          v-if="cat !== 'all'"
          @click="cat = 'all'"
          class="mt-3 text-sm text-cyan-600 hover:text-cyan-700"
        >
          ← Show all categories
        </button>
      </section>

      <!-- Thread list -->
      <section>
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-2xl font-bold text-gray-900">Threads</h2>
          <div class="relative">
            <svg class="w-5 h-5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
            </svg>
            <input
              v-model="q"
              class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-cyan-500 focus:border-transparent w-64"
              placeholder="Search threads..."
              type="search"
            />
          </div>
        </div>

        <div class="bg-white rounded-xl border border-gray-200 overflow-hidden">
          <div class="divide-y divide-gray-100">
            <div
              v-for="t in filtered"
              :key="t.id"
              class="p-4 hover:bg-gray-50 transition-colors"
            >
              <div class="flex items-start justify-between gap-4">
                <div class="flex-1 min-w-0">
                  <div class="flex items-center gap-2 mb-1">
                    <span
                      class="px-2 py-0.5 text-xs font-medium rounded"
                      :class="getCategoryColor(t.category)"
                    >
                      {{ categories.find(c => c.id === t.category)?.name }}
                    </span>
                  </div>
                  <RouterLink
                    v-if="t.url && t.url.startsWith('/')"
                    :to="t.url"
                    class="font-medium text-gray-900 hover:text-cyan-600 transition-colors"
                  >{{ t.title }}</RouterLink>
                  <a
                    v-else-if="t.url"
                    :href="t.url"
                    class="font-medium text-gray-900 hover:text-cyan-600 transition-colors"
                    rel="noopener" target="_blank"
                  >{{ t.title }}</a>
                  <span v-else class="font-medium text-gray-900">{{ t.title }}</span>
                  <div class="text-sm text-gray-500 mt-1">
                    by <span class="text-gray-700">{{ t.author }}</span>
                  </div>
                </div>
                <div class="text-right text-sm flex-shrink-0">
                  <div class="text-gray-900">{{ t.replies }} replies</div>
                  <div class="text-gray-500">{{ t.lastActivity }}</div>
                </div>
              </div>
            </div>
            <div v-if="filtered.length === 0" class="p-8 text-center text-gray-500">
              No threads found.
            </div>
          </div>
        </div>
      </section>

      <!-- New Topic -->
      <section class="bg-white rounded-xl border border-gray-200 p-6">
        <h2 class="text-xl font-bold text-gray-900 mb-4">Start a new topic</h2>
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Title</label>
            <input
              v-model="newTopic.title"
              class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
              placeholder="What's your question or topic?"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Category</label>
            <select
              v-model="newTopic.category"
              class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
            >
              <option v-for="c in categories" :key="c.id" :value="c.id">{{ c.name }}</option>
            </select>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Body (optional)</label>
            <textarea
              v-model="newTopic.body"
              class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-cyan-500 focus:border-transparent resize-none h-32"
              placeholder="Add more details..."
            ></textarea>
          </div>

          <div class="flex items-center justify-between">
            <button
              type="button"
              @click="submitTopic"
              class="px-6 py-2 bg-cyan-600 text-white font-medium rounded-lg hover:bg-cyan-700 transition-colors"
            >
              Post topic
            </button>
            <p class="text-xs text-gray-500">
              This is a static demo. Wire this to your backend.
            </p>
          </div>
        </div>
      </section>

      <!-- External Links -->
      <section class="bg-gray-100 rounded-xl p-6">
        <h3 class="font-semibold text-gray-900 mb-3">Join the conversation elsewhere</h3>
        <div class="flex flex-wrap gap-4">
          <a
            href="https://github.com/Numstore/numstore/discussions"
            target="_blank"
            rel="noopener"
            class="inline-flex items-center gap-2 px-4 py-2 bg-white rounded-lg border border-gray-200 text-gray-700 hover:border-cyan-300 transition-colors"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/>
            </svg>
            GitHub Discussions
          </a>
          <a
            href="https://discord.gg/numstore"
            target="_blank"
            rel="noopener"
            class="inline-flex items-center gap-2 px-4 py-2 bg-white rounded-lg border border-gray-200 text-gray-700 hover:border-cyan-300 transition-colors"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028 14.09 14.09 0 0 0 1.226-1.994.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/>
            </svg>
            Discord
          </a>
        </div>
      </section>
    </div>
  </main>
</template>
