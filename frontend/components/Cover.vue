<template>
    <div class="cover">
        <div class="text">
            <h1 class="font-bold text-4xl">{{ text }}</h1>
        </div>
    </div>
    <img src="../static/images/image-lines-header.jpg" class="pt-3 pb-12" alt="line header" />
</template>

<script>
export default {
    props: {
        text: {
            type: String,
            required: true
        }
    }
};
</script>

<style scoped>
.cover {
    background-image: url('../static/images/cover.jpg');
    height: 33rem;
    display: flex;
    align-items: center;
    background-size: cover;
    background-position: center;
}

.text {
    width: 100%;
    display: flex;
    text-align: center;
    justify-content: center;
}
</style>