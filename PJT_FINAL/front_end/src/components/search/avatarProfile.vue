<template>
  <div>
    <b-avatar button @click="onClick" :src="userProfile"></b-avatar>
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
        return 'http://localhost:8000/media/profile/images/default.jpg'
      }
    }
	} 
}
</script>

<style>

</style>