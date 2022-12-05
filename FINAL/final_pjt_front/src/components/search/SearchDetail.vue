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
          <b-button v-if="this.movie.like_users.includes(this.$store.state.currentUser.pk) || is_liked"  variant = "outline-warning"
          @click="likeMovie">Cancle</b-button>
          <b-button v-else-if="!this.movie.like_users.includes(this.$store.state.currentUser.pk) || !is_liked" variant = "warning"
          @click="likeMovie">Like</b-button>
        </div>        
        <div style="width: 80%; font-family: BMHANNAAir_ttf; color:darkgray">{{this.movie.overview}}</div>
        <!-- 배우가 없을떄는 v-if로 div 자체가 뜨지 않게 하기 -->
        <div v-if="this.movie.actors" class="detail_actors">
          <!-- for 문으로 배우 리스트 돌면서 이름, 사진 보여주기 -->
          <div class="detail_actors_img" v-for="actor in this.movie.actors" :key="actor.name">
            <actorImgCard :actor="actor"/>
            <p>{{actor.name}}</p>
          </div>
        </div>
        <div class="detail_rate">
          <div>
            <div style="font-size:3rem;">GENRE</div>
            <div class="d-flex">
              <div
                v-for="names in this.movie.genres"
                :key="names"
                style="color:gray;"
              >{{names.name}} /</div>
            </div>
          </div>
          <!-- 내 평점 -->
          <!-- <div>
            <div style="font-size:3rem;">10.0</div>
            <div style="color:gray;">MyRATE</div>
          </div> -->
          <!-- DB 평점 -->
          <div v-if="this.movie.vote_average">
            <div style="font-size:3rem;">{{this.movie.vote_average}}</div>
            <div style="color:gray;">RATE ⭐</div>
          </div>
        </div>
      </div>
      <div class="detail_right_div">
        <b-tabs content-class="mt-2">
          <b-tab title="TRAILER" >
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
          <b-tab title="COMMUNITY" lazy>
            <div class="commumityButtonDiv">
              <b-button v-b-modal.modal-1>
                <font-awesome-icon @click="communnityOpen" class="pluscommunuty" icon="fa-solid fa-plus" />
              </b-button>
              <!-- 모달로 게시글 받는곳 -->
              <b-modal centered class="communityModal" ref="my-modal"   size="xl" id="modal-1" title="게시글 작성">
                <div>
                  <b-form-input v-model="title" style="margin-bottom:30px; font-family: BMJUA;" size="lg" placeholder="제목을 입력하세요"></b-form-input>
                  <b-form-textarea v-model="content" size="lg" placeholder="내용을 입력하세요" style="font-family: BMHANNAAir_ttf;" no-resize rows="5" id="textarea-no-resize" type="text" ></b-form-textarea>
                  <div style="margin-left:35%; margin-top:50px;">
                  <div @mouseleave="showCurrentRating(0)" style="display:inline-block;">
                    <star-rating  :show-rating="false" @current-rating="showCurrentRating" @rating-selected="setCurrentSelectedRating" :increment="0.1"></star-rating>
                  </div>
                  <div style="margin-top:10px; font-weight : bold ;font-family: BMJUA; color:black">{{currentRating}}</div>
                  </div>
                </div>
                <template #modal-footer>
                  <div>
                    <b-button
                    variant="warning"
                      size="xl"
                      class="float-right"
                      @click="addCommunity"
                    ><font-awesome-icon icon="fa-solid fa-paper-plane" /></b-button>
                  </div>
                </template>
              </b-modal>
            </div>
            <div></div>
            <MovieArticles :articles=articles />
          </b-tab>
        </b-tabs>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import StarRating from 'vue-star-rating'
import MovieArticles from "./MovieArticles.vue";
import actorImgCard from"./actorImgCard.vue"
import Swal from 'sweetalert2';

