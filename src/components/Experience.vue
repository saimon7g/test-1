<template>
    <div class="max-w-6xl mx-auto h-full overflow-y-auto main-content">
        <template v-for="(workplace, idx) in workplaces" :key="idx">
            <h3 class="text-xl font-bold mb-2">
                {{ workplace.name }}
            </h3>
            <div class="flex">
                <div class="text-gray-800">
                    <p class="mb-1">{{ workplace.role }}</p>
                </div>
                <div class="flex-1">
                    <p class="text-gray-800 mb-4 text-right italic">{{ workplace.duration }}</p>
                </div>
            </div>
        </template>
        <!-- Notable Courses Section -->
        <div>
            <h4 class="text-xl font-bold mb-6 text-center">Projects</h4>
            <div class="grid grid-cols-2 gap-6">

                <a v-for="(project, idx) in projects" :key="idx"
                    class="p-4 rounded-lg border border-gray-200 hover:shadow-md transition-shadow bg-white flex flex-col h-full min-h-[180px]">
                    <!-- Title at top -->
                    <h5 class="font-bold text-lg mb-2 text-black">{{ project.name }}</h5>

                    <!-- Description takes available space -->
                    <p class="text-sm text-gray-700 leading-relaxed flex-grow">
                        <span>
                            {{ project.description }}
                        </span>
                    </p>

                    <!-- Tech stack pushed to bottom -->
                    <p class="text-sm text-gray-700 mt-auto pt-4">
                        Tech :
                        <span class="italic">
                            {{ project.tech }}
                        </span>
                    </p>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Education',
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

<style scoped>
/* Add some custom transition for the hover effect */
.course-card {
    transition: all 0.2s ease-in-out;
}

.main-content {
    height: 100vh;
    overflow-y: auto;

    /* Hide scrollbar for Chrome, Safari and Opera */
    &::-webkit-scrollbar {
        display: none;
    }

    /* Hide scrollbar for IE, Edge and Firefox */
    -ms-overflow-style: none;
    /* IE and Edge */
    scrollbar-width: none;
    /* Firefox */
}

/* Ensure the body only has one scrollbar */
body {
    overflow: hidden;
}

/* If you want to keep the browser's main scrollbar */
html {
    overflow-y: auto;
}
</style>