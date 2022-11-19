<template>
  <div>
    <img id="cardFilm" alt="Vue logo" :src="link_url" />
  </div>
</template>

<script>
export default {
  name: "IndexCard",
  data() {
    return {
        link_url: `https://image.tmdb.org/t/p/original/${this.topmovie}`,
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