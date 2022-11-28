<template>
  <div>    
    <div v-if="this.movieName.title.length < 6">{{this.movieName.title}}</div>
    <div v-else>{{this.movieName.title.substring(0,6)+'...'}}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name : 'ProfileArticleMovie',
  data(){
    return {
      movieName : null
    }
  },
  props : {
    movie : Number
  },
  methods : {
    readArticles(){
      const API_URL = 'http://127.0.0.1:8000'
        axios({
        method: 'get',
        url: `${API_URL}/profile/${this.movie}/article/`,
      })
        .then((res) => {
          this.movieName=res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created(){
      this.readArticles()
    }
}
</script>

<style>
</style>