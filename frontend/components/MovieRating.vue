<template>
  <div>
    <div class="stars">
      <span v-for="index in 10" :key="index" :class="{ 'filled': index <= rating }" @click="setRating(index)"
        @mouseover="hoverRating(index)" @mouseleave="hoverRating(0)">
        ★
      </span>
    </div>
    <p>Your Rating: {{ rating }}</p>
    <p>Average Rating: 87 / 10 ( ratings)</p>
  </div>
</template>

<script>
export default {
  name: 'MovieRating',
  data() {
    return {
      rating: 0,
      hover: 0
    }
  },
  methods: {
    setRating(index) {
      this.rating = index;
    },
    hoverRating(index) {
      this.hover = index;
    }
  }
}
</script>

<style scoped>
.stars {
  display: flex;
}

.stars span {
  font-size: 2em;
  cursor: pointer;
  color: lightgray;
}

.stars .filled {
  color: theme('colors.primary');
}
</style>