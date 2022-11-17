<template>
  <div class="SearchFlexDiv">
    <div class="LeftDiv">
      <div>
        <input
          class="searchInput"
          type="text"
          ref="cursor"
          v-model="keyword"
          @keyup.enter="onInputKeyword"
          placeholder="찾고 싶은 영화를 입력하세요"
        />
      </div>
      <div class="searchSelectDiv">
        <div class="searchSelect">All</div>
        <div class="searchSelect">드라마</div>
        <div class="searchSelect">코미디</div>
        <div class="searchSelect">액션</div>
        <div class="searchSelect">스릴러</div>
        <div class="searchSelect">모험</div>
        <div class="searchSelect">애니메이션</div>
      </div>
    </div>

    <div class="RightDiv" @click="searchDetailPage">
      <!-- for 문으로 detailDiv 여러개 돌릴꺼 -->
      <router-link
        class="routerLink"
        v-for="movie in search"
        :key="movie.pk"
        :to="{ name: 'SearchDetailView' }"
      >
        <div class="detailDiv">
          <div class="detailImgDiv">
            <indexSearchImg :poster_path="movie.poster_path" />
          </div>
          <div>
            <div class="detailTitle">{{ movie.title }}</div>
            <div class="detailOverviewDiv">
              {{ movie.overview }}
            </div>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>
  
  <script>
import indexSearchImg from "./indexSearchImg.vue";
export default {
  name: "SearchPage",
  data() {
    return {
      keyword: "",
    };
  },
  components: { indexSearchImg },
  computed: {
    search() {
      console.log(this.$store.state.search);
      return this.$store.state.search;
    },
    // img_url(){
    //     return  ``
    // }
  },
  methods: {
    onInputKeyword() {
      const movieName = this.keyword;
      console.log(this.keyword);
      this.$store.dispatch("search", movieName);
      this.keyword = null;
      // console.log(movieName)
      // console.log(typeof movieName)
    },
    searchDetailPage() {},
  },
};
</script>
  
  <style>
a,
.routerLink {
  --bs-link-color: none;
  --bs-link-hover-color: none;
  text-decoration: none;
  color: white;
}
.routerLink:hover{
  font-weight: bold;
}
.SearchFlexDiv {
  display: flex;
  margin-left: 3rem;
  color: white;
  width: 100%;
  height: fit-content;
  min-height: 100vh;
  position: relative;
  z-index: 1;
}

.SearchFlexDiv::after{
  width: 100%;
  height: 100%;
  content: "";
  background: linear-gradient(
            to left,
            rgba(20, 20, 20, 0.5) 10%,
            rgba(20, 20, 20, 0.7) 25%,
            rgba(20, 20, 20, 0.8) 50%,
            rgba(20, 20, 20, 0.9) 65%,
            rgba(20, 20, 20, 0.9) 100%
          ), url(  https://image.tmdb.org/t/p/original/s3GFi8SXz3zMOkjzMtRW1Nql8GI.jpg
);
        background-size: cover;  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  filter: grayscale(100%);
  opacity: 0.8;
}


.LeftDiv {
  width: 30%;
  margin-top: 5rem;
  margin-left: 5%;
  padding: 30px;
}
.searchInput {
  min-width: 300px;
  width: 70%;
  padding: 0;
  border: none;
  color: white;
  font-size: 1.5rem;
  border-bottom: 3px solid white;
  background-color: transparent;
  box-shadow: none;
}
.searchSelectDiv {
  width: 270px;
  margin-top: 3rem;
}
.searchSelect {
  margin: 1rem;
  padding: 0.3rem 1rem;
}
.searchSelect:hover {
  border: 1px solid #ffda4f;
  border-radius: 5px;
}
.searchSelect:focus {
  border: 1px solid #ffda4f;
}

.searchInput:focus {
  border: none;
  box-shadow: none;
  border-bottom: 3px solid white;
  outline: none;
}

.RightDiv {
  margin-top: 3rem;
  margin-right: 3rem;
}
.detailDiv {
  display: flex;
  margin: 40px 0;
  max-width: 1200px;
}
.detailImgDiv {
  padding: 0;
  margin-right: 50px;
  width: 200px;
}
.detailImg {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 15%;
  margin: 0 20px;
}

.detailTitle {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 10px;
}
.detailOverviewDiv {
  display: block;
  height: 60px;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: 1.2rem;
  color: gray;
  line-height: 2rem;
}
</style>