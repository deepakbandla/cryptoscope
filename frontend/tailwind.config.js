/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Academic monochrome palette
        zinc: {
          850: '#202024',
          900: '#18181b',
        }
      }
    },
  },
  plugins: [],
}