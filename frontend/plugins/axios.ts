import { defineNuxtPlugin } from '#app'
import axios from 'axios'

export default defineNuxtPlugin((nuxtApp) => {
  const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
  })

  nuxtApp.provide('axios', axiosInstance)
})
