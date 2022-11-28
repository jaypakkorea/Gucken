<template>
  <div class="loginDiv">
    <div class="loginLogo">LOGIN</div>
    <div class="loginSenterDiv">
      <div class="loginInputDiv">
        <div>E-MAIL</div>
        <input  v-model="username" class="loginInput" type="email" />
      </div>
      <div class="loginInputDiv">
        <div>PASSWORD</div>
        <input v-model="password" @keyup.enter="logIn" class="loginInput" type="password" />
      </div>
      <div class="loginInputDiv">
        <b-button @click="logIn" variant="warning" class="loginButton">LOGIN</b-button>
      </div>
      <!-- <div class="loginFindDiv">
        <div class="FindTitle">이메일 찾기</div>
        <div class="FindTitle">비밀번호 찾기</div>
      </div> -->
      <div class="loginInputDiv">
        <!-- <router-link :to="{ name: 'SearchDetailView' }"> -->
          <b-button
            style="margin-top:4rem; opacity:0.5;"
            variant="light"
            class="loginButton"
            :to="{ name: 'userSignUp' }"
          >간편 회원가입</b-button>
        <!-- </router-link> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginUser",
  data() {
    return {
      email: null,
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
};
</script>

<style>
.loginLogo {
  padding: 2rem;
  font-size: 5rem;
}
.loginDiv {
  color: white;
}
.loginInputDiv {
  margin: 2rem auto;
  width: 400px;
}
.loginInput {
  font-family: 'Courier New', Courier, monospace;
  width: 400px;
  font-size: 2rem;
  background: none;
  border: 2px solid white;
  border-radius: 5px;
  color: white;
}
.loginSenterDiv {
  padding: 2rem auto;
}
.loginButton {
  width: 300px;
  margin-left: 50px;
  height: 50px;
  line-height: 40px !important;
}
.loginFindDiv {
  display: flex;
  width: 400px;
  margin: 0 auto;
  justify-content: center;
}
.FindTitle {
  margin: 0 2rem;
}
</style>
