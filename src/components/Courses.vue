<template>
    <div class="bg-white dark:bg-dark-bg p-4 lg:p-6 rounded-lg shadow max-w-6xl mx-auto">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 lg:gap-6">
        <a v-for="course in courses" :key="course.code" :href="course.link"
          class="p-4 rounded-lg border border-secondary/20 dark:border-dark-text-secondary/20 hover:shadow-md transition-shadow bg-white dark:bg-dark-bg-secondary">
          <h5 class="font-bold text-lg mb-2 text-primary dark:text-dark-text">{{ course.code }}: {{ course.name }}</h5>
          <p class="text-sm text-secondary dark:text-dark-text-secondary leading-relaxed">
            <span v-for="(topic, index) in course.topics" :key="index">
              {{ topic }}<span v-if="index !== course.topics.length - 1">, </span>
            </span>
          </p>
        </a>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Courses',
    setup() {
      const courses = [
        {
          code: 'CSE 305',
          name: 'Computer Architecture',
          topics: ['Information and Instructions Representation', 'Processor and Control Unit Design', 'Memory', 'Cache', 'Multiprocessors'],
          link: 'https://cse.buet.ac.bd/academics/course_detail/CSE305'
        },
        {
          code: 'CSE 423',
          name: 'Fault Tolerance System',
          topics: ["Fault Tolerant Systems", "Fault Detection", "Automatic Test Pattern Generator", "Fault Modeling", "Triple Modular Redundancy", "Memory Testing"],
          link: 'https://cse.buet.ac.bd/academics/course_detail/CSE423'
        },
        {
          code: 'CSE 321',
          name: 'Computer Networks',
          topics: ['Transport Protocols', 'Routing Algorithm', 'Congestion Control', 'Domain Name Systems', 'Cryptography', 'Authentication', 'Digital Signatures'],
          link: 'https://cse.buet.ac.bd/academics/course_detail/CSE321'
        },
        {
          code: 'CSE 463',
          name: 'Software Development',
          topics: ['Making software on some practical problems with sound software engineering practices'],
          link: '/courses/cse463'
        },
        {
          code: 'CSE 471',
          name: 'Machine Learning',
          topics: ['Supervised', 'Unsupervised', 'Reinforcement Learning', 'Neural Networks', 'Deep Learning', 'Convolutional Neural Networks'],
          link: 'https://cse.buet.ac.bd/academics/course_detail/CSE471'
        },
        {
          code: 'CSE 409',
          name: 'Computer Graphics',
          topics: ['Raster graphics', '3D Modeling and Rendering', 'Transformations', 'Illumination', 'Shading and Textures'],
          link: 'https://cse.buet.ac.bd/academics/course_detail/CSE409'
        },
        {
          code: 'CSE 461',
          name: 'Algorithm Engineering',
          topics: ['Computational Complexity', 'Algorithms for Combinatorial Optimization', 'Approximation Algorithms', 'Randomized Algorithms'],
          link: 'https://cse.buet.ac.bd/academics/course_detail/CSE461'
        },
        {
          code: 'MATH 247',
          name: 'Linear Algebra',
          topics: ['Gaussian elimination', 'Euclidean n-space', 'Linear transformations', 'Laplace Transform & Fourier Analysis'],
          link: 'https://cse.buet.ac.bd/academics/course_detail/MATH247'
        },
        {
          code: 'CSE 313',
          name: 'Operating System',
          topics: ['Process', 'Inter-Process Communication', 'Scheduling', 'Memory Management', 'Input/Output', 'File Systems'],
          link: 'https://cse.buet.ac.bd/academics/course_detail/CSE313'
        },
        {
          code: 'MATH 145',
          name: 'Calculus',
          topics: ['Differential Calculus', 'Integral Calculus', 'Ordinary Differential Equations'],
          link: 'https://cse.buet.ac.bd/academics/course_detail/MATH141'
        },
        {
          code: 'CSE 405',
          name: 'Computer Security',
          topics: ['Cryptography', 'Applications Security', 'Network Security', 'Security Attacks', 'Security Measures'],
          link: 'https://cse.buet.ac.bd/academics/course_detail/CSE405'
        },
        {
          code: 'HUM 477',
          name: 'Sociology for Science and Technology',
          topics: ['Social Research Methods', 'Social Impact Assessment', 'Globalization'],
          link: 'https://cse.buet.ac.bd/academics/course_detail/HUM477'
        }
      ]
  
      return {
        courses
      }
    }
  }
  </script>
  
  <style scoped>
  /* Optional: Add hover effect for course cards */
  a:hover {
    text-decoration: none;
    transform: translateY(-2px);
    transition: transform 0.2s ease-in-out;
  }
  </style>