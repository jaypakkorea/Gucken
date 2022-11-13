<template>
  <div class="carousel2D">
    <carousel :per-page="6" :navigate-to="someLocalProperty" :mouse-drag="true" id="carousel2Dcontent">
      <slide :index="0"><img id="cardFilm" alt="Vue logo" src="../assets/starisborn.jpg"/></slide>
      <slide :index="1"><img id="cardFilm" alt="Vue logo" src="../assets/starisborn.jpg"/></slide>
      <slide :index="2"><img id="cardFilm" alt="Vue logo" src="../assets/starisborn.jpg"/></slide>
      <slide :index="3"><img id="cardFilm" alt="Vue logo" src="../assets/starisborn.jpg"/></slide>
      <slide :index="4"><img id="cardFilm" alt="Vue logo" src="../assets/starisborn.jpg"/></slide>
      <slide :index="5"><img id="cardFilm" alt="Vue logo" src="../assets/starisborn.jpg"/></slide>
      <slide :index="6"><img id="cardFilm" alt="Vue logo" src="../assets/starisborn.jpg"/></slide>
      <slide :index="7"><img id="cardFilm" alt="Vue logo" src="../assets/starisborn.jpg"/></slide>
      <slide :index="8"><img id="cardFilm" alt="Vue logo" src="../assets/starisborn.jpg"/></slide>
      <slide :index="9"><img id="cardFilm" alt="Vue logo" src="../assets/starisborn.jpg"/></slide>
    </carousel>
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';

export default {
    name : 'IndexCarousel2D',
    components: {
      Carousel,
      Slide
    }
}
</script>

<style>
.carousel2D {
  position: absolute;
  top: 70%;
  left:10%;
  z-index: 3;
  width : 90%;
}

#cardFilm{
  opacity: 0.8;
  width:150px;
  height:150px;
  object-fit: cover;
  border-radius: 15%;
}


#carousel2Dcontent > div.VueCarousel-pagination > div > button.VueCarousel-dot.VueCarousel-dot--active {
  background-color : #ffc107!important
}
#carousel2Dcontent > div.VueCarousel-pagination > div > button:nth-child{
  background-color : white
}
</style>