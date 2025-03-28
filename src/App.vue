<template>
  <div class="flex min-h-screen bg-gray-100 dark:bg-dark-bg relative">
    <!-- Mobile Menu Button -->
    <button @click="toggleSidebar" class="lg:hidden fixed top-4 left-4 z-50 p-2 rounded-lg bg-gradient-to-r from-gray-900 to-gray-950 dark:from-gray-900 dark:to-gray-950 text-white">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
      </svg>
    </button>

    <!-- Overlay for mobile -->
    <div v-if="isSidebarOpen" @click="toggleSidebar" class="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden"></div>

    <!-- Sidebar -->
    <aside :class="[
      'bg-gradient-to-b from-gray-400 to-gray-900 dark:from-gray-450 dark:to-gray-950 text-white fixed h-full z-50 transition-transform duration-300 ease-in-out',
      'w-72 lg:translate-x-0',
      isSidebarOpen ? 'translate-x-0' : '-translate-x-full'
    ]">
      <div class="flex flex-col items-center pt-12 pb-4">
        <div class="w-24 h-24 lg:w-32 lg:h-32 rounded-full overflow-hidden mb-4 border-4 border-white dark:border-gray-700 shadow-md">
          <img src="./assets/saimon3.jpg" alt="Profile" class="w-full h-full object-cover" />
        </div>
        <h2 class="text-lg lg:text-xl font-semibold mb-1">Nur Uddin Ibne Huda</h2>
        <p class="text-xs lg:text-sm text-gray-200 dark:text-gray-300">CS Graduate, BUET</p>
        <p class="text-xs lg:text-sm text-gray-200 dark:text-gray-300 mb-4">Dhaka, Bangladesh</p>

        <!-- Social Icons Section -->
        <div class="flex space-x-6 mb-6">
          <a href="https://github.com/saimon7g" class="text-gray-200 dark:text-gray-300 hover:text-white transition-colors" target="_blank"
            rel="noopener noreferrer">
            <i class="fab fa-github text-2xl"></i>
          </a>
          <a href="https://www.linkedin.com/in/Nur-Uddin-Ibne-Huda"
            class="text-gray-200 dark:text-gray-300 hover:text-white transition-colors" target="_blank" rel="noopener noreferrer">
            <i class="fab fa-linkedin text-2xl"></i>
          </a>
          <a href="#resume" @click="navigateToSection('resume')"
            class="text-gray-200 dark:text-gray-300 hover:text-white transition-colors">
            <i class="fas fa-file-alt text-2xl"></i>
          </a>
        </div>
      </div>

      <!-- Navigation Links -->
      <nav class="flex flex-col w-full mt-4">
        <a v-for="section in sections" :key="section.id" @click="navigateToSection(section.id)"
          class="relative py-2 px-8 text-sm cursor-pointer transition-all duration-200 select-none" :class="[
            activeSection === section.id
              ? 'text-white'
              : 'text-gray-200 dark:text-gray-300 hover:text-white'
          ]">
          <div v-if="activeSection === section.id"
            class="absolute left-0 top-0 w-full h-full bg-black bg-opacity-30 dark:bg-gray-900 dark:bg-opacity-70 transition-all duration-300"
            style="z-index: -1;"></div>

          {{ section.title.toUpperCase() }}
        </a>
      </nav>
    </aside>

    <!-- Main Content -->
    <main :class="[
      'flex-1 transition-all duration-300 bg-gray-50 dark:bg-dark-bg',
      'w-full lg:ml-72'
    ]">
      <div class="flex flex-col min-h-screen">
        <!-- Hero Banner Section -->
        <div class="w-full bg-gradient-to-r from-gray-400 to-gray-900 dark:from-gray-450 dark:to-black">
          <div class="max-w-6xl mx-auto px-4 py-16 lg:py-20">
            <div class="flex flex-col md:flex-row items-center justify-between">
              <div class="w-full md:w-1/2 mb-8 md:mb-0 text-center md:text-left">
                <h1 class="text-4xl lg:text-5xl font-bold text-white mb-4">Nur Uddin Ibne Huda</h1>

                <p class="text-xl text-gray-300 mb-6">Computer Science Engineer | AI Enthusiast | Software Developer</p>
                
                <!-- Mobile Profile Photo (Only visible on mobile) -->
                <div class="md:hidden mx-auto mb-6">
                  <div class="w-48 h-48 rounded-2xl overflow-hidden border-4 border-white dark:border-gray-700 shadow-lg mx-auto">
                    <img src="./assets/saimon2.jpg" alt="Profile" class="w-full h-full object-cover" />
                  </div>
                </div>
                
               
                <p class="text-gray-300 mb-8 max-w-lg mx-auto md:mx-0">
                  Fresh graduate CS student from BUET with a focus on AI and Software Security. Passionate about solving complex problems and exploring cutting-edge technologies.
                </p>
                <div class="flex justify-center md:justify-start space-x-4">
                  <a href="https://github.com/saimon7g" target="_blank" rel="noopener noreferrer"
                     class="px-6 py-3 bg-transparent border border-white text-white rounded-lg font-medium hover:bg-white/10 transition-colors flex items-center">
                    <i class="fab fa-github mr-2"></i>
                    GitHub
                  </a>
                  <a href="#resume" @click="navigateToSection('resume')" 
                     class="px-6 py-3 bg-transparent border border-white text-white rounded-lg font-medium hover:bg-white/10 transition-colors flex items-center">
                    <i class="fas fa-file-alt mr-2"></i>
                    Resume
                  </a>
                </div>
              </div>
              <!-- Desktop Profile Photo (Only visible on desktop) -->
              <div class="w-full md:w-1/2 hidden md:flex justify-center">
                <div class="w-56 h-56 lg:w-72 lg:h-72 rounded-2xl overflow-hidden border-4 border-white dark:border-gray-700 shadow-xl">
                  <img src="./assets/saimon2.jpg" alt="Profile" class="w-full h-full object-cover" />
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Sections Container -->
        <div class="flex-1">
          <section v-for="section in sections" :key="section.id" :id="section.id"
            class="w-full pt-16 lg:pt-24 pb-16 border-b border-gray-200 dark:border-gray-800 last:border-0">
            <div class="p-4 lg:p-8">
              <h2
                class="text-2xl lg:text-3xl font-bold mb-6 lg:mb-8 p-4 rounded text-center text-gray-800 dark:text-gray-200">
                {{ section.title }}
              </h2>
              <component :is="section.component" />
            </div>
          </section>
        </div>

        <!-- Footer -->
        <footer class="w-full bg-gradient-to-r from-gray-700 to-gray-900 dark:from-gray-800 dark:to-gray-950 text-white py-8 px-4">
          <div class="max-w-6xl mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
              <!-- Contact Info -->
              <div>
                <h3 class="text-lg font-semibold mb-4">Contact</h3>
                <p class="text-gray-300 mb-2">Email: nuruddin(dot)simon(at)gmail(dot)com</p>
                <p class="text-gray-300 mb-2">Phone: +880 1871 809096</p>
                <p class="text-gray-300">Location: Dhaka, Bangladesh</p>
              </div>

              <!-- Quick Links -->
              <div>
                <h3 class="text-lg font-semibold mb-4">Quick Links</h3>
                <ul class="space-y-2">
                  <li><a href="#about" class="text-gray-300 hover:text-white transition-colors">About</a></li>
                  <li><a href="#research" class="text-gray-300 hover:text-white transition-colors">Research</a></li>
                  <li><a href="#publications" class="text-gray-300 hover:text-white transition-colors">Publications</a>
                  </li>
                </ul>
              </div>

              <!-- Social Links -->
              <div>
                <h3 class="text-lg font-semibold mb-4">Connect</h3>
                <div class="flex space-x-4">
                  <a href="https://www.linkedin.com/in/Nur-Uddin-Ibne-Huda"
                    class="text-gray-300 hover:text-white transition-colors">
                    <i class="fab fa-linkedin text-xl"></i>
                  </a>
                  <a href="https://github.com/saimon7g" class="text-gray-300 hover:text-white transition-colors">
                    <i class="fab fa-github text-xl"></i>
                  </a>
                  <a href="https://x.com/saimon7t" class="text-gray-300 hover:text-white transition-colors">
                    <i class="fab fa-twitter text-xl"></i>
                  </a>
                </div>
              </div>

              <!-- Source Code -->
              <div>
                <h3 class="text-lg font-semibold mb-4">Source Code</h3>
                <a href="https://github.com/saimon7g" target="_blank" rel="noopener noreferrer"
                  class="text-gray-300 hover:text-white transition-colors flex items-center">
                  <i class="fab fa-github mr-2"></i>
                  Visit my GitHub for source code
                </a>
              </div>
            </div>
          </div>
        </footer>
      </div>
    </main>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import About from './components/About.vue'
