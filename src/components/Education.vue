<template>
  <div class="bg-white dark:bg-dark-bg p-4 lg:p-6 rounded-lg shadow max-w-6xl mx-auto">
    <!-- Education Section -->
    <div class="mb-12">
      <h2 class="text-2xl lg:text-3xl font-bold mb-6 text-primary dark:text-dark-text border-b pb-2">
        Education
      </h2>

      <!-- University Section -->
      <div class="mb-8">
        <h3 class="text-xl lg:text-2xl font-bold mb-4 text-primary dark:text-dark-text">
          Bangladesh University of Engineering and Technology (BUET)
        </h3>
        <div class="flex flex-col lg:flex-row lg:items-center mb-4">
          <div class="text-primary dark:text-dark-text mb-2 lg:mb-0">
            <p class="mb-1">BACHELOR OF SCIENCE</p>
            <p>Computer Science and Engineering</p>
          </div>
          <div class="lg:flex-1 lg:text-right">
            <p class="italic text-secondary dark:text-dark-text-secondary">February 2020 - Running</p>
            <p class="text-primary dark:text-dark-text">CGPA: 3.21/4.00</p>
          </div>
        </div>
      </div>

      <!-- College Section -->
      <div>
        <h3 class="text-xl lg:text-2xl font-bold mb-4 text-primary dark:text-dark-text">
          Notre Dame College, Dhaka
        </h3>
        <div class="flex flex-col lg:flex-row lg:items-center">
          <div class="text-primary dark:text-dark-text mb-2 lg:mb-0">
            <p class="mb-1">Group: SCIENCE</p>
          </div>
          <div class="lg:flex-1 lg:text-right">
            <p class="italic text-secondary dark:text-dark-text-secondary">July 2017 - June 2019</p>
            <p class="text-primary dark:text-dark-text">GPA: 5.00/5.00</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Skills Section -->
    <div>
      <h2 class="text-2xl lg:text-3xl font-bold mb-6 text-primary dark:text-dark-text border-b pb-2">
        Technical Skills
      </h2>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Dynamically render skill categories -->
        <div v-for="(skills, category) in skillsData" :key="category" class="mb-6">
          <h3 class="text-lg font-semibold mb-3 text-primary dark:text-dark-text">
            {{ category }}
          </h3>
          <div class="flex flex-wrap gap-2">
            <span v-for="skill in skills" :key="skill"
              class="px-3 py-1 bg-gray-200 dark:bg-gray-700 rounded-full text-sm">
              {{ skill }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Education',
  data() {
    return {
      skillsData: {
        'Programming Languages': [
          'C',
          'C++',
          'Java',
          'Python',
          'JavaScript'
        ],
        'Web Technologies': [
          'ReactJS',
          'NextJS',
          'VueJS',
          'Django',
          'HTML/CSS',
          'REST APIs',
          'Vite',
          'Tailwind CSS'
        ],
        'Frameworks & Tools': [
          'Git/Github',
          'Docker',
          'Linux',
          'Bash',
          'OpenGL',
          'JavaFX',
          'Cisco Packet Tracer',
          'NS-3',
          'Bison',
          'Flex'
        ],
        'Database': [
          'Oracle',
          'MySQL',
          'Django ORM'
        ],
        'Data Science & ML': [
          'TensorFlow',
          'PyTorch',
          'Scikit-learn',
          'Pandas',
          'NumPy'
        ]
      }
    }
  }
}
</script>