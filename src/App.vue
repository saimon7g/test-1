<template>
  <div class="flex min-h-screen bg-gray-100">
    <!-- Sidebar -->
    <aside class="w-72 bg-[#1d1d1d] text-white fixed h-full z-50">
      <div class="flex flex-col items-center pt-12 pb-8">
        <div class="w-32 h-32 rounded-full overflow-hidden mb-4">
          <img 
            src="./assets/saimon.jpg" 
            alt="Profile" 
            class="w-full h-full object-cover"
          />
        </div>
        <h2 class="text-xl font-semibold mb-1">Nur Uddin Ibne Huda</h2>
        <p class="text-sm text-gray-400">Final Year CSE Student, BUET</p>
        <p class="text-sm text-gray-400">Dhaka, Bangladesh</p>
      </div>
      
      <!-- Navigation Links -->
      <nav class="flex flex-col w-full mt-8">
        <a 
          v-for="section in sections" 
          :key="section.id"
          @click="scrollToSection(section.id)"
          class="relative py-2 px-8 text-sm cursor-pointer transition-all duration-200 select-none"
          :class="[
            activeSection === section.id 
              ? 'text-white' 
              : 'text-gray-400 hover:text-white'
          ]"
        >
          <!-- Background highlight -->
          <div 
            v-if="activeSection === section.id"
            class="absolute left-0 top-0 w-full h-full bg-gray-800 transition-all duration-300"
            style="z-index: -1;"
          ></div>
          
          {{ section.title.toUpperCase() }}
        </a>
      </nav>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 ml-72 bg-gray-50">
      <div class=" h-screen overflow-y-auto">
        <section 
          v-for="section in sections" 
          :key="section.id" 
          :id="section.id"
          class=" h-screen w-full"
        >
          <div class="h-full p-8">
            <h2 class="text-3xl font-bold mb-8 p-4 rounded text-center">
              {{ section.title }}
            </h2>
            <component :is="section.component" />
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script>
import { ref } from 'vue'
import About from './components/About.vue'
import Publications from './components/Publications.vue'
import Research from './components/Research.vue'
import Education from './components/Education.vue'
import Experience from './components/Experience.vue'
// import Awards from './components/Awards.vue'

export default {
  name: 'App',
  components: {
    About,
    Publications,
    Research,
    Education,
    Experience,
    // Awards
  },
  setup() {
    const activeSection = ref('about')

    const sections = [
      { id: 'about', title: 'About', component: About },
      { id: 'research', title: 'Research Experience', component: Research },
      { id: 'publications', title: 'Publications', component: Publications },
      { id: 'education', title: 'Education', component: Education },
      { id: 'experience', title: 'Work Experience', component: Experience },
      // { id: 'awards', title: 'Awards', component: Awards }
    ]

    const scrollToSection = (id) => {
      const element = document.getElementById(id)
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
        activeSection.value = id
      }
    }

    return {
      sections,
      activeSection,
      scrollToSection
    }
  }
}
</script>

<style>
html {
  scroll-behavior: smooth;
}

::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>