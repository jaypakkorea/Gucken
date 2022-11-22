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
    {{ follower.username.split("@")[0] }}
  </div>
</template>
  
  <script>
export default {
  name: "followerProfile",
  props: {
    follower: Object,
  },
  computed: {
    userProfile() {
      if (this.follower.profile_pic) {
        return `http://localhost:8000${this.follower.profile_pic}`;
      } else {
        return "http://localhost:8000/media/profile/images/default.jpg";
      }
    },
    userId() {
      return this.follower.id;
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