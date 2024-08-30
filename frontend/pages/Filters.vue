<template>
    <Cover text="Filter A Movie"/>
    <div class="filter-container text-white space-y-10">
        <div class="filter flex">
            <div class="flex flex-wrap gap-4">
                <input type="text" placeholder="Search..."
                    class="filter-input p-2 rounded bg-gray-800 border border-gray-700 focus:border-primary focus:ring focus:ring-primary focus:outline-none" />

                <select
                    v-model="genreName"
                    class="filter-select p-2 rounded bg-gray-800 border border-gray-700 focus:border-primary focus:ring focus:ring-primary focus:outline-none">
                    <option value="">Select a genre</option>
                    <option v-for="(genre, index) in genreAndDire.genres" :key="index">
                        {{ genre }}
                    </option>
                </select>

                <select
                    v-model="directorName"
                    class="filter-select p-2 rounded bg-gray-800 border border-gray-700 focus:border-primary focus:ring focus:ring-primary focus:outline-none">
                    <option value="">Select Director</option>
                    <option v-for="(director, index) in genreAndDire.directors" :key="index">{{ director }}</option>
                </select>
            </div>

            <button @click="submitSelections" class="filter-button p-2 rounded get-tickets-button text-white hover:bg-purple-700 transition">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                    class="w-5 h-5 inline-block mr-1">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2a1 1 0 01-.293.707l-6.293 6.293V18a1 1 0 01-.293.707l-2 2A1 1 0 0110 21v-6.293L3.293 6.707A1 1 0 013 6V4z" />
                </svg>
                Filter
            </button>
        </div>

        <div v-if="combinedMovies.length > 0">
            <Movies :movies="combinedMovies" :base_url="false"/>
        </div>
        <div v-else>
            <Movies :movies="movies" :base_url="true" />
        </div>
    </div>
</template>

<script>
import Cover from '~/components/Cover.vue'
import Movies from '~/components/Movies.vue'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useNuxtApp } from '#app'

export default {
  components: {
    Cover,
    Movies
  },
  setup() {
    const movies = ref([])
    const moviesfilter1 = ref([])
    const moviesfilter2 = ref([])
    const genreAndDire = ref([])
    const combinedMovies = ref([])
    const { $axios } = useNuxtApp()
    const router = useRouter()
    const genreName = ref('')
    const directorName = ref('')

    onMounted(async () => {
      try {
        const responsemovies = await $axios.get('/api/movie/')
        movies.value = responsemovies.data
        const responseGenresDirectors = await $axios.get("/api/movies/genres-and-directors/")
        genreAndDire.value = responseGenresDirectors.data
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    })

    const submitSelections = async () => {
      try {
        if (genreName.value) {
          const responsegenre = await $axios.get(`/api/movies/genre/${genreName.value}/`)
          moviesfilter1.value = responsegenre.data
        }
        if (directorName.value) {
          const responsedirect = await $axios.get(`/api/movies/director/${directorName.value}/`)
          moviesfilter2.value = responsedirect.data
        }
        combinedMovies.value = moviesfilter1.value.concat(moviesfilter2.value)
      } catch (error) {
        console.error('Error fetching filtered data:', error)
      }
      
      router.push({
        query: {
          genre: genreName.value,
          director: directorName.value
        }
      })
    }

    return {
      combinedMovies,
      movies,
      genreAndDire,
      directorName,
      genreName,
      submitSelections
    }
  }
}
</script>

<style scoped>
.filter-container {
    width: 100%;
    padding: 1rem 11.25rem;
}

.filter-input,
.filter-select {
    min-width: 150px;
    width: auto;
}

.filter-button {
    display: flex;
    align-items: center;
}

.filter {
    justify-content: space-between;
}
</style>
