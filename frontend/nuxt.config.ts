// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  modules: ["nuxt-icons", "@nuxtjs/tailwindcss"],
  compatibilityDate: "2024-07-30",
  plugins: ["~/plugins/axios.ts", "~/plugins/fontawesome.js"],
});
