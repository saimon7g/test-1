<template>
  <div class="max-w-4xl mx-auto">
    <!-- Download Button -->
    <div class="mb-8 flex justify-center">
      <a 
        href="/Nur_Uddin_Resume.pdf" 
        download
        class="bg-gray-900 hover:bg-gray-800 text-white font-semibold py-2 px-6 rounded-lg flex items-center space-x-2 transition-colors"
      >
        <i class="fas fa-download"></i>
        <span>Download Resume</span>
      </a>
    </div>

    <!-- PDF Viewer with intersection observer -->
    <div 
      ref="pdfContainer"
      class="w-full h-[800px] border border-gray-200 rounded-lg overflow-hidden shadow-lg bg-white"
    >
      <object
        v-if="isVisible"
        data="/Nur_Uddin_Resume.pdf"
        type="application/pdf"
        width="100%"
        height="100%"
        class="w-full h-full"
      >
        <p>It appears you don't have a PDF plugin for this browser. You can 
          <a href="/Nur_Uddin_Resume.pdf">click here to download the PDF file.</a>
        </p>
      </object>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue'

export default {
  name: 'Resume',
  setup() {
    const pdfContainer = ref(null)
    const isVisible = ref(false)
    let observer = null

    onMounted(() => {
      observer = new IntersectionObserver(
        ([entry]) => {
          if (entry.isIntersecting) {
            isVisible.value = true
            observer.disconnect()
          }
        },
        {
          threshold: 0.1
        }
      )

      if (pdfContainer.value) {
        observer.observe(pdfContainer.value)
      }
    })

    onUnmounted(() => {
      if (observer) {
        observer.disconnect()
      }
    })

    return {
      pdfContainer,
      isVisible
    }
  }
}
</script>