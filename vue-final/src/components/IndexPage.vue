<template>
  <div class="index">
    <Sidebar/>
    <section class="banner-container relative w-full h-full">
      <IndexAvatar/>
    </section>
    <IndexCarousel2D/>
  </div>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";
import Sidebar from "@/components/sidebar/Sidebar";
import IndexAvatar from "@/components/IndexAvatar";
import IndexCarousel2D from "@/components/IndexCarousel2D";
import { BootstrapVue, BIcon, BIconArrowUp, BIconArrowDown } from 'bootstrap-vue';


export default {
  name : 'IndexPage',
  components: {
    Carousel3d,
    Slide,
    Sidebar,
    IndexAvatar,
    IndexCarousel2D,
  },
  methods: {
    popupText() {
      this.$store.dispatch("popupText");
    },
  },
};
</script>

<style>
.index{
  background-color : black;
}
</style>