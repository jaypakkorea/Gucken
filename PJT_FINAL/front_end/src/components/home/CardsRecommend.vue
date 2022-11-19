<template>
    <div>
      <img id="cardFilm" alt="Vue logo" :src="link_url" />
    </div>
  </template>
  
  <script>
  export default {
    name: "CardsRecommend",
    data() {
      return {
          link_url: `https://image.tmdb.org/t/p/original/${this.recommendmovie}`,
      };
    },
    props:{
        recommendmovie : String
    },
  
  };
  </script>
  
  <style>
  </style>