<template>
  <div
    class="detail_main_div"
    :style="{backgroundImage:`url(${`https://image.tmdb.org/t/p/original/${this.movie.poster_path}`})`}"
  >
    <router-link class="homeTag" :to="{ name: 'search' }">
      <font-awesome-icon icon="fa-solid fa-angle-left" />BACK
    </router-link>
    <div class="detail_div">
      <div class="detail_left_div">
        <div class="detail_title">{{this.movie.title}}</div>
        <div class="detail_flexdiv">
          <div>{{this.movie.release_date}}</div>
          <!-- <div> Top 10 Movie </div> -->
          <b-button variant="warning" @click="likeMovie">Add List</b-button>
        </div>
        <div style="width: 80%;">{{this.movie.overview}}</div>
        <!-- 배우가 없을떄는 v-if로 div 자체가 뜨지 않게 하기 -->
        <div v-if="this.movie.actors" class="detail_actors">
          <!-- for 문으로 배우 리스트 돌면서 이름, 사진 보여주기 -->
          <div class="detail_actors_img" v-for="actor in this.movie.actors" :key="actor.name">
            <img
              class="detail_actors_img_crop"
              src="https://image.tmdb.org/t/p/original/qSizF2i9gz6c6DbAC5RoIq8sVqX.jpg"
              alt
            />
            {{actor.name}}
          </div>
        </div>
        <div class="detail_rate">
          <div>
            <div style="font-size:3rem;">MOVIE</div>
            <div class="d-flex">
              <div
                v-for="names in this.movie.genres"
                :key="names"
                style="color:gray;"
              >{{names.name}} /</div>
            </div>
          </div>
          <!-- 내 평점 -->
          <div>
            <div style="font-size:3rem;">10.0</div>
            <div style="color:gray;">MyRATE</div>
          </div>
          <!-- DB 평점 -->
          <div v-if="this.movie.vote_average">
            <div style="font-size:3rem;">{{this.movie.vote_average}}</div>
            <div style="color:gray;">RATE</div>
          </div>
        </div>
      </div>
      <div class="detail_right_div">
        <b-tabs content-class="mt-2">
          <b-tab title="TRAILER" active>
            <iframe
              style="margin-top:3rem;"
              id="ytplayer"
              type="text/html"
              width="100%"
              height="1000px"
              :src="VideoData"
              frameborder="0"
            ></iframe>
          </b-tab>
          <b-tab title="COMMUNITY">
            <div class="commumityButtonDiv">
              <b-button v-b-modal.modal-1>
                <font-awesome-icon class="pluscommunuty" icon="fa-solid fa-plus" />
              </b-button>
              <b-modal class="communityModal" size="xl" id="modal-1" title="게시글 작성">
                <div>
                  <b-form-textarea size="lg" no-resize rows="7" id="textarea-no-resize" type="text" ></b-form-textarea>
                  <div style="margin-left:35%; margin-top:100px;">
                  <div @mouseleave="showCurrentRating(0)" style="display:inline-block;">
                    <star-rating :show-rating="false" @current-rating="showCurrentRating" @rating-selected="setCurrentSelectedRating" :increment="0.1"></star-rating>
                  </div>
                  <div style="margin-top:10px;font-weight:bold;">{{currentRating}}</div>
                  </div>
                </div>
                <template #modal-footer>
                  <div>
                    <b-button
                    variant="warning"
                      size="xl"
                      class="float-right"
                      @click="submitcommunity"
                    >SUBMIT</b-button>
                  </div>
                </template>
                
              </b-modal>
            </div>
            <div class="detailCommunityDiv">
              <div class="CommunitysDiv">
                <div class="CommunityDiv" v-for="ss in 5" :key="ss">
                  <img class="communityUserImg" src="../../assets/starisborn.jpg" alt />
                  <div class="communityScore">3.5</div>
                  <!-- communityScoreHigh / -->
                  <div class="communutyText">지루해요</div>
                </div>
              </div>
            </div>
          </b-tab>
        </b-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import StarRating from 'vue-star-rating'

