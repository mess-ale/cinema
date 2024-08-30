<template>
    <Cover text="Movies"/>
    
    <div class="moviediv">
    <Movies :movies="movies" base_url="1" />
    </div>
</template>

<script>
import Cover from '~/components/Cover.vue'
import Movies from '~/components/Movies.vue'
import { ref, onMounted } from 'vue'
import { useNuxtApp } from '#app'

export default {
  components: {
    Cover,
    Movies
  },
  setup() {
    const movies = ref([])
    const { $axios } = useNuxtApp()
    
    onMounted(async () => {
      try {
        const responsemovies = await $axios.get('/api/movie/')
        movies.value = responsemovies.data
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    })

    return {
      movies
    }
  }
}
</script>


<style scoped>
.moviediv {
    padding: 1rem 11.25rem;
}
</style>