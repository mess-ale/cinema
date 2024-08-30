<template>
  <Cover text="Movie Detail" />
  <div class="movie-detail text-black">
    <div class="flex justify-between items-center">
      <div>
        <h2 class="text-3xl font-bold">{{ movie.title }}</h2>
        <p class="text-sm text-gray-600">{{ movie.genre_name }} / {{ movie.duration }} Mins</p>
      </div>
      <button class="button-movie" @click="openModal(id)">GET TICKETS</button>
    </div>
    <div class="flex gap-8 mt-5">
      <div class="image1 w-2/6">
        <img :src="`http://127.0.0.1:8000/media/${movie.featured_image}`" alt="Movie Poster"
          class="h-full w-full object-cover" />
      </div>
      <div class="image2 w-4/6">
        <img :src="`http://127.0.0.1:8000/media/${movie.featured_image}`" alt="Scene Image"
          class="h-full w-full object-cover" />
      </div>
    </div>



    <div class="mt-4">
      <div class="flex justify-between text-sm text-gray-600 mt-3 mb-3">
        <p><span class="font-semibold text-xl">Director:</span> {{ movie.director_name }}</p>
        <MovieRating />
      </div>
    </div>

    <div class="pt-3 pb-3 storyclass">
      <h1 class="text-4xl font-bold ">Story Line</h1>
      <p class="story-desc">{{ movie.description }}</p>
    </div>

    <ShowtimesTable />

    <TicketModal v-if="isModalOpen" :id="selectedMovieId" @close="closeModal" />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useNuxtApp } from '#app';
import { useRoute } from 'vue-router';

export default {
  setup() {
    const movie = ref({});
    const { $axios } = useNuxtApp();
    const route = useRoute();
    const id = route.params.id;

    const fetchMovies = async () => {
      try {
        const response = await $axios.get(`/api/movies/${id}/`);
        movie.value = response.data[0];
        console.log(movie);
      } catch (error) {
        console.error('Error fetching movies:', error);
      }
    };

    onMounted(async () => {
      await fetchMovies();
    });

    return {
      movie,
      id
    };
  },

  data() {
    return {
      isModalOpen: false,
      selectedMovieId: null
    };
  },
  methods: {
    openModal(movieId) {
      this.selectedMovieId = movieId;
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
      this.selectedMovieId = null;
    },
  }
};
</script>

<style>
.movie-detail {
  padding: 1rem 11.25rem;
}

.carousel-container {
  position: relative;
  overflow: hidden;
  width: 100%;
}

.carousel-item {
  flex: 0 0 25%;
  box-sizing: border-box;
  padding: 10px;
  height: 28rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background-size: cover;
  background-position: center;
  padding: 2rem;
  transition: box-shadow 0.5s ease-in-out;
}

.button-movie {
  background-color: theme('colors.primary');
  color: theme('colors.background');
  padding: 15px 40px;
  font-size: 1rem;
  border: none;
  border-radius: 1px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.button-movie:hover {
  background-color: theme('colors.background');
  color: theme('colors.primary');
  border: 1px solid theme('colors.primary');
}

.storyclass {
  border-top: 1px solid #000;
}

.story-desc {
  line-height: 2;
  font-weight: 50;
  font-size: medium;
}
</style>
