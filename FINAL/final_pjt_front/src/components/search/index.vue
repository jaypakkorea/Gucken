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
        <div class="searchSelect" @click="allGenre">All</div>
        <div class="searchSelect" @click="searchGenre(18)">드라마</div>
        <div class="searchSelect" @click="searchGenre(35)">코미디</div>
        <div class="searchSelect" @click="searchGenre(28)">액션</div>
        <div class="searchSelect" @click="searchGenre(53)">스릴러</div>
        <div class="searchSelect" @click="searchGenre(12)">모험</div>
        <div class="searchSelect" @click="searchGenre(16)">애니메이션</div>
      </div>
    </div>

    <div class="RightDiv" @click="searchDetailPage">
      <!-- for 문으로 detailDiv 여러개 돌릴꺼 -->
      <div v-if="!this.listState">
        <router-link
          class="routerLink"
          v-for="movie in GenreMovies"
          :key="movie.pk"
          :to="{ name: 'SearchDetailView', params: { moviePk: movie.pk } }"
        >
          <div class="detailDiv">
            <div class="detailImgDiv">
              <indexSearchImg :poster_path="movie.poster_path" />
            </div>
            <div>
              <div class="detailTitle">{{ movie.title }}</div>
              <div class="detailOverviewDiv">{{ movie.overview }}</div>
              <div class="detailOverviewDiv">{{ movie.release_date }}</div>
            </div>
          </div>
        </router-link>
      </div>
      <div v-if="this.listState">
        <router-link
          class="routerLink"
          v-for="movie in search"
          :key="movie.pk"
          :to="{ name: 'SearchDetailView', params: { moviePk: movie.pk } }"
        >
          <div class="detailDiv">
            <div class="detailImgDiv">
              <indexSearchImg :poster_path="movie.poster_path" />
            </div>
            <div>
              <div class="detailTitle" style="font-family: BMDOHYEON">{{ movie.title }}</div>
              <div class="detailOverviewDiv">{{ movie.overview }}</div>
              <div class="detailOverviewDiv">{{ movie.release_date}}</div>
            </div>
          </div>
        </router-link>
      </div>
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
      listState: 0
    };
  },
  components: { indexSearchImg },
  computed: {
    search() {
      return this.$store.state.search;
    },
    GenreMovies() {
      return this.$store.state.genre;
    }
    // img_url(){
    //     return  ``
    // }
  },
  methods: {
    onInputKeyword() {
      const movieName = this.keyword;
      this.$store.dispatch("search", movieName);
      this.keyword = null;
      this.listState = 1;
    },
    searchDetailPage() {},
    searchGenre(genreId) {
      this.$store.dispatch("searchGenre", genreId);
      this.listState = 0;
    },
    allGenre() {
      this.$store.dispatch("searchGenreAll");
      this.listState = 0;
    }
  },
  created(){
    this.allGenre()
    this.listState = 0;
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


.routerLink {
  --bs-link-color: none;
  --bs-link-hover-color: none;
  text-decoration: none;
  color: white;
}
.routerLink:hover {
  font-weight: bold;
}
.SearchFlexDiv {
  display: flex;
  color: white;
  width: 100%;
  height: fit-content;
  min-height: 100vh;
  position: relative;
  z-index: 1;
}

.SearchFlexDiv::after {
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
    );


  background-size: cover;
  position: absolute;
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
  font-family: BMJUA ;
}
.searchSelectDiv {
  width: 270px;
  margin-top: 3rem;
  cursor : pointer;
}
.searchSelect {
  margin: 1rem;
  padding: 0.3rem 1rem;
  font-family: BMDOHYEON
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
  font-family: BMHANNAAir_ttf;
}
.detailOverviewDiv {
  display: block;
  height: 60px;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: 1.2rem;
  color: gray;
  line-height: 2rem;
  font-family: BMHANNAAir_ttf;
}
</style>