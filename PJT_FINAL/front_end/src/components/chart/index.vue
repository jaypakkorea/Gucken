<template>
  <div>
    <carousel-3d class="carousel">
        <slide  v-for="aa in 5" :key="aa" :index="aa-1">
          <img alt="Vue logo" src="../../assets/logo.png"/>
        </slide>
   </carousel-3d>
  </div>
</template>

<script>
// import LankIndexCard from './cardDiv.vue'
import {Carousel3d, Slide} from 'vue-carousel-3d'
export default {
  name:"ChartIndex",
  components:{
    // LankIndexCard,
    Carousel3d,
    Slide,
  }
}
</script>

<style>

</style>