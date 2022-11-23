<template>
  <div>
    <div class="CommunityDiv" v-for="article in profile.ratings" :key="article.id">
      <div class="recommendMovieTitle" >
        <ProfileArticleMovie style="font-family: BMHANNAAir_ttf;" :movie=article.movie />
      </div>
      <div class="d-flex justify-content-between" style="width:100%; ">
        <div>
          <div class="communityTitle" style="font-family: BMJUA;">{{article.title}}</div>
        </div>
        <div class="d-flex">
          <div class="communityScore">❤ {{article.like_user_count}}</div>
          <div class="communityScore" style="margin-right: 1rem;">⭐ {{article.rate}}</div>
          <div class="communityDate" >{{article.created_at.split('T')[0].replace(/-/g,' / ')}}</div></div>
        </div>
      </div> 
  </div>
</template>
  
<script>
import ProfileArticleMovie from './ProfileArticleMovie.vue'
// import ArticleInAccount from './ArticleInAccount.vue'



export default {
  name: "ProfileArticles",
  props: {
    profile: Object,
    userProfile: String,
  },
  data(){
    return{
      visibleContect:false,
    }
  },
  components:{
    ProfileArticleMovie,
  },

};
</script>
  
<style>
@font-face {
  font-family: BMDOHYEON;
  src: url(../../fonts/BMDOHYEON_ttf.ttf);
}
@font-face {
  font-family: BMJUA;
  src: url(../../fonts/BMJUA_ttf.ttf);
}
@font-face {
  font-family: BMHANNAAir_ttf;
  src: url(../../fonts/BMHANNAAir_ttf.ttf);
}

  .recommendSelect{
    font-size:0.8rem;
  }
</style>