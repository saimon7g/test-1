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
    
        <!-- Projects Section -->
        <div class="mt-8">
            <h4 class="text-xl lg:text-2xl font-bold mb-6 text-center text-primary dark:text-dark-text">Projects</h4>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 lg:gap-6">
                <div v-for="(project, idx) in projects" :key="idx"
                    class="p-4 rounded-lg border border-secondary/20 dark:border-dark-text-secondary/20 hover:shadow-md transition-shadow bg-white dark:bg-dark-bg-secondary h-full">
                    <h5 class="font-bold text-lg mb-2 text-primary dark:text-dark-text">{{ project.name }}</h5>
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
    </div>
    </template>
    
    <script>
    export default {
        name: 'Experience',
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
                projects,
                workplaces
            }
        }
    }
    </script>