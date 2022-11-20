<template>
  <div>
    <carousel-3d class="carousel">
      <slide v-for="aa in 5" :key="aa" :index="aa-1">
        <img alt="Vue logo" :src="link_url" />
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";

export default {
  name: "LankIndexCard",
  data() {
    return {
        link_url: `https://search.pstatic.net/sunny/?src=https%3A%2F%2Fdnvefa72aowie.cloudfront.net%2Forigin%2Farticle%2F202206%2FA03D68CD75227C1C7E7A0F6E8D7AEC59FD7697ED2A0BB8B57F8CFD4E0F0B1B02.jpg%3Fq%3D95%26s%3D1440x1440%26t%3Dinside&type=sc960_832`,
    };
  },
  props:{

  },
  components: {
    Carousel3d,
    Slide
  }

};
</script>

<style>
</style>