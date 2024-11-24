<template>
  <div class="bg-white dark:bg-dark-bg p-4 lg:p-6 rounded-lg shadow max-w-6xl mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-4 lg:gap-6">
      <a v-for="course in visibleCourses" :key="course.code" :href="course.link"
        class="p-4 rounded-lg border border-secondary/20 dark:border-dark-text-secondary/20 hover:shadow-md transition-all duration-200 bg-white dark:bg-dark-bg-secondary group"
        target="_blank" rel="noopener noreferrer">
        <h5
          class="font-bold text-lg mb-2 text-primary dark:text-dark-text group-hover:text-blue-600 dark:group-hover:text-blue-400">
          {{ course.code }}: {{ course.name }}
        </h5>
        <p class="text-sm text-secondary dark:text-dark-text-secondary leading-relaxed">
          <span v-for="(topic, index) in course.topics" :key="index">
            {{ topic }}<span v-if="index !== course.topics.length - 1">, </span>
          </span>
        </p>
      </a>
    </div>

    <div v-if="courses.length > initialDisplayCount" class="mt-6 flex justify-center">
      <button @click="toggleShowMore"
        class="px-6 py-2 bg-gray-900 dark:bg-gray-700 text-white rounded-md hover:bg-gray-800 dark:hover:bg-gray-600 transition-colors duration-200">
        {{ showAll ? 'Show Less' : 'See More Courses' }}
      </button>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  name: 'Courses',
  setup() {
    const showAll = ref(false)
    const initialDisplayCount = 10

    const courses = [
      {
        code: 'CSE 107',
        name: 'Object Oriented Programming Language',
        topics: ['C++', 'Java', 'Classes and Objects', 'Inheritance', 'Polymorphism', 'Templates', 'Multi-threaded Programming'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE107'
      },
      {
        code: 'CSE 203',
        name: 'Data Structures and Algorithms',
        topics: ['Array', 'Linked List', 'Stack', 'Queue', 'Tree', 'Binary Search Tree', 'Heap', 'Graph', 'Sorting Algorithms', 'Divide and Conquer', 'Greedy Algorithms', 'Dynamic Programming', 'Disjoint Set'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE203'
      },
      {
        code: 'CSE 207',
        name: 'Data Structures and Algorithms II',
        topics: ['AVL Trees', 'Red-Black Trees', 'Splay Trees', 'Skip Lists', 'Fibonacci Heaps', 'Binomial Heaps', 'Hash Tables', 'Graph Algorithms', 'Shortest Path Algorithms', 'Minimum Spanning Tree', 'Maximum Flow', 'String Matching', 'NP-Completeness', 'Approximation Algorithms', 'Backtracking', 'Branch and Bound'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE207'
      },
      {
        code: 'CSE 215',
        name: 'Database',
        topics: ['Relational Database Design', 'SQL', 'Entity Relationship Diagrams', 'Normalization', 'Relational Algebra', 'Indexing and Hashing', 'Query Processing', 'Transaction Management', 'Concurrency Control', 'Data Recovery'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE215'
      },
      {
        code: 'CSE 307',
        name: 'Software Engineering',
        topics: ['Software Engineering Paradigms', 'Project Management', 'Requirements Analysis', 'Design Principles', 'UML', 'Design Patterns', 'Testing Strategies', 'System Maintenance', 'Quality Assurance', 'Cost Analysis', 'Documentation'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE307'
      },
      {
        code: 'CSE 471',
        name: 'Machine Learning',
        topics: ['Supervised Learning', 'Unsupervised Learning', 'Reinforcement Learning', 'Neural Networks', 'Genetic Algorithms', 'Evolutionary Computing', 'Applied ML'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE471'
      },
      {
        code: 'CSE 405',
        name: 'Computer Security',
        topics: ['Cryptography', 'Operating System Security', 'Network Security', 'Application Security', 'Security Attacks', 'Security Measures', 'Digital Signatures', 'Social Engineering'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE405'
      },
      {
        code: 'CSE 317',
        name: 'Artificial Intelligence',
        topics: ['Search Techniques', 'Constraint Satisfaction', 'Game Playing', 'Knowledge Representation', 'Planning', 'Probabilistic Reasoning', 'Machine Learning', 'Expert Systems', 'Natural Language Processing', 'Computer Vision'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE317'
      },
      {
        code: 'CSE 313',
        name: 'Operating System',
        topics: ['Process Management', 'Inter-Process Communication', 'Scheduling', 'Memory Management', 'Virtual Memory', 'Input/Output', 'Deadlock', 'File Systems', 'System Security'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE313'
      },
      {
        code: 'Math Courses',
        name: '',
        topics: ['Calculus', 'Linear Algebra', 'Probability and Statistics', 'Numerical Analysis', 'Fourier Analysis', 'Ordinary and Partial Differential Equations', 'Vector Calculus', 'Complex Variables', 'Coordinate Geometry', 'Laplacian Transform',],
        link: 'https://math.buet.ac.bd/'
      },




      {
        code: 'CSE 211',
        name: 'Theory of Computation',
        topics: ['Regular Languages', 'Regular Expressions', 'Finite Automata', 'Context-free Grammars', 'Pushdown Automata', 'Turing Machines', 'Computability', 'Complexity Theory', 'Time and Space Complexity'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE211'
      },
      {
        code: 'CSE 309',
        name: 'Compilers',
        topics: ['Introduction to Compiling', 'Lexical Analysis', 'Syntax Analysis', 'Syntax-Directed Translation', 'Semantic Analysis', 'Type Checking', 'Run-time Environments', 'Intermediate Code Generation', 'Code Generation', 'Machine-Independent Optimizations'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE309'
      },
      {
        code: 'CSE 321',
        name: 'Computer Networks',
        topics: ['Protocol Hierarchies', 'Data Link Layer', 'LAN Protocols', 'Routing Algorithms', 'IP Addressing', 'Transport Layer', 'Congestion Control', 'Domain Name Systems', 'Network Security', 'IoT Networks'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE321'
      },

      {
        code: 'CSE 409',
        name: 'Computer Graphics',
        topics: ['Raster Graphics', '3D Modeling', 'Transformations', 'Ray Tracing', 'Hidden Surface Removal', 'Illumination', 'Shading and Textures', 'Computer Animation', 'Fractals'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE409'
      },
      {
        code: 'CSE 103',
        name: 'Discrete Mathematics',
        topics: ['Set Theory', 'Relations and Functions', 'Propositional and Predicate Calculus', 'Mathematical Reasoning and Proofs', 'Combinatorics', 'Discrete Probability', 'Recurrence Relations', 'Graph Theory', 'Algebraic Structures'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE103'
      },
      {
        code: 'CSE 301',
        name: 'Mathematical Analysis for Computer Science',
        topics: ['Recurrent Problems', 'Number Theory', 'Generating Functions', 'Random Variables', 'Stochastic Process', 'Markov Chains', 'Queuing Models', 'Birth-Death Process'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE301'
      },
      {
        code: 'CSE 421',
        name: 'Basic Graph Theory',
        topics: ['Graph Fundamentals', 'Trees', 'Graph Connectivity', 'Euler Tours', 'Hamilton Cycles', 'Graph Coloring', 'Planar Graphs', 'Graph Problems'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE421'
      },
      {
        code: 'CSE 461',
        name: 'Algorithm Engineering',
        topics: ['Computational Complexity', 'Parameterized Complexity', 'Combinatorial Optimization', 'Approximation Algorithms', 'Randomized Algorithms', 'Experimental Algorithms', 'Applied Algorithms'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE461'
      },
      {
        code: 'CSE 305',
        name: 'Computer Architecture',
        topics: ['Information Representation', 'Performance Measurement', 'Instruction Set Architecture', 'ALU Design', 'Processor Design', 'Control Unit Design', 'Pipelining', 'Hazards and Exceptions', 'Memory Hierarchy', 'Cache Memory', 'Virtual Memory', 'DMA and Interrupts', 'Bus Architecture', 'Multiprocessors'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE305'
      },
      {
        code: 'CSE 325',
        name: 'Information System Design',
        topics: ['System Analysis', 'Project Management', 'Requirements Analysis', 'Information Gathering', 'Agile Modeling', 'Data Flow Diagrams', 'UML', 'Database Design', 'UI/UX Design', 'Quality Assurance', 'Implementation'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE325'
      },
      {
        code: 'CSE 463',
        name: 'Introduction to Bioinformatics',
        topics: ['Molecular Biology', 'Sequence Alignment', 'Gene Prediction', 'Genome Assembly', 'Pattern Matching', 'Expression Analysis', 'Phylogenetics', 'Machine Learning'],
        link: 'https://cse.buet.ac.bd/academics/course_detail/CSE463'
      },
      {
        code: 'Other CS Courses',
        name: '',
        topics: ['Structured Programming Language', 'Digital Logic Design', 'Numerical Methods', 'Microprocessor Microcontroller and Embedded Systems', 'Data Communication',],
        link: 'https://cse.buet.ac.bd/academics/undergraduate-courses'

      },
    ]
    const visibleCourses = computed(() => {
      return showAll.value ? courses : courses.slice(0, initialDisplayCount)
    })

    const toggleShowMore = () => {
      showAll.value = !showAll.value
    }
    return {
      courses,
      visibleCourses,
      showAll,
      initialDisplayCount,
      toggleShowMore
    }
  }
}
</script>

<style scoped>
a {
  text-decoration: none;
  transform: translateY(0);
  transition: all 0.2s ease-in-out;
}

a:hover {
  transform: translateY(-2px);
}
</style>