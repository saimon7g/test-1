<template>
    <div class="bg-white dark:bg-dark-bg p-4 lg:p-6 rounded-lg shadow max-w-6xl mx-auto">
      <!-- Work Experience Section -->
      <template v-for="(workplace, idx) in workplaces" :key="idx">
        <div class="mb-6 last:mb-0">
          <h3 class="text-xl lg:text-2xl font-bold mb-4 text-primary dark:text-dark-text">
            {{ workplace.name }}
          </h3>
          <div class="flex flex-col lg:flex-row lg:items-center">
            <div class="text-primary dark:text-dark-text mb-2 lg:mb-0">
              <p class="font-medium">{{ workplace.role }}</p>
            </div>
            <div class="lg:flex-1 lg:text-right">
              <p class="italic text-secondary dark:text-dark-text-secondary">{{ workplace.duration }}</p>
            </div>
          </div>
        </div>
      </template>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Experience',
    setup() {
      const workplaces = [
        {
          name: "Bengal Mobile Quality and AI Security",
          duration: "October 2024 - Present",
          role: "Software Engineer",
        },
        {
          name: "Bengal Mobile Quality and AI Security",
          duration: "December 2023 - July 2024",
          role: "Consultant",
        },
        {
          name: "Computer Network Systems Limited",
          duration: "June 2023 - July 2024",
          role: "Assistant Software Engineer"
        },
        {
          name: "AODoubleClick",
          duration: "Oct 2022 - Present",
          role: "Part Time Software Engineer",
        },
        {
          name: "Sedbox",
          duration: "May 2022 - Nov 2022",
          role: "Intern",
        }
      ]
  
      return {
        workplaces
      }
    }
  }
  </script>