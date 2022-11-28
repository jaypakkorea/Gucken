<template>
  <div style="margin:auto 10px;">
    <router-link :to="{ name: 'userProfile', params: { userid: userId } }">
      <b-avatar  button @click="onClick" :src="userProfile"></b-avatar>
    </router-link>
  </div>
</template>

<script>
export default {
	name : 'avatarProfile',
	props: {
		article: Object,
	},
	computed: {
    userProfile(){
      if (this.article.profile_pic) {
        return `http://localhost:8000${this.article.profile_pic}`  
      } else {
        return 'http://localhost:8000/media/profile/images/change.jpg'
      }
    },
    userId () {
      return this.article.pk
    }
	} 
}
</script>

<style>

</style>