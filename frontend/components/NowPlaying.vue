<template>
    <div class="carousel-container text-white">
        <div class="carousel-track space-x-7" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
            <div class="carousel-item" v-for="movie in movies" :key="movie.id"
                :style="{ backgroundImage: `url(${movie.featured_image})` }" @click="openmovie(movie.id)">
                <h1>{{ movie.genre.name }} / {{ movie.duration }} mins</h1>
                <h1 class="font-bold text-xl">{{ movie.title }}</h1>
                <span>
                    <button class="get-tickets-button nowPlayingbutton" @click.stop="openModal(movie.id)">Get Ticket</button>
                </span>
            </div>
        </div>

        <div class="carousel-dots">
            <span v-for="(dot, index) in totalSlides" :key="index" :class="{ 'active-dot': index === currentIndex }"
                @click="setSlide(index)">
            </span>
        </div>

        <TicketModal v-if="isModalOpen" :id="selectedMovieId" @close="closeModal" />
    </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { useNuxtApp } from '#app'

export default {
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
    },
    setup() {
        const movies = ref([])
        const currentIndex = ref(0)
        const moviesPerSlide = 4

        const fetchMovies = async () => {
            try {
                const { $axios } = useNuxtApp()
                const response = await $axios.get('/api/nowplaying-movies/')
                movies.value = response.data
            } catch (error) {
                console.error('Error fetching movies:', error)
            }
        }

        onMounted(fetchMovies)

        const totalSlides = computed(() => Math.ceil(movies.value.length / moviesPerSlide))

        const setSlide = (index) => {
            currentIndex.value = index
        }

        return {
            movies,
            currentIndex,
            totalSlides,
            setSlide
        }
    }
}
</script>

<style scoped>
.nowplaying {
    height: 30rem;
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
    cursor: pointer;
    justify-content: flex-end;
    background-size: cover;
    background-position: center;
    padding: 2rem;
    transition: box-shadow 0.3s ease-in-out;
}

.carousel-item:hover {
    box-shadow: inset 0 0 0 5px theme('colors.primary');
}

.carousel-item::after {
    transition: box-shadow 0.3s ease-in-out;
}

.carousel-item:hover .get-tickets-button {
    background-color: theme('colors.primary');
    animation-duration: 2s;
    transition: background-color 0.3s ease-in-out;
    color: #fff;
}

.carousel-track {
    display: flex;
}

.movie-info {
    margin-top: 10px;
}

.carousel-dots {
    display: flex;
    justify-content: center;
    padding-top: 1rem;
    gap: 8px;
}

.carousel-dots span {
    width: 10px;
    height: 10px;
    background-color: #f6d1bb;
    border-radius: 50%;
    cursor: pointer;
    transition: background-color 0.3s;
}

.carousel-dots .active-dot {
    background-color: theme('colors.primary');
}

.get-tickets-button {
    color: theme('colors.secondary');
    background-color: #fff;
}

.nowPlayingbutton {
    font-size: 0.8rem;
    border-radius: 2px;
}
</style>
