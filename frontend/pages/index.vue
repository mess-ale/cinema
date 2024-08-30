<template>
  <div>
    <SwitchingStacks />
    <img src="../static/images/image-lines-header.jpg" class="pt-3 pb-12" alt="line header" />

    <div class="cardcompo grid grid-cols-3 gap-5">
      <Card text1="Upcoming Film Festivals" text2="Join Now" icon="/_nuxt/static/images/cardicon2.png" />
      <Card text1="Watch Film Awards" text2="Watch Now" icon="/_nuxt/static/images/cardicon1.png" />
      <Card text1="Comedy TV Shows" text2="Get Ticket" icon="/_nuxt/static/images/cardicon3.png" />
    </div>

    <div class="element-selector">
      <div class="text-center space-y-3 pb-10">
        <div class="centerdiv"> <img src="../static/images/movie.png" class=" w-12 h-12" />
        </div>
        <h1 class="text-xl text-gray-600">Watch New Movies</h1>
        <h1 class="movieplaying text-secondary font-bold"> Movies Now Playing</h1>
      </div>

      <NowPlaying />
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
.cardcompo {
  padding: 1rem 4rem;
}

.element-selector {
  margin: 8rem 10rem;
}

.centerdiv {
  display: flex;
  justify-content: center;
  align-items: center;
}
.movieplaying {
  font-size: 4rem;
}
</style>