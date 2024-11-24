<template>
  <div class="bg-white dark:bg-dark-bg p-4 lg:p-6 rounded-lg shadow max-w-6xl mx-auto">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div v-for="cert in certificates" :key="cert.title"
        class="bg-gray-50 dark:bg-gray-800 rounded-lg p-4 hover:shadow-lg transition-shadow">
        <div class="flex flex-col h-full">
          <h3 class="text-lg font-semibold mb-2 text-primary dark:text-dark-text">
            {{ cert.title }}
          </h3>
          <p class="text-sm text-gray-600 dark:text-gray-300 mb-2">
            {{ cert.issuer }}
          </p>
          <p class="text-xs text-gray-500 dark:text-gray-400 mb-3">
            Completed: {{ cert.date }}
          </p>
          <p v-if="cert.description" class="text-sm text-gray-600 dark:text-gray-300 mb-4 flex-grow">
            {{ cert.description }}
          </p>
          <div class="flex items-center space-x-3">
            <a :href="cert.verify" target="_blank"
              class="text-sm text-blue-600 hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-300 flex items-center">
              <i class="fas fa-certificate mr-1"></i>
              View Credentials
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Certificates',
  data() {
    return {
      certificates: [
        {
          title: 'Machine Learning Specialization',
          issuer: 'DeepLearning.AI and Stanford University',
          date: 'November 10, 2024',
          description: 'Completed comprehensive specialization covering supervised learning (linear regression, logistic regression, neural networks, decision trees), unsupervised learning (clustering, anomaly detection), recommender systems, and reinforcement learning.',
          verify: 'https://coursera.org/verify/specialization/VSIN2UWLN846'
        },
        {
          title: 'Supervised Machine Learning: Regression and Classification',
          issuer: 'DeepLearning.AI and Stanford University',
          date: 'September 8, 2024',
          verify: 'https://coursera.org/verify/CYWXRZOAD04O'
        },
        {
          title: 'Advanced Learning Algorithms',
          issuer: 'DeepLearning.AI and Stanford University',
          date: 'October 5, 2024',
          verify: 'https://coursera.org/verify/ITXLHSSVX4UZ'
        },
        {
          title: 'Unsupervised Learning, Recommenders, Reinforcement Learning',
          issuer: 'DeepLearning.AI and Stanford University',
          date: 'November 10, 2024',
          verify: 'https://coursera.org/verify/I2251WV4JB9X'
        }
      ]
    }
  }
}
</script>