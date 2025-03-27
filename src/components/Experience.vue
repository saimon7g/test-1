<template>
  <div class="bg-white dark:bg-dark-bg p-4 lg:p-6 rounded-lg shadow max-w-6xl mx-auto">
    <!-- Work Experience Section -->
    <template v-for="(workplace, idx) in workplaces" :key="idx">
      <div class="mb-6 last:mb-0">
        <h3 class="text-xl lg:text-2xl font-bold mb-4 text-primary dark:text-dark-text">
          {{ workplace.name }}
        </h3>
        <div class="flex flex-col lg:flex-row lg:items-center mb-3">
          <div class="text-primary dark:text-dark-text mb-2 lg:mb-0">
            <p class="font-medium">{{ workplace.role }}</p>
          </div>
          <div class="lg:flex-1 lg:text-right">
            <p class="italic text-secondary dark:text-dark-text-secondary">{{ workplace.duration }}</p>
          </div>
        </div>
        
        <!-- Team details section -->
        <div v-if="workplace.teams && workplace.teams.length > 0" class="ml-4 text-sm text-secondary dark:text-dark-text-secondary">
          <div v-for="(team, teamIdx) in workplace.teams" :key="teamIdx" class="mb-2">
            <p class="font-medium">{{ team.name }}:</p>
            <p class="ml-2">{{ team.description }}</p>
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
        name: "Bengal Mobile QA Solution",
        duration: "January 2025 - Present",
        role: "Software Engineer",
        teams: [
  {
    "name": "Team-1",
    "description": "Working with CyberSecurity Research Team to develop a machine learning-based approach for detecting zero-day attacks and firewall vulnerabilities in network security systems"
  },
  {
    "name": "Team-2",
    "description": "Collaborating with the Android development team to build a comprehensive ticket management system using Flutter framework"
  }
]
      }
    ]

    return {
      workplaces
    }
  }
}
</script>