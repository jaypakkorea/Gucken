<template>
  <div>
    <carousel-3d :controls-visible="true" :autoplay="true" :autoplay-timeout="1500"  :controls-prev-html="'&#10092; '" :controls-next-html="'&#10093;'" :controls-width="30" :controls-height="60" :clickable="false"  :width="500" :height="750" class="carousel">
      <slide v-for="(recommendmovie, index) in recommendmovies" :key="recommendmovie" :index="index">
        <router-link :to="{ name: 'SearchDetailView', params: { moviePk: recommendmovie.pk } }">
        <ChartRecommendCard :recommendmovie="recommendmovie" />
        </router-link>
      </slide>
    </carousel-3d>
    <div>
    </div>
  </div>
  
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";
import ChartRecommendCard from './cardImg.vue'
export default {
  name: "LankIndexCard",
  data() {
    return {
      link_url: `https://image.tmdb.org/t/p/original/${this.recommendmovies}`,

      };
  },
  props:{
    recommendmovies:Array
  },
  components: {
    Carousel3d,
    Slide,
    ChartRecommendCard
  },

};
</script>

<style>

#app > div > div > div.LankCardDiv > div > div > div.carousel-3d-container.carousel > div.carousel-3d-slider > div.carousel-3d-slide

{
  background-color: transparent;
}
</style>