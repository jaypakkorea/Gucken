<template>
  <b-modal centered ref="my-modal" hide-footer size="xl" :id="article.pk+'가나다'">
    <div class="communityDetailModal">
      <div  class="communityDetailDate">{{article.created_at.split('T')[0].replace(/-/g,' / ')}}</div>
      <div  class="communityDetailDate">작성자 : {{article.user.username.split('@')[0]}}</div>
    <div class="communityDetailTitle">{{article.title}} </div>
    <div class="communityDetailContent">
      <div>{{article.content}} </div>
      <b-button variant="secondary" size="sm">edit</b-button>
      <b-button @click="deleteArticle" variant="secondary" size="sm">delete</b-button>
    </div>
    <div class="communityLike">
      <!--  좋아요 안 한 사람 -->
      <b-button @click="likeCommunity" v-if="!communityLike"  class="likeButton" variant="outline-danger">🤍</b-button>
      <!-- 좋아요 한 사람은 -->
      <b-button @click="likeCommunity" v-if="communityLike"  class="likeButton" variant="outline-danger">❤</b-button>
      <div style="text-align: left;">0 명이 이 게시글을 좋아합니다.</div>
    </div>
    <div>
      <div class="communityDetailListDiv">댓글 목록</div>
      <div style="margin-bottom:1rem;"  v-for="comment in comments" :key="comment.pk">
        <!-- <commentProfile/> -->
        <div class="d-flex ">
          <div><commentProfile :comment="comment" /></div>
          <div class="d-flex" style="margin-left:1rem; margin-top:0.3rem; width: 100%; justify-content:space-between;">
            <div>
              <div style="font-size:0.8rem;">{{comment.user.username.split('@')[0]}}</div>
              <div style="font-size:0.7rem;">{{comment.created_at.split('T')[0].replace(/-/g,' / ')}}</div>
            </div>
            <div>
              <b-button @click="likeRecommunity" v-if="!RecommunityLike"  class="likeButton" size="sm" variant="outline-danger">🤍</b-button>
              <!-- 좋아요 한 사람은 -->
              <b-button @click="likeRecommunity" v-if="RecommunityLike" class="likeButton" size="sm" variant="outline-danger">❤</b-button>
            </div>
          </div>
        </div>
          <div style="margin-top:0.5rem; font-weight: bold;">{{comment.content}}</div>
      </div >
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
        <b-button v-on:click="addReCommunity"><font-awesome-icon icon="fa-solid fa-paper-plane" /></b-button>
        </div>
    </div>
    </div>
  </b-modal>
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
      comments : null,
      communityLike : false,
      RecommunityLike : false,
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
    },
    isLogin(){
      return this.$store.getters.isLogin
    }
  },
  created () {
    this.readComments()
  },
  methods:{
    deleteArticle(){
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/${this.article.pk}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.comments = res.data
          this.$refs['my-modal'].hide()
          window.location.reload(true);
        })
        .catch((err) => {
          console.log(err)
        })
    },
    readComments() {
      const API_URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/${this.article.pk}/comments/`,
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
        url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/${this.article.pk}/comments/`,
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
          this.recontent = null;
        })
        .catch((err) => {
          console.log(err)
        })
    },
    likeCommunity() {
      if (!this.isLogin) {
        Swal.fire('로그인이 필요한 서비스 입니다', '', 'error')
        this.$router.push({name:'user'})
      } else {
        this.communityLike = !this.communityLike;
      }

    },
    likeRecommunity() {
      if (!this.isLogin) {
        Swal.fire('로그인이 필요한 서비스 입니다', '', 'error')
        this.$router.push({name:'user'})
      } else {

        this.RecommunityLike = !this.RecommunityLike;
      }

    },
  }
};
</script>

<style>
.communityLike{
  margin-top: -3rem;
  text-align: end;
  margin-bottom: 1rem;
}
.likeButton{
  color: red;
  font-size: 2rem;
}
</style>