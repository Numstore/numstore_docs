<template>
  <div class="max-w-5xl mx-auto">
    <!-- Hero / Sales Pitch Section -->
    <section class="text-center py-16 px-6">
      <h1 class="text-5xl font-bold text-gray-900 mb-6">
        The Database Built for Machine Learning
      </h1>
      <p class="text-xl text-gray-700 mb-8 max-w-3xl mx-auto">
        Numstore is a high-performance embedded database optimized for numeric and time-series data.
        Built in pure C with zero dependencies, it integrates seamlessly into any language or platform.
      </p>

      <!-- Download CTA -->
      <div class="flex flex-col sm:flex-row gap-4 justify-center items-center mb-8">
        <a
          href="#download"
          class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-8 rounded-lg text-lg transition-colors"
        >
          <i class="fa-solid fa-download mr-2"></i>
          Download Numstore
        </a>
        <a
          href="#docs"
          class="bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-4 px-8 rounded-lg text-lg transition-colors"
        >
          View Documentation
        </a>
      </div>

      <p class="text-sm text-gray-600">
        Latest version: 1.0.0 • Free and Open Source
      </p>
    </section>

    <!-- Product Description Section -->
    <section id="product" class="py-12 px-6 bg-gray-50 rounded-lg mb-8">
      <h2 class="text-3xl font-bold text-gray-900 mb-6">What is Numstore?</h2>
      <div class="space-y-4 text-gray-700">
        <p>
          Numstore is an embedded database designed specifically for numeric and time-series workloads.
          Unlike traditional databases, Numstore optimizes for the unique patterns of machine learning pipelines,
          scientific computing, and data analysis workflows.
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
          <div class="bg-white p-6 rounded-lg shadow-sm">
            <h3 class="font-bold text-lg text-blue-700 mb-2">
              <i class="fa-solid fa-gauge-high mr-2"></i>
              Extreme Performance
            </h3>
            <p class="text-sm">
              10-100x faster than traditional databases for numeric operations and time-series queries.
            </p>
          </div>
          <div class="bg-white p-6 rounded-lg shadow-sm">
            <h3 class="font-bold text-lg text-blue-700 mb-2">
              <i class="fa-solid fa-code mr-2"></i>
              Pure C Implementation
            </h3>
            <p class="text-sm">
              Zero dependencies. Embed in Python, Java, Go, Rust, or any language with C bindings.
            </p>
          </div>
          <div class="bg-white p-6 rounded-lg shadow-sm">
            <h3 class="font-bold text-lg text-blue-700 mb-2">
              <i class="fa-solid fa-microchip mr-2"></i>
              Optimized Data Structures
            </h3>
            <p class="text-sm">
              Rope trees and contiguous data models designed for ML and analytics workloads.
            </p>
          </div>
          <div class="bg-white p-6 rounded-lg shadow-sm">
            <h3 class="font-bold text-lg text-blue-700 mb-2">
              <i class="fa-solid fa-users mr-2"></i>
              Early Adopter Benefits
            </h3>
            <p class="text-sm">
              Shape the roadmap, get direct maintainer access, and influence future development.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Download Section -->
    <section id="download" class="py-12 px-6 mb-8">
      <h2 class="text-3xl font-bold text-gray-900 mb-6">Download</h2>
      <div class="bg-blue-50 border-2 border-blue-200 rounded-lg p-8">
        <div class="flex flex-col md:flex-row items-center justify-between gap-6">
          <div>
            <h3 class="text-2xl font-bold text-gray-900 mb-2">Numstore v1.0.0</h3>
            <p class="text-gray-700">Latest stable release</p>
            <p class="text-sm text-gray-600 mt-2">
              Available for Linux, macOS, and Windows
            </p>
          </div>
          <div class="flex flex-col gap-3">
            <button
              @click="handleDownload"
              class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-colors"
            >
              <i class="fa-solid fa-download mr-2"></i>
              Download for {{ platform }}
            </button>
            <a
              href="#"
              class="text-center text-sm text-blue-600 hover:text-blue-800"
            >
              View all versions
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Documentation Section -->
    <section id="docs" class="py-12 px-6 bg-gray-50 rounded-lg mb-8">
      <h2 class="text-3xl font-bold text-gray-900 mb-6">Documentation</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded-lg shadow-sm border-l-4 border-blue-600">
          <h3 class="font-bold text-lg text-gray-900 mb-2">Getting Started</h3>
          <p class="text-sm text-gray-700 mb-4">
            Quick start guide to install and use Numstore in your project.
          </p>
          <a href="#" class="text-blue-600 hover:text-blue-800 text-sm font-medium">
            Read Guide →
          </a>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border-l-4 border-blue-600">
          <h3 class="font-bold text-lg text-gray-900 mb-2">API Reference</h3>
          <p class="text-sm text-gray-700 mb-4">
            Complete API documentation for all Numstore operations.
          </p>
          <a href="#" class="text-blue-600 hover:text-blue-800 text-sm font-medium">
            View API Docs →
          </a>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-sm border-l-4 border-blue-600">
          <h3 class="font-bold text-lg text-gray-900 mb-2">Tutorials</h3>
          <p class="text-sm text-gray-700 mb-4">
            Step-by-step tutorials for common use cases and integrations.
          </p>
          <a href="#" class="text-blue-600 hover:text-blue-800 text-sm font-medium">
            Browse Tutorials →
          </a>
        </div>
      </div>
    </section>

    <!-- Usage Section -->
    <section id="usage" class="py-12 px-6 mb-8">
      <h2 class="text-3xl font-bold text-gray-900 mb-6">Usage Examples</h2>
      <div class="space-y-6">
        <div class="bg-gray-900 text-gray-100 p-6 rounded-lg">
          <h3 class="text-sm font-semibold text-gray-400 mb-3">Python Integration</h3>
          <pre class="text-sm overflow-x-auto"><code>import numstore

