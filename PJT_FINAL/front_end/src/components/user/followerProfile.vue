<template>
    <div >
      <b-avatar badge button size="3rem" @click="onClick" :src="userProfile">
      </b-avatar>
      {{follower.username.split('@')[0]}}
    </div>
  </template>
  
  <script>
  export default {
      name : 'followerProfile',
      props: {
        follower: Object,
      },
      computed: {
      userProfile(){
        if (this.follower.profile_pic) {
          return `http://localhost:8000${this.follower.profile_pic}`  
        } else {
          return 'http://localhost:8000/media/profile/images/default.jpg'
        }
      }
      } 
  }
  </script>
  
  <style>

  </style>