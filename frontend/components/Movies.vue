<template>
  <div class="movie-container">
    <div class="movies-grid">      
      <div v-for="(movie, index) in movies" :key="movie.id" class="movie-card" @click="openmovie(movie.id)"
        :style="{ backgroundImage: !base_url ? `url(http://127.0.0.1:8000/media/${movie.featured_image})` :`url(${movie.featured_image})` }">
        <div class="movie-details">
          <h3>{{ movie.title }}</h3>
          <button class="get-tickets-button" @click.stop="openModal(movie.id)">Get Ticket</button>
        </div>
      </div>
    </div>

    <TicketModal v-if="isModalOpen" :id="selectedMovieId" @close="closeModal" />
  </div>
</template>

<script>

export default {
  props: {
    movies: {
      type: Array,  // Should be an array instead of an object
      required: true,
    },
    base_url: {
      type: String,
      required: true
    }
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
    openmovie(movieId) {
      this.$router.push(`/movie/${movieId}`);
    },
  }
}
</script>
<style scoped>
.movies-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 20px;
}

.movie-card {
  cursor: pointer;
  position: relative;
  height: 300px;
  background-size: cover;
  background-position: center;
  border-radius: 8px;
  overflow: hidden;
  transition: box-shadow .3s ease-in-out;
}

.movie-card:hover {
  box-shadow: inset 0 0 0 5px theme('colors.primary');
}

.movie-card::after {
  transition: box-shadow .3s ease-in-out;
}

.get-tickets-button {
  font-size: 1rem;
  margin-top: 10px;
}

.movie-details {
  position: absolute;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  color: #fff;
  width: 100%;
  text-align: center;
  padding: 10px;
}

.movie-details h3 {
  margin: 0;
  font-size: 18px;
}
</style>
