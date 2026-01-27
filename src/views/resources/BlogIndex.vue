<template>
  <main class="bg-gray-50 min-h-screen">
    <!-- Header -->
    <div class="bg-gradient-to-br from-cyan-600 via-cyan-700 to-teal-800 text-white py-16">
      <div class="max-w-4xl mx-auto px-6">
        <h1 class="text-4xl font-bold mb-4">NumStore Blog</h1>
        <p class="text-cyan-100 text-lg max-w-2xl">
          Technical deep-dives, tutorials, and updates from the NumStore project.
          Learn about architecture, best practices, and real-world use cases.
        </p>
      </div>
    </div>

    <!-- Blog Posts -->
    <div class="max-w-4xl mx-auto px-6 py-12">
      <div class="space-y-8">
        <article
          v-for="post in posts"
          :key="post.slug"
          class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-lg hover:border-cyan-200 transition-all group"
        >
          <RouterLink :to="`/resources/blog/${post.slug}`" class="block">
            <div class="p-6 md:p-8">
              <!-- Date badge -->
              <div class="flex items-center gap-3 mb-4">
                <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-cyan-100 text-cyan-800">
                  <svg class="w-3.5 h-3.5 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                  </svg>
                  {{ formatDate(post.meta.date) }}
                </span>
                <span v-if="isRecent(post.meta.date)" class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-emerald-100 text-emerald-800">
                  New
                </span>
              </div>

              <!-- Title -->
              <h2 class="text-xl md:text-2xl font-bold text-gray-900 mb-3 group-hover:text-cyan-700 transition-colors">
                {{ post.meta.title }}
              </h2>

              <!-- Summary -->
              <p class="text-gray-600 leading-relaxed mb-4">
                {{ post.summary || 'Read more about this topic in the full article.' }}
              </p>

              <!-- Read more link -->
              <div class="flex items-center text-cyan-600 font-medium text-sm group-hover:text-cyan-700">
                <span>Read article</span>
                <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                </svg>
              </div>
            </div>
          </RouterLink>
        </article>
      </div>

      <!-- Empty state -->
      <div v-if="posts.length === 0" class="text-center py-16">
        <svg class="w-16 h-16 text-gray-300 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/>
        </svg>
        <p class="text-gray-500 text-lg">No blog posts yet</p>
        <p class="text-gray-400 text-sm mt-1">Check back soon for new content!</p>
      </div>

      <!-- Newsletter CTA -->
      <div class="mt-16 bg-gradient-to-r from-gray-900 to-gray-800 rounded-2xl p-8 text-center">
        <h3 class="text-2xl font-bold text-white mb-3">Stay Updated</h3>
        <p class="text-gray-400 mb-6 max-w-md mx-auto">
          Get notified about new articles, releases, and NumStore updates.
        </p>
        <div class="flex flex-col sm:flex-row gap-3 justify-center max-w-md mx-auto">
          <input
            type="email"
            placeholder="Enter your email"
            class="flex-1 px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
          />
          <button class="px-6 py-3 bg-cyan-600 text-white font-medium rounded-lg hover:bg-cyan-700 transition-colors">
            Subscribe
          </button>
        </div>
      </div>
    </div>
  </main>
</template>

<script lang="ts" setup>

interface Meta {
  title: string;
  date: string
}

interface EntryModule {
  default: any;
  meta?: Meta;
  summary?: string
}

const modules = import.meta.glob('./blog_entries/*.vue', {eager: true}) as Record<string, EntryModule>

function byDateDesc(a: string, b: string): number {
// Prefer meta.date if present; otherwise, parse leading YYYY-MM-DD from filename
  const am = modules[a].meta?.date || a.match(/(\d{4}-\d{2}-\d{2})/)?.[1] || '1970-01-01'
  const bm = modules[b].meta?.date || b.match(/(\d{4}-\d{2}-\d{2})/)?.[1] || '1970-01-01'
  return am < bm ? 1 : am > bm ? -1 : 0
}

const posts = Object.keys(modules)
    .sort(byDateDesc)
    .map((path) => {
      const slug = path.split('/').pop()!.replace('.vue', '')
      const mod = modules[path]
      return {
        slug,
        meta: mod.meta || {title: slug, date: slug.slice(0, 10)},
        summary: mod.summary || '',
      }
    })

function formatDate(dateStr: string): string {
  const date = new Date(dateStr)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

function isRecent(dateStr: string): boolean {
  const date = new Date(dateStr)
  const now = new Date()
  const diffDays = (now.getTime() - date.getTime()) / (1000 * 60 * 60 * 24)
  return diffDays <= 14 // Consider posts from last 2 weeks as "new"
}
</script>
