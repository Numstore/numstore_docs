<script lang="ts" setup>
import {ref} from 'vue'

const form = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const emails = [
  { label: "General inquiries", email: "hello@numstore.dev" },
  { label: "Enterprise & support", email: "support@numstore.dev" },
  { label: "Consulting", email: "consulting@numstore.dev" },
  { label: "Academic & research", email: "academic@numstore.dev" },
  { label: "Security issues", email: "security@numstore.dev" }
]

function submitForm() {
  const mailto = `mailto:hello@numstore.dev?subject=${encodeURIComponent(form.value.subject)}&body=${encodeURIComponent(`From: ${form.value.name} <${form.value.email}>\n\n${form.value.message}`)}`
  window.location.href = mailto
}
</script>

<template>
  <main class="min-h-screen bg-gray-50">
    <!-- Header -->
    <div class="bg-gradient-to-br from-cyan-600 via-cyan-700 to-teal-800 text-white py-16">
      <div class="max-w-4xl mx-auto px-6">
        <h1 class="text-4xl font-bold mb-4">Contact</h1>
        <p class="text-cyan-100 text-lg max-w-2xl">
          Questions about NumStore? Reach out directly or use the form below.
        </p>
      </div>
    </div>

    <div class="max-w-4xl mx-auto px-6 py-12">
      <div class="grid md:grid-cols-2 gap-12">
        <!-- Direct Contact -->
        <div class="space-y-6">
          <h2 class="text-2xl font-bold text-gray-900">Direct contact</h2>
          <div class="space-y-4">
            <a
              v-for="item in emails"
              :key="item.email"
              :href="`mailto:${item.email}`"
              class="block bg-white rounded-lg border border-gray-200 p-4 hover:border-cyan-300 hover:shadow-sm transition-all"
            >
              <div class="text-sm text-gray-500 mb-1">{{ item.label }}</div>
              <div class="text-cyan-600 font-medium">{{ item.email }}</div>
            </a>
          </div>

          <div class="bg-gray-100 rounded-lg p-4 text-sm text-gray-600">
            <strong>Response times:</strong> I typically respond within 1-2 business days.
            For urgent production issues, use <a href="mailto:support@numstore.dev" class="text-cyan-600 underline">support@numstore.dev</a>.
          </div>
        </div>

        <!-- Contact Form -->
        <div class="space-y-6">
          <h2 class="text-2xl font-bold text-gray-900">Send a message</h2>
          <form class="space-y-4" @submit.prevent="submitForm">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
              <input
                v-model="form.name"
                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
                required
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
              <input
                v-model="form.email"
                type="email"
                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
                required
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Subject</label>
              <input
                v-model="form.subject"
                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Message</label>
              <textarea
                v-model="form.message"
                rows="5"
                class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-cyan-500 focus:border-transparent resize-none"
                required
              ></textarea>
            </div>

            <button
              type="submit"
              class="w-full bg-cyan-600 text-white font-medium py-3 rounded-lg hover:bg-cyan-700 transition-colors"
            >
              Open in email client
            </button>
          </form>
        </div>
      </div>
    </div>
  </main>
</template>
