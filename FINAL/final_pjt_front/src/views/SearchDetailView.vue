<template>
  <div v-if="this.movie" class="SearchContainer">
    <SearchDetailVue :movie="movie" />
  </div>
</template>

<script>
import SearchDetailVue from '@/components/search/SearchDetail.vue';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'DetailView',
  data() {
    return {
      movie: null,
    };
  },
  components: {
    SearchDetailVue,
  },
  async created() {
    await this.getMovieDetail();
  },
  methods: {
    async getMovieDetail() {
      await axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.moviePk}`,
      })
        .then((res) => {
          this.movie = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
.SearchContainer {
  font-family: Staatliches;
}
</style>