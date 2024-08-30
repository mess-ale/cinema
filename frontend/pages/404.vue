<template>
    <Cover :taxt="error.statuscode" />
    <div class="error-page">
      <h1 class="error-code">404</h1>
      <p class="error-message">Sorry we can’t find that page!</p>
      <p class="error-description">The page you are looking for was never existed.</p>
      
      <div class="search-box">
        <input type="text" placeholder="Search ..." class="search-input"/>
        <button class="search-button">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="search-icon">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 1114 0 7 7 0 01-14 0z" />
          </svg>
        </button>
      </div>
      
      <button class="home-button" @click="goHome">Back to Home</button>
    </div>
  </template>
  
  <script>
  defineProps(['error'])
  export default {
    methods: {
      goHome() {
        this.$router.push('/');
      }
    }
  }
  </script>
  
  <style scoped>
  .error-page {
    text-align: center;
    margin: 0 auto;
    padding: 50px;
    max-width: 500px;
    color: #333;
  }
  
  .error-code {
    font-size: 100px;
    color: #F97316; /* Orange color */
    font-weight: bold;
  }
  
  .error-message {
    font-size: 24px;
    margin-top: 10px;
    font-weight: bold;
  }
  
  .error-description {
    color: #888;
    margin-top: 10px;
  }
  
  .search-box {
    margin-top: 20px;
    position: relative;
  }
  
  .search-input {
    width: 100%;
    padding: 10px;
    padding-right: 40px;
    border-radius: 5px;
    border: 1px solid #ccc;
    box-sizing: border-box;
  }
  
  .search-button {
    position: absolute;
    right: 0;
    top: 0;
    bottom: 0;
    background-color: transparent;
    border: none;
    padding: 0 10px;
    cursor: pointer;
  }
  
  .search-icon {
    width: 20px;
    height: 20px;
    color: #888;
  }
  
  .home-button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #F97316; /* Orange color */
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .home-button:hover {
    background-color: #EA580C; /* Darker Orange */
  }
  </style>
  