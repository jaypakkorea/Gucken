<template>
  <div class="detail_main_div">
    <router-link class="homeTag" :to="{ name: 'search' }">
      <font-awesome-icon icon="fa-solid fa-angle-left" /> BACK
    </router-link>
    <div class="detail_div">
      <div class="detail_left_div">
        <p>{{this.movie}}</p>
        <div class="detail_title">{{this.movie.title}}</div>
        <div class="detail_flexdiv">
          <div>2018</div>
          <!-- <div> Top 10 Movie </div> -->
          <b-button variant="warning">Add List</b-button>
        </div>
        <div style="width: 80%;">내용이야다무엠누람누이라ㅜㅁㄴ이룸ㄴㅇㅎ무넹훔ㄴㅇㄹ'ㅏㅁㅎ/ㄴㅇ;ㅏㅠ니뮹내용이야다무엠누람누이라ㅜㅁㄴ이룸ㄴㅇㅎ무넹훔ㄴㅇㄹ'ㅏㅁㅎ/ㄴㅇ;ㅏㅠ니뮹</div>
        <div class="detail_actors">
            <div class="detail_actors_img" v-for="gg in 3" :key="gg">
              <img class="detail_actors_img_crop" src="https://image.tmdb.org/t/p/original/qSizF2i9gz6c6DbAC5RoIq8sVqX.jpg" alt="">
              이미현
            </div>
        </div>
        <div class="detail_rate">
          <div>
            <div style="font-size:3rem;">MOVIE</div>
            <div style="color:gray;">DRAMA / ROMANCE / MUSIC</div>
          </div>
          <!-- 내 평점 -->
          <div>
            <div style="font-size:3rem;">10.0</div>
            <div style="color:gray;">MyRATE</div>
          </div>
          <!-- DB 평점 -->
          <div>
            <div style="font-size:3rem;">7.2</div>
            <div style="color:gray;">RATE</div>
          </div>
        </div>
      </div>
      <div  class="detail_right_div">
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
    <b-tab title="COMMUNITY" >
      <div class="detailCommunityDiv">
        <div class="CommunitysDiv">
          <div class="CommunityDiv" v-for="ss in 5" :key="ss">
            <img class="communityUserImg" src="../../assets/starisborn.jpg" alt="">
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
import axios from 'axios'

export default {
  name:'DetailVue',
  props : {
    movie : Object,
    
  },
  data() {
    return {
      myKeyword: this.movie,
      urlList:[],
      video:[],
      VideoData:'',
      myApi:'',
      myAPIList: ['AIzaSyDvjcb7odUilSZEcCyXBY2rX9z0fTYYWvQ',
      'AIzaSyDAes3uWN2F5a2_2EHBBFuIm0Ctv8Hpj1A',
      'AIzaSyCN9uPuXJyXoVjTvkOA8g5ivcUGsGKDiK8',
      // 'AIzaSyATqBywB8sPKs2PrAv_FMEp4Xy7OWzqXOI',
      'AIzaSyDEgtL7oYOo_OJBvIqq2MJhVxDV-IYwekc',
      'AIzaSyBLMEBNxzyohh-zUFGFvHA5ZpI-TLmM4JE',
      'AIzaSyDd-ndJ5GJOKwdBhILSGmAmDneCZEnzrKw'],
      tabIndex: 0,
    };
  },
  methods : {
    pick(){
      const idx = Math.floor(Math.random() * this.myAPIList.length)
      this.myApi = this.myAPIList[idx];
    },
    InputGetEvent(keyword){
      this.myKeyword = keyword
      const baseURL = "https://www.googleapis.com/youtube/v3/search"
      // const API_KEY = 'AIzaSyCN9uPuXJyXoVjTvkOA8g5ivcUGsGKDiK8'
    axios
      .get(baseURL, {
        params: {
          key:  this.myApi ,
          part: "snippet",
          type: "video",
          q: this.myKeyword+'공식 예고편',
          maxResults:1
        }
      })
      .then(response => {
        this.video = response.data.items[0]
        console.log(this.video);
        this.VideoData = `https://www.youtube.com/embed/${response.data.items[0].id.videoId}?autoplay=1&mute=1`
      })
      .catch((error)=>{
        console.log('something wrong!')
        console.log(error)
      })
    },
  },
  created(){
    // this.pick()
    // this.InputGetEvent(this.myKeyword)
  }
}
</script>

<style>
.detail_main_div{
  padding-top: 2rem;
  width: 100%;
  height: fit-content;
  min-height: 100vh;
  position: relative;
  z-index: 1;
}
.detail_main_div::after{
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
          ), url(https://image.tmdb.org/t/p/original/75aHn1NOYXh4M7L5shoeQ6NGykP.jpg);
        background-size: cover;  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  filter: grayscale(100%);
  opacity: 0.8;
}
.nav-link{
  color: white !important;
}
.nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link.active{
  color: black !important;
}
.homeTag{
  text-decoration: none;
  color: rgb(151, 148, 148);
  margin-left: 2rem;
}
.detail_div{
  display: flex;
  font-family: Staatliches;
  color: white;
}
.detail_left_div{
  width: 35%;
  margin: 0 50px;
}
.detail_flexdiv{
  display: flex;
  justify-content: space-between;
  width: 70%;
  margin: 40px;
}
.detail_actors{
  display: flex;
  /* justify-content: space-between; */
  margin: 2rem 0;
}
.detail_rate{
  display: flex;
  justify-content: space-between;
  margin: 4rem 0;
  width: 60%;
  min-width: 400px;
}
.detail_actors_img{
  padding: 0;
  margin: 0;
  width: 120px;
  display: flex;
  flex-direction: column;
  text-align: center;
  margin: 0 10px;
  filter: grayscale(100%);
}
.detail_actors_img_crop{
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 100%;
  margin: 0 auto;
}
.detail_right_div{
  width: 65%;
  margin-right: 50px;
} 
.detail_title{
  margin-top: 3rem;
  font-size: 7rem;
  width: 70%;
}

.detailCommunityDiv{
  margin-top: 50px;
  width: 100%;
  min-height: 500px;
  padding-top: 1rem;
  position: relative;
  z-index: 1;
}
.detailCommunityDiv::after{
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


.CommunitysDiv{
  margin: 20px 50px;
}
.CommunityDiv{
  border: 1px solid white;
  border-radius: 5px;
  margin: 10px 0;
  padding: 10px 20px;
  display: flex;
}
.communityUserImg{
  width: 50px;
  height: 50px;
  border-radius: 100%;
  margin-right: 2rem;
}
.communityScore{
  color: black;
  font-size:2rem;
  padding: 0 20px;
  border-radius: 5px;
  z-index: 10;
  background-color: rgb(211, 209, 209);
}
.communityScoreHigh{
  color: black;
  font-size:2rem;
  padding: 0 20px;
  border-radius: 5px;
  z-index: 10;
  background-color: #ffda4f;
}
.communutyText{
  margin-left: 2rem;
  color: white;
  font-size:2rem;
}
</style>