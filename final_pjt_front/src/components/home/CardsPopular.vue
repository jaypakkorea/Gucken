<template>
  <div>
    <img id="cardFilm" alt="Vue logo" :src="link_url" />
  </div>
</template>

<script>
export default {
  name: "CardsPopular",
  data() {
    return {
        link_url: `https://image.tmdb.org/t/p/original/${this.popularmovies}`,
    };
  },
  props:{
    popularmovies : String
  },

};
</script>

<style>
</style>