<template>
  <div class="chartIndexDiv">
    <div class="LankCardDiv">
      <div v-if="this.isLoading"> 
      <div class="lodingDiv"> 
        <b-spinner variant="warning" style="width: 3rem; height: 3rem;" label="Text Centered"></b-spinner>
        <p style="color: #ffc107; margin-top:2rem;">{{this.rodingText}} </p>
      </div>
      </div>
      <div v-if="!this.isLoading">
        <LankIndexCard :recommendmovies="recommendmovies" />
      </div>
    </div>
  </div>
</template>

<script>
  import LankIndexCard from "./cardDiv.vue";
  import axios from "axios";
export default {

  name: "ChartIndex",
  data () {
      return {
          isLoading: true,
          recommendmovies: [],
          rodingText:'내가 좋아요한 영화 찾는중...',
      }
    },
  components: {
    LankIndexCard
  },  

  
  methods: {
    userRecommendMovie(){
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$store.state.currentUser.pk}/recommendation/`,
      })
      .then((res) => {
        this.recommendmovies = res.data
        this.isLoading = false
      })
      .catch((err) => {
        console.log(err)
      })
    },
    isLoadingState(){
      this.isLoading = !this.isLoading 
    },
    
  },
  created() {
    setTimeout(() => this.rodingText = '영화 목록 가져오는 중...', 1500)
    setTimeout(() => this.rodingText = '10,000개 데이터에서 비슷한 영화 찾는중...', 3000)
    setTimeout(() => this.rodingText = '하나씩 머신러닝 돌려 담는 중...', 6000)
    setTimeout(() => this.rodingText = '영화 목록 포장하는 중...', 9000)

    this.userRecommendMovie()
  },
};
</script>

<style>


  .chartIndexDiv {
    padding: 2rem; 
    height: 100vh;
    
  }
  .chartMainButtonDiv{
    height: 15%;
    display: flex;
    flex-direction: column;
    justify-content:space-between;
    width: fit-content;
  }
  .chartMainButton{
    text-align: left;
  }
  .chartSelectButton{
    height: 60px;
  }
  .LankCardDiv{
    max-width: 1200px;
    margin:auto;
  }
  .lodingDiv{
    width: 100%;
    /* height: 80vh; */
    text-align: center;
    margin-top: 300px;
    }
</style>