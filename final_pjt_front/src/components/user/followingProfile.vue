<template>
  <div>
    <router-link :to="{ name: 'userProfile', params: { userid: userId } }">
      <b-avatar
        badge
        button
        size="2rem"
        @click="onClick"
        :src="userProfile"
      ></b-avatar>
    </router-link>
    {{ following.username.split("@")[0] }}
  </div>
</template>
  
  <script>
export default {
  name: "followingProfile",
  props: {
    following: Object,
  },
  computed: {
    userProfile() {
      if (this.following.profile_pic) {
        return `http://localhost:8000${this.following.profile_pic}`;
      } else {
        return "http://localhost:8000/media/profile/images/default.jpg";
      }
    },
    userId() {
      return this.following.id;
    },
  },
  methods: {
    onClick() {
      setTimeout(() => this.$router.go(), 100);
    },
  },
};
</script>
  
  <style>
</style>