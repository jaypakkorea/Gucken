<template>
  <div class="communityDetailModal">
    <div  class="communityDetailDate">{{article.created_at.split('T')[0].replace(/-/g,' / ')}}</div>
    <div  class="communityDetailDate">작성자 : {{article.user.username.split('@')[0]}}</div>

  <div class="communityDetailTitle">{{article.title}} </div>
  <div class="communityDetailContent">
    <div>{{article.content}} </div>
  </div>
  <div>
    <div class="communityDetailListDiv">댓글 목록</div>
    <div  v-for="comment in comments" :key="comment.pk">
      <!-- <commentProfile/> -->
      <div><commentProfile :comment="comment" /></div>
      <div>{{comment.user.username.split('@')[0]}}</div>
      <div>{{comment.content}}</div>
      <div>{{comment.created_at.split('T')[0].replace(/-/g,' / ')}}</div>
    </div>
  </div>
  <div>
    <b-form-textarea v-model="recontent" size="lg" 
      placeholder="댓글을 입력하세요"
      no-resize rows="3" 
      id="textarea-no-resize2" 
      type="text" 
      @keyup.enter="addReCommunity"
      ></b-form-textarea>
      <div style="display:flex; justify-content:right;">
      <b-button v-on:click="addReCommunity">작성</b-button>
      </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";
import Swal from 'sweetalert2';
import commentProfile from "./commentProfile.vue";


export default {
  name: "commentList",
  data() {
    return {
      recontent : null,
      comments : null
    }
  },
  components: { commentProfile },
  props: {
    article: Object,
  },
  computed: {
    userProfile(){
      if (this.following.profile_pic) {
        return `http://localhost:8000${this.following.profile_pic}`  
      } else {
        return 'http://localhost:8000/media/profile/images/default.jpg'
      }
    }
  },
  created () {
    this.readComments()
  },
  methods:{
    readComments() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/${this.article.id}/comments/`,
      })
        .then((res) => {
          console.log(res.data, 'hiddd')
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    addReCommunity() {
      const API_URL = 'http://127.0.0.1:8000'
      const recontent = this.recontent
      if (!recontent) {
        Swal.fire('댓글을 입력해주세요', '', 'error')
        return} 
      console.log(recontent)

      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/${this.article.id}/comments/`,
        data: {
          content: this.recontent,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res.data, 'hiddd')
          this.comments = res.data
         // this.$router.push({ name: 'SearchDetailView', params: { moviePk: this.movie.id } })
          Swal.fire({
            html: '댓글 작성 성공~🎉',
            confirmButtonText: `확인`,
            confirmButtonColor: '#FFC83A',
            timer: 1500,
            width: 450,
            allowEnterKey: false,
          });
          this.recontent = null;
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
};
</script>

<style>
</style>