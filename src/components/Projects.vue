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
        name: "StayNest - Property Rental Platform",
        organization: "Full Stack Development Project",
        description: "Built a comprehensive property rental platform with Next.js and Django, featuring sophisticated booking management, price negotiation, and meal planning systems. Implemented multi-step property registration, real-time availability tracking, and role-based access control. Features include interactive map integration, meal package customization, price negotiation system, and secure payment processing. Utilized microservices architecture with separate services for property management, bookings, and negotiations.",
        tech: "Next.js, Django REST Framework, PostgreSQL, Tailwind CSS, MapTiler SDK, AWS",
        github: "https://github.com/saimon7g/StayNest-BackEnd",
      },
      {
        name: "Bangla Image Caption Generator",
        organization: "Machine Learning Sessional",
        description: "Developed a Bangla image caption generator using CNN-LSTM architecture with TensorFlow and Keras. Trained on custom Bangla image-caption dataset with 47k+ images and captions. Implemented image preprocessing with OpenCV, feature extraction with pre-trained VGG16, and caption generation with LSTM. Achieved BLEU score of 0.75+ with beam search decoding and attention mechanism. Features include real-time image captioning, interactive caption editing, and custom dataset creation.",
        tech: "Python, TensorFlow, Keras, OpenCV, VGG16, LSTM, BLEU Score",
        github: "https://github.com/saimon7g/CSE-102-Project",
      },
      {
        name: "Mini C Compiler",
        organization: "Compiler Sessional",
        description: "Developed a compiler for a subset of C programming language through a series of modular components. Built a robust symbol table using custom hash implementation and scope management. Created lexical analyzer with Flex for token recognition and error detection. Implemented syntax & semantic analyzer using Bison with comprehensive type checking and validation. Generated optimized 8086 assembly code with stack-based memory management, peephole optimizations, and support for control structures and function calls. Features include detailed error reporting, scope analysis, and integrated println function.",
        tech: "C++, Flex, Bison, YACC, 8086 Assembly",
        github: "https://github.com/saimon7g/CSE-310-Compiler-Design"  // Replace with your repo link
      },
      {
        name: "Railway E-Ticket Reservation System",
        organization: "Database Design Project",
        description: "Designed and implemented a comprehensive railway reservation database system with Django and Oracle. Created complex database architecture including transaction management, real-time seat availability tracking, and automated reservation timeout triggers. Implemented intricate SQL queries for station-to-station fare calculation, multi-class seat management, and booking validations. Features include secure user authentication, interactive seat selection, and integrated payment verification system.",
        tech: "Oracle Database, Django, Python, SQL, PL/SQL Triggers",
        github: "https://github.com/saimon7g/Railway-Ticket"  // Add your actual repo link
      },
      {
        name: "Football Transfer Market System",
        organization: "Object Oriented Programming Sessional",
        description: "Built a real-time football transfer market system with multi-club support using socket programming. Implemented features like club-based authentication, live player trading between multiple clubs, market monitoring, and club analytics. Designed with multi-threaded server to handle concurrent club connections and JavaFX-based responsive UI.",
        tech: "Java, JavaFX, Socket Programming, Multi-threading, File I/O",
        github: "https://github.com/saimon7g/CSE-108-Project"  // Add your actual repo link here
      },
      {
        name: "DX-ball Game Recreation",
        organization: "Structured Programming Language Sessional",
        description: "Recreated classic DX-ball game using OpenGL and iGraphics. Implemented complex collision, power-ups (fireball, paddle modifications), 4-level system with unique patterns, and save/load functionality. Features include progressive difficulty, multi-ball system, and high score tracking. Used struct-based object management, timer-based animations, and binary file I/O for game state persistence.",
        tech: "C, OpenGL, iGraphics Library",
        github: "https://github.com/saimon7g/CSE-102-Project", // Add your actual GitHub repo link here
      },




      // {
      //   name: "StayNest - Property Rental Platform",
      //   organization: "Full Stack Development Project",
      //   description: "Engineered a comprehensive property rental platform using Next.js 13+ with App Router and Django microservices. Implemented sophisticated features including: multi-step property registration with dynamic form validation and image optimization; real-time booking system with concurrent session handling and timeout management; price negotiation system using WebSocket for live updates; map integration with custom clustering and geocoding; role-based authentication with JWT and refresh token mechanism. Frontend utilizes SSR for SEO, lazy-loaded components, and optimized image delivery through CloudFront CDN. Backend architecture comprises four microservices (Host, Guest, API Gateway, Negotiation) with PostgreSQL database featuring complex triggers for booking validation and availability tracking. Integrated MapTiler SDK for location services, implemented custom caching layer for API responses, and achieved 90+ Lighthouse performance score through strategic code splitting and API response optimization. Deployed on AWS using EC2 for application hosting, S3 for media storage, and RDS for database management, with automated CI/CD through GitHub Actions.",
      //   tech: "Next.js 13+, Django REST Framework, PostgreSQL, Tailwind CSS, WebSocket, JWT, MapTiler SDK, AWS (EC2, S3, CloudFront, RDS)",
      //   github: "https://github.com/yourusername/staynest"
      // },
    ]
    return {
      projects
    }
  }
}
</script>