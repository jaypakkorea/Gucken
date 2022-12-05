<template>
  <b-modal
    centered
    ref="my-modal"
    hide-footer
    size="xl"
    :id="article.pk + '가나다'"
  >
    <div class="communityDetailModal">
      <div class="d-flex">
        <div class="communityDetailTitle">{{ article.title }}</div>
        <b-button
        v-if="article.user.pk === this.$store.state.currentUser.pk"
          class="communityDetailDelete"
          @click="deleteArticle"
          variant="outline-secondary"
          size="sm"
          ><font-awesome-icon icon="fa-solid fa-trash"
        /></b-button>
      </div>

      <div class="communityDetailDate">
        작성자 : {{ article.user.username.split("@")[0] }}
      </div>
      <div class="communityDetailDate">
        {{ article.created_at.split("T")[0].replace(/-/g, " / ") }}
      </div>
      <div class="communityDetailContent">
        <div>{{ article.content }}</div>
        <!-- <b-button variant="secondary" size="sm">edit</b-button> -->
      </div>
      <div class="communityLike">
        <!--  좋아요 안 한 사람 -->
        <div
          @click="likeCommunity"
          v-if="!communityLike"
          class="likeButton"
          style="color: gray"
        >
          <font-awesome-icon icon="fa-solid fa-heart" />
        </div>
        <!-- 좋아요 한 사람은 -->
        <div @click="likeCommunity" v-if="communityLike" class="likeButton">
          <font-awesome-icon icon="fa-solid fa-heart" />
        </div>
        <div style="text-align: left; ">
          {{ this.likecount }} 명이 이 게시글을 좋아합니다.
        </div>
      </div>
      <div>
        <div class="communityDetailListDiv" style="font-size: 1rem; margin-top:2rem ;">댓글 목록</div>
        <div
          style="margin-bottom: 1rem"
          v-for="comment in comments"
          :key="comment.pk"
        >
          <!-- <commentProfile/> -->
          <div class="d-flex">
            <div><commentProfile :comment="comment" /></div>
            <div
              class="d-flex"
              style="
                margin-left: 1rem;
                margin-top: 0.3rem;
                width: 100%;
                justify-content: space-between;
              "
            >
              <div>
                <div style="font-size: 0.8rem">
                  {{ comment.user.username.split("@")[0] }}
                </div>
                <div style="font-size: 0.7rem">
                  {{ comment.created_at.split("T")[0].replace(/-/g, " / ") }}
                </div>
              </div>
            </div>
          </div>
          <div style="margin-top: 0.5rem; font-weight: bold">
            {{ comment.content }}
          </div>
        </div>
      </div>
      <div>
        <b-form-textarea
          v-model="recontent"
          size="lg"
          placeholder="댓글을 입력하세요"
          no-resize
          rows="3"
          id="textarea-no-resize2"
          type="text"
          @keyup.enter="addReCommunity"
        ></b-form-textarea>
        <div style="display: flex; justify-content: right">
          <b-button v-on:click="addReCommunity"
            ><font-awesome-icon icon="fa-solid fa-paper-plane"
          /></b-button>
        </div>
      </div>
    </div>
  </b-modal>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";
import commentProfile from "./commentProfile.vue";

export default {
  name: "commentList",
  data() {
    return {
      recontent: null,
      comments: null,
      communityLike: false,
      RecommunityLike: false,
      likecount: this.count,
    };
  },
  components: { commentProfile },
  props: {
    article: Object,
    count: Number,
  },
  computed: {
    userProfile() {
      if (this.following.profile_pic) {
        return `http://localhost:8000${this.following.profile_pic}`;
      } else {
        return "http://localhost:8000/media/profile/images/default.jpg";
      }
    },
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  created() {
    this.readComments();
  },
  watch: {
    communityLike: {
      handler: function () {
        if (this.communityLike) {
          this.likecount++;
        } else {
          this.likecount--;
        }
      },
    },
  },

  methods: {
    deleteArticle() {
      const API_URL = "http://127.0.0.1:8000";
      axios({
        method: "delete",
        url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/${this.article.pk}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.comments = res.data;
          this.$refs["my-modal"].hide();
          window.location.reload(true);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    readComments() {
      const API_URL = "http://127.0.0.1:8000";
      axios({
        method: "get",
        url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/${this.article.pk}/comments/`,
      })
        .then((res) => {
          this.comments = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addReCommunity() {
      const API_URL = "http://127.0.0.1:8000";
      const recontent = this.recontent;
      if (!recontent) {
        Swal.fire("댓글을 입력해주세요", "", "error");
        return;
      }
      if (!this.isLogin) {
        Swal.fire('로그인이 필요한 서비스 입니다', '', 'error')
        this.$router.push({name:'user'})
      }

      axios({
        method: "post",
        url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/${this.article.pk}/comments/`,
        data: {
          content: this.recontent,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.comments = res.data;
          this.recontent = null;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    likeCommunity() {
      if (!this.isLogin) {
        Swal.fire("로그인이 필요한 서비스 입니다", "", "error");
        this.$router.push({ name: "user" });
      } else {
        const API_URL = "http://127.0.0.1:8000";
        axios({
          method: "post",
          url: `${API_URL}/movies/${this.$route.params.moviePk}/articles/${this.article.pk}/comments/like/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            console.log(res);
            this.communityLike = !this.communityLike;
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
};
</script>

<style>
.communityLike {
  margin-top: -3rem;
  text-align: end;
  margin-bottom: 1rem;
}
.likeButton {
  color: red;
  font-size: 2rem;
  background-color: transparent;
  border: none;
}
.communityDetailDelete {
  color: red;
  height: 30px;
  width: 30px;
}
.communityDetailDate {
  font-size: 0.8rem;
  /* margin-top: 0rem; */
  text-align: left;
}
.communityDetailModal {
  background-color: aliceblue;
  width: 80%;
  margin: 0 auto;
  border-radius: 10px;
  padding: 3rem;
  margin-bottom: 3rem;
}
.communityDetailTitle {
  width: 100%;
  font-size: 3rem;
  /* margin-bottom: 3rem; */
  font-weight: bold;
  word-wrap:break-word;
  word-break:break-all;
}
.communityDetailContent {
  width: 100%;
  font-size: 1.5rem;
  font-weight: bold;
  margin: 3rem 0;
  display: flex;
  justify-content: space-between;
  word-wrap:break-word;
  word-break:break-all;
}
.communityDetailListDiv {
  font-size: 1.5rem;
  color: gray;
  margin-bottom: 1rem;
}
#textarea-no-resize2 {
  margin: 3rem 0 2rem 0;
}
.recommendMovieTitle {
  min-width: 150px;
  max-width: 150px;
  margin: auto 0;
  font-size: 1.5rem;
}
</style>