import Publications from './components/Publications.vue'
import Research from './components/Research.vue'
import Education from './components/Education.vue'
import Courses from './components/Courses.vue'
import Experience from './components/Experience.vue'
import Projects from './components/Projects.vue'
import Resume from './components/Resume.vue'
import Certificates from './components/Certificates.vue'

export default {
  name: 'App',
  components: {
    About,
    Publications,
    Research,
    Education,
    Courses,
    Experience,
    Projects,
    Resume,
    Certificates
  },
  setup() {
    const activeSection = ref('about')
    const isSidebarOpen = ref(false)

    onMounted(() => {
      window.history.scrollRestoration = 'manual'
      document.documentElement.scrollTop = 0
      document.body.scrollTop = 0
    })

    const sections = [
      { id: 'about', title: 'About', component: About },
      { id: 'experience', title: 'Experience', component: Experience },
      { id: 'education', title: 'Education and Skills', component: Education },
      { id: 'projects', title: 'Projects', component: Projects },
      { id: 'certificates', title: 'Certificates', component: Certificates },
      { id: 'courses', title: 'Notable Courses', component: Courses },
      { id: 'research', title: 'Research Experience', component: Research },
      // { id: 'publications', title: 'Publications', component: Publications },
      { id: 'resume', title: 'Resume', component: Resume },
    ]

    const toggleSidebar = () => {
      isSidebarOpen.value = !isSidebarOpen.value
    }

    const navigateToSection = (id) => {
      const element = document.getElementById(id)
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
        activeSection.value = id
        isSidebarOpen.value = false
      }
    }

    return {
      sections,
      activeSection,
      isSidebarOpen,
      toggleSidebar,
      navigateToSection
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

section {
  scroll-margin-top: 80px;
}

@media (max-width: 1024px) {
  html {
    scroll-padding-top: 80px;
  }
}

@media (min-width: 1024px) {
  section {
    scroll-margin-top: 0;
  }
}
</style>