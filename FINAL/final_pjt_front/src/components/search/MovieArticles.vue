<template>
  <div>
    <div class="detailCommunityDiv">
      <div class="CommunitysDiv">
        <div
          v-b-modal="article.pk + '가나다'"
          class="CommunityDiv"
          v-for="article in articles"
          :key="article.pk"
        >
          <!-- <divstyle="display:flex; border:1px solid red;"> -->
          <avatarProfile :article="article.user" />
          <div class="communutyText">
            {{ article.user.username.split("@")[0] }}
          </div>

          <div class="d-flex justify-content-between" style="width: 100%">
            <div class="communityTitle2">{{ article.title }}</div>
          </div>
          <div class="communityScore" >💓{{article.like_user_count}}</div>
          <div class="communityScore"> ⭐ {{ article.rate }} </div>
        <div class="communityDate">
          {{ article.created_at.split("T")[0].replace(/-/g, " / ") }}
        </div>
        
          <commentList :article="article" :count="article.like_user_count" />

          <!-- </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import avatarProfile from "./avatarProfile.vue";
import commentList from "./commentList.vue";

export default {
  name: "MovieArticles",
  props: {
    articles: Array,
  },
  data() {
    return {
      recontent: null,
    };
  },
  methods: {},
  components: { avatarProfile, commentList },
  computed: {
    userProfile() {
      if (this.article.user.profile_pic) {
        return `http://localhost:8000${this.article.user.profile_pic}`;
      } else {
        return "http://localhost:8000/media/profile/images/default.jpg";
      }
    },
  },
};
</script>

<style>
</style>