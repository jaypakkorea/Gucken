<template>
    <router-link :to="{ name: 'userProfile', params: { userid: userId } }">
      <b-avatar badge button size="3rem" @click="onClick" :src="userProfile"></b-avatar>
    </router-link>
</template>

<script>
export default {
  name: "commentProfile",
  props: {
    comment: Object,
  },
  computed: {
    userProfile(){
      if (this.comment.user.profile_pic) {
        return `http://localhost:8000${this.comment.user.profile_pic}`  
      } else {
        return 'http://localhost:8000/media/profile/images/default.jpg'
      }
    },
    userId () {
      return this.comment.user.pk
    }
  },
}
</script>

<style>

</style>