# Create a new database
db = numstore.Database("mydata.nstore")

# Store numeric data
db.insert(timestamps, values)

# Query with high performance
results = db.query(start_time, end_time)</code></pre>
        </div>
        <div class="bg-gray-900 text-gray-100 p-6 rounded-lg">
          <h3 class="text-sm font-semibold text-gray-400 mb-3">C API</h3>
          <pre class="text-sm overflow-x-auto"><code>#include "numstore.h"

// Initialize database
numstore_db* db = numstore_open("mydata.nstore");

// Store time-series data
numstore_insert(db, timestamps, values, count);

// Efficient range queries
numstore_query(db, start, end, &results);</code></pre>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-12 px-6 bg-gray-50 rounded-lg mb-8">
      <h2 class="text-3xl font-bold text-gray-900 mb-6">About Numstore</h2>
      <div class="space-y-4 text-gray-700">
        <p>
          Numstore was created to solve the performance challenges faced when working with large-scale
          numeric and time-series data in machine learning and scientific computing environments.
        </p>
        <p>
          Built from the ground up in dependency-free C, Numstore can be embedded into any application
          or language runtime. The project is in active development, and early adopters have the unique
          opportunity to shape its future direction.
        </p>
        <div class="mt-6 flex flex-wrap gap-4">
          <a
            href="#"
            class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium"
          >
            <i class="fa-brands fa-github mr-2"></i>
            View on GitHub
          </a>
          <a
            href="#"
            class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium"
          >
            <i class="fa-solid fa-book mr-2"></i>
            Research Papers
          </a>
          <a
            href="#"
            class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium"
          >
            <i class="fa-solid fa-envelope mr-2"></i>
            Contact Us
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

// Detect platform for download button
const platform = computed(() => {
  const ua = navigator.userAgent.toLowerCase()
  if (ua.includes('mac')) return 'macOS'
  if (ua.includes('win')) return 'Windows'
  if (ua.includes('linux')) return 'Linux'
  return 'Your Platform'
})

// Mock download handler
const handleDownload = () => {
  alert('Download started! (This is a mock download)')
}
</script>

<style scoped>
/* Smooth scrolling for anchor links */
html {
  scroll-behavior: smooth;
}
</style>
