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
        
        <!-- Projects section -->
        <div v-if="workplace.projects && workplace.projects.length > 0" class="mt-6">
          <h4 class="text-base lg:text-lg font-semibold text-primary dark:text-dark-text mb-4">
            Key Projects at BMQAS
          </h4>
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 lg:gap-6">
            <div
              v-for="(project, projectIdx) in workplace.projects"
              :key="projectIdx"
              class="p-4 rounded-lg border border-secondary/20 dark:border-dark-text-secondary/20 hover:shadow-md transition-shadow bg-white dark:bg-dark-bg-secondary h-full"
            >
              <div class="flex items-center justify-between mb-2">
                <p class="font-bold text-lg text-primary dark:text-dark-text">{{ project.name }}</p>
                <a
                  :href="project.link"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="text-gray-600 hover:text-gray-800 dark:text-gray-400 dark:hover:text-gray-200"
                  aria-label="Open project link"
                >
                  <i class="fas fa-external-link-alt text-base"></i>
                </a>
              </div>
              <p class="text-sm mb-2 text-secondary dark:text-dark-text-secondary">
                <span class="font-medium">::</span>
                <span class="italic ml-2">{{ project.organization }}</span>
              </p>
              <p class="text-sm text-secondary dark:text-dark-text-secondary leading-relaxed flex-grow mb-4">
                {{ project.summary }}
              </p>
              <p class="text-sm text-secondary dark:text-dark-text-secondary">
                <span class="font-medium">Tech:</span> {{ project.tech }}
              </p>
            </div>
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
        projects: [
          {
            name: "Cybersecurity Research Project",
            organization: "BMQAS CyberSecurity Research Team",
            summary: "Built an ML-driven detection workflow for zero-day attacks and firewall vulnerabilities to strengthen early threat analysis in network security systems.",
            tech: "Python, Machine Learning, Network Security",
            link: "https://github.com/saimon7g"
          },
          {
            name: "Digital Product Passport (DPP)",
            organization: "Supply Chain Traceability Platform",
            summary: "Shipped a DPP system for textile supply chains with order/batch traceability, verifier workflows, and public passport links for transparent product records.",
            tech: "Next.js, TypeScript, PostgreSQL, Prisma, Angular, Tailwind CSS",
            link: "https://github.com/saimon7g"
          },
          {
            name: "Hope Healthcare Mobile Client",
            organization: "Healthcare Platform",
            summary: "Delivered cross-platform patient/provider mobile workflows with role-aware navigation, scheduling, and push-enabled engagement to support day-to-day clinical operations.",
            tech: "Flutter, Dart, GetX, Dio, Firebase Messaging, Geolocator",
            link: "https://github.com/saimon7g"
          },
          {
            name: "Cow Insurance and Muzzle-ID System (PoC)",
            organization: "AI + Insurtech Proof of Concept",
            summary: "Built a role-based livestock insurance platform with claim lifecycle automation and muzzle-image identification for practical field verification.",
            tech: "Django REST Framework, JWT, PyTorch, SQLite, Flutter",
            link: "https://github.com/saimon7g"
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