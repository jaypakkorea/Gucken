<template>
  <div>
    <img v-if="this.poster_path" class="detailImg" :src="link_url" />
    <img
      v-if="!this.poster_path"
      class="detailImg"
      src="https://icon-library.com/images/no-image-icon/no-image-icon-1.jpg"
      alt=""
    />
  </div>
</template>

<script>
export default {
  name: "indexSearchImg",
  data() {
    return {
      link_url: `https://image.tmdb.org/t/p/original${this.poster_path}`,
    };
  },
  props: {
    poster_path: String,
  },
};
</script>

<style>

</style>