export default {
  name: "DetailVue",
  props: {
    movie: Object
  },
  data() {
    return {
      myKeyword: this.movie,
      is_liked: false,
      urlList: [],
      video: [],
      VideoData: "",
      myApi: "",
      myAPIList: [
        "AIzaSyDvjcb7odUilSZEcCyXBY2rX9z0fTYYWvQ",
        "AIzaSyDAes3uWN2F5a2_2EHBBFuIm0Ctv8Hpj1A",
        "AIzaSyCN9uPuXJyXoVjTvkOA8g5ivcUGsGKDiK8",
        // 'AIzaSyATqBywB8sPKs2PrAv_FMEp4Xy7OWzqXOI',
        "AIzaSyDEgtL7oYOo_OJBvIqq2MJhVxDV-IYwekc",
        "AIzaSyBLMEBNxzyohh-zUFGFvHA5ZpI-TLmM4JE",
        "AIzaSyDd-ndJ5GJOKwdBhILSGmAmDneCZEnzrKw"
      ],
      tabIndex: 0,
      rating: 0,
    currentRating: "점수를 등록해 주세요!",
    currentSelectedRating: "점수를 등록해 주세요!",
    boundRating: 3,
    };
  },
  methods: {
    pick() {
      const idx = Math.floor(Math.random() * this.myAPIList.length);
      this.myApi = this.myAPIList[idx];
    },
    InputGetEvent(keyword) {
      this.myKeyword = keyword;
      const baseURL = "https://www.googleapis.com/youtube/v3/search";
      // const API_KEY = 'AIzaSyCN9uPuXJyXoVjTvkOA8g5ivcUGsGKDiK8'
      axios
        .get(baseURL, {
          params: {
            key: this.myApi,
            part: "snippet",
            type: "video",
            q: this.myKeyword + "공식 예고편",
            maxResults: 1
          }
        })
        .then(response => {
          this.video = response.data.items[0];
          console.log(this.video);
          this.VideoData = `https://www.youtube.com/embed/${response.data.items[0].id.videoId}?autoplay=1&mute=1`;
        })
        .catch(error => {
          console.log("something wrong!");
          console.log(error);
        });
    },
    likeMovie() {
      const moviePk = this.movie.id;
      this.$store.dispatch("addList", moviePk);
      this.is_liked = !this.is_liked;
    },
    addCommunity() {
      console.log("ㅎㅇㅎㅇ");
    },
    setRating: function(rating) {
      this.rating =  rating * 2 ;
    },
    showCurrentRating: function(rating) {
      this.currentRating = (rating === 0) ? this.currentSelectedRating : rating* 2;
    },
    setCurrentSelectedRating: function(rating) {
      this.currentSelectedRating =  rating* 2 ;
    }
  },
  created() {
    // this.pick()
    // this.InputGetEvent(this.myKeyword)
  },
  components: {
    StarRating
}
};
</script>

<style>
.detail_main_div {
  padding-top: 2rem;
  width: 100%;
  height: fit-content;
  min-height: 100vh;
  position: relative;
  z-index: 1;
  background-repeat: no-repeat;
}
.detail_main_div::after {
  width: 100%;
  height: 100%;
  content: "";
  background: linear-gradient(
    to left,
    rgba(20, 20, 20, 0.5) 10%,
    rgba(20, 20, 20, 0.75) 25%,
    rgba(20, 20, 20, 0.9) 50%,
    rgba(20, 20, 20, 0.9) 65%,
    rgba(20, 20, 20, 1) 80%
  );
  background-size: cover;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  filter: grayscale(100%);
  opacity: 0.8;
}
.nav-link {
  color: white !important;
}
.nav-tabs .nav-item.show .nav-link,
.nav-tabs .nav-link.active {
  color: black !important;
}
.homeTag {
  text-decoration: none;
  color: rgb(151, 148, 148);
  margin-left: 2rem;
}
.detail_div {
  display: flex;
  font-family: Staatliches;
  color: white;
}
.detail_left_div {
  width: 35%;
  margin: 0 50px;
}
.detail_flexdiv {
  display: flex;
  justify-content: space-between;
  width: 70%;
  margin: 40px;
}
.detail_actors {
  display: flex;
  /* justify-content: space-between; */
  margin: 2rem 0;
}
.detail_rate {
  display: flex;
  justify-content: space-between;
  margin: 4rem 0;
  width: 60%;
  min-width: 400px;
}
.detail_actors_img {
  padding: 0;
  margin: 0;
  width: 120px;
  display: flex;
  flex-direction: column;
  text-align: center;
  margin: 0 10px;
  filter: grayscale(100%);
}
.detail_actors_img_crop {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 100%;
  margin: 0 auto;
}
.detail_right_div {
  width: 65%;
  margin-right: 50px;
}
.detail_title {
  margin-top: 3rem;
  font-size: 7rem;
}

.detailCommunityDiv {
  width: 100%;
  min-height: 500px;
  padding-top: 1rem;
  position: relative;
  z-index: 1;
}
.pluscommunuty {
  width: 40px;
  height: 40px;
  color: #ffda4f;
  border-radius: 5px;
}
.commumityButtonDiv {
  text-align: end;
  margin-bottom: 5px;
}
.detailCommunityDiv::after {
  width: 100%;
  height: 100%;
  content: "";
  background-color: black;
  opacity: 0.2;
  background-size: cover;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}

.CommunitysDiv {
  margin: 20px 50px;
}
.CommunityDiv {
  border: 1px solid white;
  border-radius: 5px;
  margin: 10px 0;
  padding: 10px 20px;
  display: flex;
}
.communityUserImg {
  width: 50px;
  height: 50px;
  border-radius: 100%;
  margin-right: 2rem;
}
.communityScore {
  color: black;
  font-size: 2rem;
  padding: 0 20px;
  border-radius: 5px;
  z-index: 10;
  background-color: rgb(211, 209, 209);
}
.communityScoreHigh {
  color: black;
  font-size: 2rem;
  padding: 0 20px;
  border-radius: 5px;
  z-index: 10;
  background-color: #ffda4f;
}
.communutyText {
  margin-left: 2rem;
  color: white;
  font-size: 2rem;
}

.communityModal{
  height: 60vh;
}
#modal-1{
  top: 10vh;
  color: white;

}
.modal-header{
  border-bottom: none !important;
}
.modal-footer{
  border-top: none !important;
}
.modal-content{
  background-color: rgb(63, 63, 63) !important;
}
#modal-1___BV_modal_header_ > button{
  background-color: rgb(63, 63, 63);
  border: none;
  font-size: 3rem;
}
#textarea-no-resize{
  font-size: 2rem;
  color: black;
  font-weight: bold;
}

</style>