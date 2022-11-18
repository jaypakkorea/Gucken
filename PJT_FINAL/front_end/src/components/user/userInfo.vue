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
    <b-tab title="PROFILE" active>
        <div class="userProfileDiv">
            <div class="userTextName">Name</div>
            <div class="userText">M.H</div>
            <div class="userTextName">Follower</div>
            <div class="userText">23,000</div>
            <div class="userTextName">Following</div>
            <div class="userText">12,313</div>
            <div class="userTextName">Add Movie</div>
            <div class="userText">452</div>
            <div class="userTextName">Joined</div>
            <div class="userText">03 / 2019</div>
        </div>
    </b-tab>
    <b-tab title="ARTICLES">
        
    </b-tab>
    <b-tab title="ADD LIST">
        
    </b-tab>

  </b-tabs>
    </div>
    <div style="color : red">
        <p>{{profile}}</p>
        <h1> {{profile.id}}</h1>
        <h1> {{profile.username}}</h1>
        <h1> {{profile.followings}}</h1>
        <h1>  {{profile.followers}}</h1>
        <h1> {{profile.following_count}}</h1>
        <h1>  {{profile.follower_count}}</h1>
        <h1> {{profile.date_joined}}</h1>
        <p>  {{profile.like_movies}}</p>
        
    </div>
  </div>
</template>

<script>

export default {
    name:'UserInfo',
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
</style>