<template>
  <div>
    <h1 style="color:red">{{profile.ratings_count}}</h1>
    <div class="CommunityDiv" v-for="article in profile.ratings" :key="article.id">
      <div class="recommendMovieTitle" >
        <ProfileArticleMovie :movie=article.movie />
      </div>
      <div class="communityScore" v-if="article.rate<=6">👎 {{article.rate}}</div>
      <div
        class="communityScore"
        style="background-color:#ffda4f;"
        v-if="article.rate>6"
      >👍 {{article.rate}}</div>
      <div class="d-flex justify-content-between" style="width:100%;">
        <div class="communityTitle">{{article.title}}<br/> <p style="font-size:1.3rem;">{{article.content}}</p></div>
        <div class="communityDate">{{article.created_at.split('T')[0].replace(/-/g,' / ')}}</div></div>
      </div>      
  </div>
</template>
  
<script>
import ProfileArticleMovie from './ProfileArticleMovie.vue'


export default {
  name: "ProfileArticles",
  props: {
    profile: Object,
    userProfile: String
  },
  components:{
    ProfileArticleMovie
  }
};
</script>
  
  <style>
.communityDetailDate {
  font-size: 1rem;
  margin-top: 0.5rem;
  text-align: right;
}
.communityDetailModal {
  background-color: aliceblue;
  width: 80%;
  margin: 0 auto;
  border-radius: 10px;
  padding: 3rem;
  margin-bottom: 3rem;
}
.communityDetailTitle {
  width: 100%;
  font-size: 3rem;
  margin-bottom: 3rem;
  font-weight: bold;
}
.communityDetailContent {
  width: 100%;
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 3rem;
  display: flex;
  justify-content: space-between;
}
.communityDetailListDiv {
  font-size: 1.5rem;
  color: gray;
  margin-bottom: 1rem;
}
#textarea-no-resize2 {
  margin: 3rem 0 2rem 0;
}
.recommendMovieTitle{
  min-width: 150px;
  max-width: 150px;
  margin: auto 0;
  font-size: 1.5rem;

}
</style>