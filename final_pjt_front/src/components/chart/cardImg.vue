<template>
  <div>
    <div>
        <img class="ChartRecommendimgDiv"  :src="link_url" />
    </div>
  </div>
</template>
  
  <script>
export default {
  name: "ChartRecommendCard",
  data() {
    return {
      link_url: `https://image.tmdb.org/t/p/original/${this.recommendmovie.poster_path}`,
    };
  },
  props: {
    recommendmovie: String,
  },
};
</script>  
<style>
.noneImg{
    background-color: lightcyan;
}
.ChartRecommendimgDiv{
    border-radius: 20px;
}
</style>