export default {
  name: "DetailVue",
  components: {
    StarRating,
    MovieArticles,
    actorImgCard,
  },
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
        'AIzaSyATqBywB8sPKs2PrAv_FMEp4Xy7OWzqXOI',
        "AIzaSyDEgtL7oYOo_OJBvIqq2MJhVxDV-IYwekc",
        "AIzaSyBLMEBNxzyohh-zUFGFvHA5ZpI-TLmM4JE",
        "AIzaSyDd-ndJ5GJOKwdBhILSGmAmDneCZEnzrKw"
      ],
      tabIndex: 0,
      rating: 0,
    currentRating: 0,
    currentSelectedRating: "점수를 등록해 주세요!",
    boundRating: 3,
    title:null,
    content:null,
    articles : null
    };
  },
  computed : {
    isLogin(){
      return this.$store.getters.isLogin
    },
    realData(){
      return this.$store.getters.isLogin
    }
  },
  methods: {
    // pick() {
    //   const idx = Math.floor(Math.random() * this.myAPIList.length);
    //   this.myApi = this.myAPIList[idx];
    // },
    InputGetEvent(keyword) {
      const baseURL = "https://www.googleapis.com/youtube/v3/search";
      // const API_KEY = 'AIzaSyDvjcb7odUilSZEcCyXBY2rX9z0fTYYWvQ'
      const API_KEY = ''

      axios
        .get(baseURL, {
          params: {
            key: API_KEY,
            part: "snippet",
            type: "video",
            q: keyword + "공식 예고편",
            maxResults: 1
          }
        })
        .then(response => {
          this.video = response.data.items[0];
          this.VideoData = `https://www.youtube.com/embed/${response.data.items[0].id.videoId}?autoplay=1&mute=1`;
        })
        .catch(error => {
          console.log(error);
        });
    },
    likeMovie() {
      if (!this.isLogin) {
        Swal.fire('로그인이 필요한 서비스 입니다', '', 'error')
        this.$router.push({name:'user'})
      } else {
        if(this.movie.like_users.includes(this.$store.state.currentUser.pk)){
          const moviePk = this.movie.id;
          this.$store.dispatch("addList", moviePk);
          this.is_liked = !this.is_liked
        }
        else{
          const moviePk = this.movie.id;
          this.$store.dispatch("addList", moviePk);
          this.is_liked = !this.is_liked
        }
      }

    },
    setRating: function(rating) {
      this.rating =  rating * 2 ;
    },
    showCurrentRating: function(rating) {
      this.currentRating = (rating === 0) ? this.currentSelectedRating : rating* 2;
    },
    setCurrentSelectedRating: function(rating) {
      this.currentSelectedRating =  rating* 2 ;
    },
    communnityOpen(){
      if (!this.isLogin) {
        Swal.fire('로그인이 필요한 서비스 입니다', '', 'error')
        this.$router.push({name:'user'})
      }
    },
    readArticles(){
      const API_URL = 'http://127.0.0.1:8000'
        axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/`,
      })
        .then((res) => {
          this.articles=res.data
        })
        .catch((err) => {
          if (err.response.status === 404) {
            Swal.fire('없는 영화 정보 입니다', '', 'error')
            setTimeout(()=>this.$router.go(-1), 100)
            
  } 
        })
    },
    addCommunity() {
      const API_URL = 'http://127.0.0.1:8000'
        const movie = this.movie.id
        const rate = this.currentRating
        const title = this.title
        const content = this.content
        if (!title) {
          Swal.fire('제목을 입력해주세요', '', 'error')
          return
        } else if (!content) {
          Swal.fire('내용을 입력해주세요', '', 'error')
          return
        } else if (rate<=0) {
          Swal.fire('평점을 남겨주세요', '', 'error')
          return
        }

        axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/`,
        data: {
          movie, rate, title, content
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$router.push({ name: 'SearchDetailView', params: { moviePk: this.movie.id } })
          this.$refs['my-modal'].hide()
          this.readArticles()
          this.title = null
          this.content = null
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.readArticles()
    // this.InputGetEvent(this.movie.title)
    // this.pick()
    setTimeout(()=>this.InputGetEvent(this.movie.title),200) 
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


.detail_main_div {
  padding-top: 2rem;
  width: 100%;
  height: fit-content;
  min-height: 100vh;
  position: relative;
  z-index: 1;
  overflow: auto;
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
  flex-wrap: wrap;
  max-width: 500px;
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
  padding-right: 100px;
}
.detail_title {
  margin-top: 3rem;
  font-size: 7rem;
  font-family: BMDOHYEON;
  /* font-family: BMJUA; */
  /* font-family: BMHANNAAir_ttf; */
}

.detailCommunityDiv {
  width: 100%;
  min-height: 500px;
  padding-top: 1rem;
  position: relative;
  z-index: 1;
  margin: auto 0;
}
.pluscommunuty {
  width: 30px;
  height: 30px;
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
  color: white;
  overflow: hidden;
}
.communityUserImg {
  width: 50px;
  height: 50px;
  border-radius: 100%;
  margin-right: 2rem;
}
.communityScore {
  font-size: 0.8rem;
  margin: auto 0;
  min-width: 50px;
  text-align: left;

  
}
.communityTitle{
  margin: auto 20px;
  font-size:2rem;
  line-height: fit-content;
  word-break: normal;
  word-wrap:break-word;
  word-break:break-all;
  
}
.communityTitle2{
  margin: auto 20px;
  font-size:1.8rem;
  line-height: fit-content;
  word-break: normal;
  word-wrap:break-word;
  word-break:break-all;

}
.communityDate{
  margin: auto 0;
  min-width: 80px;
}
.communityScoreHigh {
  color: black;
  font-size: 2rem;
  padding: 0;
  border-radius: 5px;
  background-color: #ffda4f;
}
.communutyText {
  margin-left: 2rem;
  color: gray;
  font-size: 2rem;
  margin: auto 0;
  font-weight: 100;
}

.communityModal{
  height: 60vh;
}
#modal-1{
  color: white;
}
.modal-header{
  border-bottom: none !important;
}
.modal-footer{
  border-top: none !important;
}
.modal-content{
  /* background-color: rgb(63, 63, 63) !important; */
  width: 90%;
  height: fit-content;
  position: relative;
  z-index: 2;
}
.modal-content::after{
  background-image: url('https://res.klook.com/image/upload/Mobile/City/szhx3ytpgfnhpbmsngk0.jpg');
  background-size:contain;
  background-repeat: no-repeat;
  background-size: cover;
  width: 100%;
  height: 100%;
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  filter: grayscale(50%);
  opacity: 0.5;
}
#modal-1___BV_modal_header_ > button{
  background-color: transparent;
  border: none;
  font-size: 3rem;
  margin-top: -10px;
}
#textarea-no-resize{
  font-size: 2rem;
  color: black;
  font-weight: bold;
}
#modal-1___BV_modal_footer_ > div > button{
  width: 130px;
  height: 50px;
  font-weight: bolder;
  font-size: 1.5rem;
}


</style>