/** @type {import('tailwindcss').Config} */
export default {
    content: [
      "./index.html",
      "./src/**/*.{vue,js,ts,jsx,tsx}",  // This ensures Tailwind scans all your Vue components
    ],
    theme: {
      extend: {
        colors: {
          // You can add custom colors here to match your design
          'primary': '#1a202c',  // dark blue-gray
          'secondary': '#2d3748', // lighter blue-gray
          'accent': '#4299e1',   // blue
        },
        spacing: {
          '72': '18rem',
          '84': '21rem',
          '96': '24rem',
        },
        fontFamily: {
          'sans': ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        },
      },
    },
    plugins: [],
  }