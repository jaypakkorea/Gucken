<template>
  <div>
    <div class="detailCommunityDiv">
        <div class="CommunitysDiv">
            <div class="CommunityDiv" v-for="article in movie.ratings" :key="article.id">
                <div class="communutyText">{{article.user.username.split('@')[0]}}</div>
                  <div class="communityScore">{{article.rate}}</div>
                  <!-- communityScoreHigh / -->
                <div style="margin-right:20px;">{{article.title}}</div>
                <div >{{article.created_at.split('T')[0].replace(/-/g,' / ')}}</div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>

export default {
    name: "MovieArticles",
    props : {
      movie : Object
    },
    data() {
    return {
      articles: this.movie.ratings,
    };
  },
    watch: {
      articles: {
        deep : true,
        handler : function() {
          this.articles = this.movie.ratings
          console.log('The list of colours has changed!')
          console.log(this.articles)
        },
      }
  }
}
</script>

<style>

</style>