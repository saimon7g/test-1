<template>
    <div class="bg-white dark:bg-dark-bg p-4 lg:p-6 rounded-lg shadow max-w-6xl mx-auto">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 lg:gap-6">
        <div v-for="(project, idx) in projects" :key="idx"
          class="p-4 rounded-lg border border-secondary/20 dark:border-dark-text-secondary/20 hover:shadow-md transition-shadow bg-white dark:bg-dark-bg-secondary h-full">
          <h5 class="font-bold text-lg mb-2 text-primary dark:text-dark-text">{{ project.name }}</h5>
          <p class="text-sm mb-2 text-secondary dark:text-dark-text-secondary">
            <span class="font-medium">Organization:</span>
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
          name: "Chatbot for Hospitality System",
          organization: "BMQAS",
          description: "Designed and implemented a chatbot with microservice architecture. Used redis to optimiza chat history for 1 hour. Used ChatGPT's api along with RAG to to implement localized responses.",
          tech: "GPT-3.5-Turbo API, Langchain, Redis, Pinecone Vector DB, RAG"
        },
        {
          name: "APTITUDO",
          organization: "CNS",
          description: "Contributed in the frontend of employee assessment system. Implemented front-end logics and integrated apis with the backend team.",
          tech: "VueJS"
        },
        {
          name: "Business Intelligence",
          organization: "CNS",
          description: "Designed and developed the backend of the BI Software. Major contribution includes developing the pipeline for finetuing and replacing ML models.",
          tech: "Django, Scikit Learn, MySQL"
        },
        {
          name: "Call Center",
          organization: "CNS",
          description: "Migrated the whole project from Laravel backend to Spring backend. Looked deeply how the ORM in Laravel worked with the DB and updated the backend of Spring accordingly.",
          tech: "Spring, Java, Laravel, PHP, MySQL"
        },
        {
          name: "MVTAX",
          organization: "CNS",
          description: "Collaborated with the frontend team to implement the designs for Bangladesh Road Transport Authority Payment Module. Contributed in complicated frontend logics with the backend team.",
          tech: "AngularJS, Javascript"
        },
        {
          name: "AODoubleClick",
          organization: "AODoubleClick",
          description: "Designed and implemented the vendor portal, employee management and contributed in Stripe API integration with the application. Upgraded the project framework, frontend framework, javascript version, PHP version and ORM version.",
          tech: "Symfony, VueJS, Doctrine, MySQL"
        },
        {
          name: "Tour Carnival - Medical",
          organization: "Self Project",
          description: "A doctor directory website to collect appointments and records of the old patients. Worked on the frontend and collaborated with the backend with one more member. Also contributed in deployment on AWS",
          tech: "Spring, NextJS, MySQL, AWS",
        },
      ]
  
      return {
        projects
      }
    }
  }
  </script>