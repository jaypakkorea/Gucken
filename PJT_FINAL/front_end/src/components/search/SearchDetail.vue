<template>
  <div class="detail_main_div">
    <router-link class="homeTag" :to="{ name: 'search' }">
      <font-awesome-icon icon="fa-solid fa-angle-left" /> BACK
    </router-link>
    <div class="detail_div">
      <div class="detail_left_div">
        <div class="detail_title">{{this.myKeyword}}</div>
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
    <b-tab title="COMMUNITY"><p>I'm the second tab</p></b-tab>
  </b-tabs>
      </div>
    </div>
      
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'DetailVue',
  data() {
    return {
      myKeyword: '블랙팬서2',
      urlList:[],
      video:[],
      VideoData:''
    };
  },
  methods : {
    InputGetEvent(keyword){
      this.myKeyword = keyword
      const baseURL = "https://www.googleapis.com/youtube/v3/search"
      const API_KEY = 'AIzaSyDEgtL7oYOo_OJBvIqq2MJhVxDV-IYwekc'
    axios
      .get(baseURL, {
        params: {
          key: API_KEY,
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
    this.InputGetEvent(this.myKeyword)
  }
}
</script>

<style>

.detail_main_div{
  background: linear-gradient(
            to left,
            rgba(20, 20, 20, 0.5) 10%,
            rgba(20, 20, 20, 0.75) 25%,
            rgba(20, 20, 20, 0.9) 50%,
            rgba(20, 20, 20, 0.9) 65%,
            rgba(20, 20, 20, 1) 80%
          ), url(https://image.tmdb.org/t/p/original/75aHn1NOYXh4M7L5shoeQ6NGykP.jpg);
        background-size: cover;
  padding-top: 2rem;
  height: fit-content;
  min-height: 100vh;
  filter: grayscale(100%);
  opacity: 0.8;
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
</style>