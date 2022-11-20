<template>
  <div class="SearchFlexDiv">
    <div class="UserLeftDiv">
      <img
        class="userImg"
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQM5z7l_V183adxjX0NHjejDhNSdunjN8UoTkZIBKts_Q&s"
        alt
      />
      <div class="userIconDiv">
        <font-awesome-icon icon="fa-solid fa-trophy" />
        <font-awesome-icon icon="fa-solid fa-medal" />
        <font-awesome-icon icon="fa-solid fa-award" />
      </div>
      <b-button variant="warning" class="followButton">FOLLOW</b-button>
    </div>
    <div class="UserRightDiv">
      <b-tabs content-class="mt-3">
        <b-tab title="PROFILE">
          <div class="userProfileDiv" v-if="correctState">
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
            <div class="userButtonDiv">
              <b-button style="margin-right: 50px;" @click="userForm">수정하기</b-button>
              <b-button>회원탈퇴</b-button>
            </div>
          </div>
          <div class="userButtonDiv2" v-if="!correctState">
            <div >
              <b-button size="lg" style="margin-right: 100px;" v-b-modal.modal-password >비밀번호 변경</b-button>
              <b-button size="lg">프로필 사진 변경</b-button>
              <b-modal class="communityModal" ref="my-modal"  size="md" id="modal-password" title="게시글 작성">
                <div>
                  <b-form-input v-model="password1" style="margin-bottom:30px;" size="lg" placeholder="새로운 비밀번호를 입력하세요"></b-form-input>
                  <b-form-input v-model="password2" style="margin-bottom:30px;" size="lg" placeholder="비밀번호를 다시 입력하세요"></b-form-input>
                </div>
                <template #modal-footer>
                  <div>
                    <b-button
                    variant="warning"
                      size="xl"
                      class="float-right"
                      @click="addChangePassword"
                    >변경하기</b-button>
                  </div>
                </template>
                
              </b-modal>
            </div>
          </div>
        </b-tab>
        
        <b-tab title="ARTICLES">
          <ProfileArticles :profile=profile />
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


export default {
  name: "UserInfo",
  data() {
    return {
      correctState: 1,
      password1:null,
      password2: null,
    };
  },
  components: { AddCardDiv, Carousel, Slide, ProfileArticles },
  computed: {
    profile() {
      return this.$store.getters.profile;
    }
  },
  methods: {
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

  },
  created() {
    console.log(this.$store.state.profile)
    console.log(this.$store.state.currentUser)
    console.log('yes')

    this.fetchProfile();
  }
};
</script>

<style>
.UserLeftDiv {
  margin: auto;
  width: 35%;
  text-align: center;
}
.userImg {
  width: 200px;
  height: 200px;
  border-radius: 100%;
}
.followButton {
  width: 150px;
  margin-top: 150px;
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