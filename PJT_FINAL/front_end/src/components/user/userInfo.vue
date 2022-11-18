<template>
  <div class="SearchFlexDiv">
    <div class="UserLeftDiv">
        <img class="userImg" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM5z7l_V183adxjX0NHjejDhNSdunjN8UoTkZIBKts_Q&s" alt="">
        <div class="userIconDiv"> 
            <font-awesome-icon icon="fa-solid fa-trophy" />
            <font-awesome-icon icon="fa-solid fa-medal" />
            <font-awesome-icon icon="fa-solid fa-award" />
        </div>
        <b-button variant="warning" class="followButton">FOLLOW</b-button>
    </div>
    <div class="UserRightDiv">
        <b-tabs content-class="mt-3">
    <b-tab title="PROFILE" >
        <div class="userProfileDiv">
            <div class="userTextName">Name</div>
            <div class="userText">{{profile.username.split('@')[0]}}</div>
            <div class="userTextName">Follower</div>
            <div class="userText">{{profile.followers}}</div>
            <div class="userTextName">Following</div>
            <div class="userText">{{profile.followings}}</div>
            <div class="userTextName">Add Movie</div>
            <div class="userText">{{profile.like_movies.length}}</div>
            <div class="userTextName">Joined</div>
            <div class="userText">{{profile.date_joined.split('T')[0].replace(/-/g,' / ')}}</div>
        </div>
    </b-tab>
    <b-tab title="ARTICLES">
        
    </b-tab>
    <b-tab title="ADD LIST" active>
    <carousel
      :loop="true"
      v-bind:autoplay="true"
      :per-page="2"
      :mouse-drag="true"
      speed="3000"
      autoplay-timeout="5000"
      id="carousel2Dcontentaddlist"
      style="transition: transform 0.5s ease 0s"
    >
      <slide
        v-for="(topmovie, index) in profile.like_movies"
        :key="topmovie.id"
        :index="index"
      >
        <router-link
        :to="{ name: 'SearchDetailView', params: { moviePk: topmovie.id } }">
          <AddCardDiv :topmovie="topmovie.poster_path" />
        </router-link>
      </slide>
    </carousel>
    </b-tab>
  </b-tabs>
    </div>        
  </div>
</template>

<script>
import AddCardDiv from "./addListCard.vue";
import { Carousel, Slide } from "vue-carousel";

export default {
    name:'UserInfo',
    components:{AddCardDiv, Carousel, Slide},
    computed: {
        profile(){
            return this.$store.getters.profile
        }
    },
    methods: {
        fetchProfile(){
            const payload =  parseInt(this.$route.params.userid)
            this.$store.dispatch("fetchProfile", payload);
        }
    },
    created() {
        this.fetchProfile()
    },
}
</script>

<style>
.UserLeftDiv{
    margin: auto;
    width: 35%;
    text-align: center;
}.userImg{
    width: 200px;
    height: 200px;
    border-radius: 100%;
    
}.followButton{
    width: 150px;
    margin-top: 150px;
}
.userIconDiv{
    margin: 150px auto;
    max-width: 250px;
    display: flex;
    margin-bottom: 100px;
    justify-content: space-between;
    color: gray;
    font-size: 2rem;
}.UserRightDiv{
    padding: 5rem;
    width: 65%;
}.userTextName{
    color: gray;
}.userText{
    font-size: 3rem;
    margin-top: -5px;
    margin-bottom: 60px;
}.userProfileDiv{
    padding-top: 2rem;
}
#carousel2Dcontentaddlist
  > div.VueCarousel-pagination
  > div
  > button.VueCarousel-dot.VueCarousel-dot--active {
  background-color: #ffc107 !important;
}
#carousel2Dcontentaddlist > div.VueCarousel-pagination > div > button:nth-child {
  background-color: white;
}

</style>