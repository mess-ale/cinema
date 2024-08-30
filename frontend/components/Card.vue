<template>
  <div class="card">
    <div class="text-container">
      <h1 class="text-md text-gray-400">{{ text2 }}</h1>
      <h1 class="font-bold text-4xl">{{ text1 }}</h1>
    </div>
    <div class="icon-container">
      <img :src="icon" />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    text1: {
      type: String,
      required: true
    },
    text2: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      required: true
    },
  }
};
</script>

<style scoped>
.icon-container {
  border-radius: 50%;
  background-color: theme('colors.primary');
  padding: 1rem;
}

.card:hover {
  transform: scale(1.05);
}

.card-content {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  background: rgba(0,
      0, 0, 0.5);
}


.card {
  display: flex;
  padding: 1rem;
  background-image: url('../static/images/cinema.png');
  justify-content: space-around;
  height: 14rem;
  align-items: center;
  background-size: cover;
  background-position: center;
  color: #fff;
  position: relative;
  transition: transform 0.2s ease-in-out;
}

.text-container {
  width: 60%;
  color: #fff;
}
</style>