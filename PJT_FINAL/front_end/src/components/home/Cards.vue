<template>
  <div>
    <img id="cardFilm" alt="Vue logo" :src="link_url" />
    <img id="cardFilm" alt="Vue logo" :src="link_url2" />
  </div>
</template>

<script>
export default {
  name: "IndexCard",
  data() {
    return {
        link_url: `https://image.tmdb.org/t/p/original/${this.topmovie}`,
        link_url2: `https://image.tmdb.org/t/p/original/${this.popularmovies}`,
    };
  },
  props:{
    topmovie:String,
    popularmovies : String
  },

};
</script>

<style>
</style>