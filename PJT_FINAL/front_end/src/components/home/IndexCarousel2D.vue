<template>
  <div class="carousel2D">
    <div class="CardTitle">Best Rating</div>
    <carousel
      :loop="true"
      v-bind:autoplay="true"
      :per-page="6"
      :mouse-drag="true"
      speed="3000"
      autoplay-timeout="5000"
      id="carousel2Dcontent"
      style="transition: transform 0.5s ease 0s"
    >
      <slide
        v-for="(topmovie, index) in topmovies"
        :key="topmovie.id"
        :index="index"
      >
        <router-link
        :to="{ name: 'SearchDetailView', params: { moviePk: topmovie.id } }">
          <IndexCard :topmovie="topmovie.poster_path" />
        </router-link>
      </slide>
    </carousel>
    <div class="CardTitle2">Recommend</div>
    <carousel
      :loop="true"
      v-bind:autoplay="true"
      speed="3000"
      autoplay-timeout="5000"
      :per-page="6"
      :mouse-drag="true"
      id="carousel2Dcontent"
    >
      <slide :index="0"><IndexCard /></slide>
      <slide :index="1"
        ><img id="cardFilm" alt="Vue logo" src="../../assets/starisborn.jpg"
      /></slide>
      <slide :index="2"
        ><img id="cardFilm" alt="Vue logo" src="../../assets/starisborn.jpg"
      /></slide>
      <slide :index="3"
        ><img id="cardFilm" alt="Vue logo" src="../../assets/starisborn.jpg"
      /></slide>
      <slide :index="4"
        ><img id="cardFilm" alt="Vue logo" src="../../assets/NBLpng.png"
      /></slide>
      <slide :index="5"
        ><img id="cardFilm" alt="Vue logo" src="../../assets/starisborn.jpg"
      /></slide>
      <slide :index="6"
        ><img id="cardFilm" alt="Vue logo" src="../../assets/starisborn.jpg"
      /></slide>
      <slide :index="7"
        ><img id="cardFilm" alt="Vue logo" src="../../assets/starisborn.jpg"
      /></slide>
      <slide :index="8"
        ><img id="cardFilm" alt="Vue logo" src="../../assets/starisborn.jpg"
      /></slide>
      <slide :index="9"
        ><img id="cardFilm" alt="Vue logo" src="../../assets/starisborn.jpg"
      /></slide>
    </carousel>
  </div>
</template>

<script>
import { Carousel, Slide } from "vue-carousel";
import IndexCard from "./Cards.vue";

export default {
  name: "IndexCarousel2D",
  components: {
    Carousel,
    Slide,
    IndexCard,
  },
  computed: {
    topmovies() {
      console.log(this.$store.state.topmovies);
      return this.$store.state.topmovies;
    },
  },
  methods: {
    getTop10Movies() {
      this.$store.dispatch("getTop10Movies");
    },
  },
  created() {
    this.getTop10Movies();
  },
};
</script>

<style>
.carousel2D {
  position: absolute;
  top: 65%;
  left: 10%;
  z-index: 3;
  width: 90%;
}

#cardFilm {
  opacity: 0.8;
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 15%;
  margin: 0 20px;
}
.CardTitle {
  color: white;
  font-size: 1.5rem;
  margin-bottom: 1rem;
  font-family: Staatliches;
}
.CardTitle2 {
  color: black;
  font-size: 1.5rem;
  margin-bottom: 1rem;
  margin-top: 1rem;
  font-family: Staatliches;
}

#carousel2Dcontent
  > div.VueCarousel-pagination
  > div
  > button.VueCarousel-dot.VueCarousel-dot--active {
  background-color: #ffc107 !important;
}
#carousel2Dcontent > div.VueCarousel-pagination > div > button:nth-child {
  background-color: white;
}
/* .VueCarousel-inner{
  transition: transform 5s ease 0s!important
} */
</style>


