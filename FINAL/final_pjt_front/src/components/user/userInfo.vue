<template>
  <div class="SearchFlexDiv">
    <div class="UserLeftDiv">
      <div style="position:relative;">
        <b-avatar button size="18rem" 
        :src="userProfile"
        alt="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM5z7l_V183adxjX0NHjejDhNSdunjN8UoTkZIBKts_Q&s"
        @click="$refs.profileImage.click()"></b-avatar>
        <div v-if="this.$store.state.currentUser.pk === profile.id && !profile.profile_pic" style="position:absolute; left: 40%; top:70% ; color:white; font-weight: bold;">C l i c k !</div>
      </div>
        
      <input style="display: none" type="file"  @change="inputProfilePic" ref="profileImage"  class="input-file" value="프로필 변경"  >
      

      <div class="userIconDiv">
        <div v-if="profile.follower_count < 5"  id="tooltip-target-1" ><font-awesome-icon icon="fa-solid fa-trophy" /></div>
        <div v-if="profile.follower_count >= 5"  id="tooltip-target-1" style="color:#ffc107;"><font-awesome-icon icon="fa-solid fa-trophy" /></div>

        <div  v-if="likeCount < 5" id="tooltip-target-2"><font-awesome-icon icon="fa-solid fa-medal" /></div>
        <div v-if="likeCount >= 5" id="tooltip-target-2" style="color:#ffc107;"><font-awesome-icon icon="fa-solid fa-medal" /></div>

        <div v-if="profile.ratings_count < 5" id="tooltip-target-3"><font-awesome-icon icon="fa-solid fa-award" /></div>
        <div v-if="profile.ratings_count >= 5" id="tooltip-target-3" style="color:#ffc107;"><font-awesome-icon icon="fa-solid fa-award" /></div>
        <b-tooltip target="tooltip-target-1" triggers="hover">
          팔로워 수 <div class="d-flex justify-content-center">
          <div style="color:#ffc107;"> {{profile.follower_count}} </div>
          <div> &nbsp; / 5</div> </div>
        </b-tooltip>
        <b-tooltip target="tooltip-target-2" triggers="hover">
          총 좋아요 수 <div class="d-flex justify-content-center">
          <div style="color:#ffc107;"> {{likeCount}} </div>
          <div> &nbsp; / 5</div> </div>
        </b-tooltip>
        <b-tooltip target="tooltip-target-3" triggers="hover">
          게시물 수 <div class="d-flex justify-content-center">
          <div style="color:#ffc107;"> {{profile.ratings_count}} </div>
          <div> &nbsp; / 5</div> </div>
        </b-tooltip>
      </div>
      
      <!-- <b-button  v-if="!parseInt(this.$route.params.userid) === this.$store.state.currentUser.pk" 
        variant="warning" class="followButton">FOLLOW</b-button> -->
        <b-button v-if="this.$store.state.currentUser.pk !== profile.id && follow_follwing || this.followerList.includes(this.$store.state.currentUser.pk)" 
         class="followButton"  @click="followIng">UNFOLLOW</b-button>
        <b-button v-else-if="this.$store.state.currentUser.pk !== profile.id && !follow_follwing" 
        variant="warning" class="followButton" @click="followIng">FOLLOW</b-button>
    </div>
    <div class="UserRightDiv">
      <b-tabs content-class="mt-3">
        <b-tab title="PROFILE" active>
          <div class="userProfileDiv" v-if="correctState">
            <div class="userTextName">Name</div>
            <div class="userText" style="font-family: BMDOHYEON;">{{profile.username.split('@')[0]}}</div>
            <div class="userTextName">Follower</div>
            <div class="userText" style="cursor : pointer; font-family: BMJUA;" @click="FollowerStateChange">{{profile.follower_count}}</div>
            <div v-if="FollowerState && profile.follower_count"  class="followingsDiv">
              <div style="margin-bottom: 0.5rem;" v-for="follower in profile.followers" :key="follower.id">
                  <div><followerProfile :follower="follower" /></div>
              </div>
            </div>
            <div class="userTextName">Following</div>
            <div class="userText" style="cursor : pointer; font-family: BMJUA;" @click="FollowingStateChange">{{profile.following_count}}</div>
            <div v-if="FollowingState && profile.following_count" class="followingsDiv" >
              <div style="margin-bottom: 0.5rem;" v-for="following in profile.followings" :key="following.id">
                  <followingProfile :following="following" />
              </div>
            </div>
            <div class="userTextName">Like List</div>
            <div class="userText" style="font-family: BMJUA;">{{profile.like_movies.length}}</div>
            <div class="userTextName">Joined</div>
            <div class="userText" style="font-family: BMJUA;">{{profile.date_joined.split('T')[0].replace(/-/g,' / ')}}</div>
          </div>
        </b-tab>
        
        <b-tab title="ARTICLES">
          <ProfileArticles :profile=profile :userProfile=userProfile :sumLikeUsers=sumLikeUserCount />
        </b-tab>

        <b-tab title="LIKE LIST" lazy >
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
              v-for="(topmovie, index) in profile.like_movies.slice().reverse()"
              :key="topmovie.id"
              :index="index"
            >
              <router-link :to="{ name: 'SearchDetailView', params: { moviePk: topmovie.id } }">
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
import ProfileArticles from "./ProfileArticles.vue";
import followerProfile from "./followerProfile.vue";
import followingProfile from "./followingProfile.vue";
import Swal from "sweetalert2";
import axios from "axios";

