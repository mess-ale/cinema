<template>
  <div class="text-white pb-8">
    <div class="moviePoster"
      :style="{ height: `33rem`, backgroundSize: 'cover', backgroundImage: `url(${picture_src})`, borderRadius: '1rem' }">
      <div class="pl-8 pb-12">
        <h1 class="text-6xl font-bold text-shadow">{{ title }}</h1>
        <h3 class="text-xl font-bold pb-8 text-shadow">{{ time }} | {{ genre }} | {{ director }}</h3>


        <button v-if="get === 'get tickets'"
          class="text-capital rounded-3xl flex items-center bg-secondary pl-5 pr-5 pt-3 pb-3"><nuxt-link
            to="/gettickets">{{ get }}</nuxt-link></button>

        <div v-else class="flex space-x-4">
          <button class="text-capital rounded-3xl flex items-center bg-secondary pl-5 pr-5 pt-3 pb-3">Trailer</button>
          <button class="text-capital rounded-3xl flex items-center bg-primary pl-5 pr-5 pt-3 pb-3">{{ get }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    director: {
      type: String,
      required: true
    },
    genre: {
      type: String,
      required: true
    },
    time: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    get: {
      type: String,
      required: true
    },
    picture_src: {
      type: String,
      required: true
    }
  }
};
</script>

<style scoped>
.moviePoster {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.text-shadow {
  text-shadow: 1px 1px 2px black, 0 0 1em black, 0 0 0.2em black;
}

.text-capital {
  text-transform: capitalize;
}
</style>
