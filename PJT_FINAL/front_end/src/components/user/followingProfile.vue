<template>
    <div >
      <b-avatar badge button size="3rem" @click="onClick" :src="userProfile">
      </b-avatar>
      {{following.username.split('@')[0]}}
    </div>
  </template>
  
  <script>
  export default {
      name : 'followingProfile',
      props: {
        following: Object,
      },
      computed: {
      userProfile(){
        if (this.following.profile_pic) {
          return `http://localhost:8000${this.following.profile_pic}`  
        } else {
          return 'http://localhost:8000/media/profile/images/default.jpg'
        }
      }
      } 
  }
  </script>
  
  <style>

  </style>