export default {
  name: "UserInfo",
  data() {
    return {
      correctState: 1,
      password1:null,
      password2: null,
      selectedFile: '' ,
      FollowerState:0,
      FollowingState:0,
      sumLikeUserCount:0,
      follow_follwing:'',
      likeCount : 0,
      followerList:[]
    };
  },
  components: { AddCardDiv, Carousel, Slide, ProfileArticles, followerProfile,followingProfile },
  computed: {
    profile() {
      return this.$store.getters.profile;
    },
    isLogin(){
      return this.$store.getters.isLogin
    },
    userProfile(){
      if (this.profile.profile_pic) {
        return `http://localhost:8000${this.profile.profile_pic}`  
      } else {
        return 'http://localhost:8000/media/profile/images/change.jpg'
      }
    } 
  },
  methods: {
    readLikeCount(){
      const API_URL = 'http://127.0.0.1:8000'
        axios({
        method: 'get',
        url: `${API_URL}/profile/${this.$route.params.userid}/like/`,
      })
        .then((res) => {
          this.likeCount = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    inputProfilePic(event){
      this.selectedFile = event.target.files[0]
      this.updateProfilePic()
    },
    updateProfilePic(){
      let fd = new FormData();
      fd.append('profile_pic', this.selectedFile)
      this.$store.dispatch("updateProfilePic", fd)
      window.location.reload(true);
    },

    followIng(){
      if (!this.isLogin) {
        Swal.fire('로그인이 필요한 서비스 입니다', '', 'error')
        this.$router.push({name:'user'})
      }
      const payload = parseInt(this.$route.params.userid);
      this.$store.dispatch("followIng", payload);
      this.follow_follwing = !this.follow_follwing
    },
    fetchProfile() {
      const payload = parseInt(this.$route.params.userid);
      this.$store.dispatch("fetchProfile", payload);
    },
    userForm(){
      this.correctState = 0
    },
    addChangePassword(){
      const password1 = this.password1
      const password2 = this.password2
      const payload = {
        password1,
        password2,
      }
      this.$store.dispatch('changePassword', payload)
    },
    FollowerStateChange(){
      this.FollowerState = !this.FollowerState
    },
    FollowingStateChange(){
      this.FollowingState = !this.FollowingState
    },
    sumLikeUsers(){
      for(let i=0; i< this.profile.ratings_count; i++){
        let item = this.profile.ratings[i];
        this.sumLikeUserCount += item.like_user_count
      }
    },
    makeFollowerList(){
      for(let i=0; i < this.profile.followers.length; i++){
        this.followerList.push(this.profile.followers[i].id)
      }
    }

  },
  created() {
    this.makeFollowerList()
    this.sumLikeUsers()
    this.fetchProfile()
    this.readLikeCount()
  }

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


.UserLeftDiv {
  margin: auto;

  text-align: center;
  position: fixed;
  top: 10rem;
  left: 10%;
}
.userImg {
  width: 200px;
  height: 200px;
  border-radius: 100%;
}
.profileImgUpdate{
  background: rgb(175, 175, 175);
  height: 40px;
  line-height: 40px;
  margin-top: 0.8rem;
  border-radius: 10px;
  color: rgb(66, 66, 66);
  font-weight: bold;
}
.followButton {
  width: 150px;
  margin-top: 150px;
}
.followingsDiv{
  background-color: aliceblue;
  color: black;
  padding: 1rem;
  border-radius: 10px;
  margin-top: -1rem;
  margin-bottom: 2rem;
}
.userIconDiv {
  margin: 150px auto;
  max-width: 250px;
  display: flex;
  margin-bottom: 100px;
  justify-content: space-between;
  color: gray;
  font-size: 2rem;
}
.UserRightDiv {
  padding: 5rem;
  width: 65%;
  margin-left: 35%;
}
.userTextName {
  color: gray;
}
.userText {
  font-size: 3rem;
  margin-top: -5px;
  margin-bottom: 30px;
}
.userProfileDiv {
  padding-top: 2rem;
}
#carousel2Dcontentaddlist
  > div.VueCarousel-pagination
  > div
  > button.VueCarousel-dot.VueCarousel-dot--active {
  background-color: #ffc107 !important;
}
#carousel2Dcontentaddlist
  > div.VueCarousel-pagination
  > div
  > button:nth-child {
  background-color: white;
}
.userButtonDiv {
  margin-top: 15px;
}
.userButtonDiv2{
  widows: 500px;
  height: 500px;
  line-height: 500px;
  margin: auto;
  text-align: center;
}
#modal-password{
  top: 20vh;
  color: white;
}

</style>