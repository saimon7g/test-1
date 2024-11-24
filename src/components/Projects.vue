<template>
  <div class="bg-white dark:bg-dark-bg p-4 lg:p-6 rounded-lg shadow max-w-6xl mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 lg:gap-6">
      <div v-for="(project, idx) in projects" :key="idx"
        class="p-4 rounded-lg border border-secondary/20 dark:border-dark-text-secondary/20 hover:shadow-md transition-shadow bg-white dark:bg-dark-bg-secondary h-full">
        <div class="flex items-center justify-between mb-2">
          <h5 class="font-bold text-lg text-primary dark:text-dark-text">{{ project.name }}</h5>
          <a v-if="project.github" :href="project.github" target="_blank"
            class="text-gray-600 hover:text-gray-800 dark:text-gray-400 dark:hover:text-gray-200">
            <i class="fab fa-github text-xl"></i>
          </a>
        </div>
        <p class="text-sm mb-2 text-secondary dark:text-dark-text-secondary">
          <span class="font-medium">::</span>
          <span class="italic ml-2">{{ project.organization }}</span>
        </p>
        <p class="text-sm text-secondary dark:text-dark-text-secondary leading-relaxed flex-grow mb-4">
          {{ project.description }}
        </p>
        <p class="text-sm text-secondary dark:text-dark-text-secondary">
          <span class="font-medium">Tech:</span>
          <span class="italic ml-2">{{ project.tech }}</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Projects',
  setup() {
    const projects = [
      {
        name: "DX-ball Game Recreation",
        organization: "CSE-102, Structured Programming Language Sessional",
        description: "Recreated classic DX-ball game using OpenGL and iGraphics. Implemented complex collision, power-ups (fireball, paddle modifications), 4-level system with unique patterns, and save/load functionality. Features include progressive difficulty, multi-ball system, and high score tracking. Used struct-based object management, timer-based animations, and binary file I/O for game state persistence.",
        tech: "C, OpenGL, iGraphics Library",
        github: "https://github.com/yourusername/dxball-game"  // Add your actual GitHub repo link here
      },
      {
        name: "Football Transfer Market System",
        organization: "CSE-108, Object Oriented Programming Sessional",
        description: "Built a real-time football transfer market system with multi-club support using socket programming. Implemented features like club-based authentication, live player trading between multiple clubs, market monitoring, and club analytics. Designed with multi-threaded server to handle concurrent club connections and JavaFX-based responsive UI.",
        tech: "Java, JavaFX, Socket Programming, Multi-threading, File I/O",
        github: "https://github.com/yourusername/football-transfer-market"  // Add your actual repo link here
      },
      {
        name: "Railway E-Ticket Reservation System",
        organization: "CSE Database Project",
        description: "Designed and implemented a comprehensive railway reservation database system with Django and Oracle. Created complex database architecture including transaction management, real-time seat availability tracking, and automated reservation timeout triggers. Implemented intricate SQL queries for station-to-station fare calculation, multi-class seat management, and booking validations. Features include secure user authentication, interactive seat selection, and integrated payment verification system.",
        tech: "Oracle Database, Django, Python, SQL, PL/SQL Triggers",
        github: "https://github.com/yourusername/railway-ticket-system"  // Add your actual repo link
      },
    ]
    return {
      projects
    }
  }
}
</script>