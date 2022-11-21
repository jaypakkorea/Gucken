<template>
    <b-avatar badge button size="3rem" @click="onClick" :src="userProfile"></b-avatar>
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
    }
  },
}
</script>

<style>

</style>