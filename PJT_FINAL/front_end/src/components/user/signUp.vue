<template>
  <div class="loginDiv">
    <div class="loginLogo">SIGN UP</div>
    <div class="loginSenterDiv">
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
      <!-- <div class="loginFindDiv">
        <div class="FindTitle">이메일 찾기</div>
        <div class="FindTitle">비밀번호 찾기</div>
      </div> -->
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
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const payload = {
        username,
        password1,
        password2,
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style>

</style>