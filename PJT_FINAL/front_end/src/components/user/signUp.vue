<template>
  <div class="loginDiv">
    <div class="loginLogo">SIGN UP</div>
    <div class="loginSenterDiv">
      <div class="loginInputDiv">
        <v-img  :src="profile_pic"
            contain height="150px" width="200px" style="border: 2px solid black; margin-left:100px;"/>
        <input  @change="onInputImage"  type="file" accept="image/*" />
        {{profile_pic.url}}
      </div>
      <div class="loginInputDiv">
        <div>E-MAIL</div>
        <input v-model="username" class="loginInput" type="email" />
      </div>
      <div class="loginInputDiv">
        <div>PASSWORD</div>
        <input  v-model="password1" class="loginInput" type="password" />
      </div>
      <div class="loginInputDiv">
        <div>PASSWORD CHECK</div>
        <input v-model="password2" @keyup.enter="signUp" class="loginInput" type="password" />
      </div>
      <div  class="loginInputDiv">
        <b-button @click="signUp" variant="warning" class="loginButton">회원가입</b-button>
      </div>
      <div class="loginFindDiv">
        <div class="FindTitle">이메일 찾기</div>
        <div class="FindTitle">비밀번호 찾기</div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name:'signUp',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      profile_pic: ''
    }
  },
  methods: {
    signUp() {
      console.log(this.username)
      console.log(this.profile_pic)
      const payload = new FormData();
      payload.append('username', this.username)
      payload.append('password1', this.password1)
      payload.append('password2', this.password2)
      payload.append('profile_pic', this.profile_pic)

      console.log(payload, '2')
      console.log(this.profile_pic, '3')
      this.$store.dispatch('signUp', payload)
    },
    onInputImage(e){
      this.profile_pic = e.target.files[0]
      console.log(this.profile_pic, '1')
    }
  }
}
</script>

<style>

</style>