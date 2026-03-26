import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  // Root base path for user site deployment: https://saimon7g.github.io
  base: '/',
})