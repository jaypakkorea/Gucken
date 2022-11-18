<template>
  <div>
    <div class="detailCommunityDiv">
        <div class="CommunitysDiv">
            <div class="CommunityDiv" v-for="article in movie.ratings" :key="article.id">
                <div class="communutyText">{{article.user.username}}</div>
                  <div class="communityScore">{{article.rate}}</div>
                  <!-- communityScoreHigh / -->
                <div>{{article.title}}</div>
                <div>{{article.created_at}}</div>
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
    }

}
</script>

<style>

</style>