<template>
  <div id="app">
    <nav >
      <div class="navDiv">
      <div>
        <router-link to="/home">
          <font-awesome-icon icon="fa-solid fa-house" />
        </router-link>
      </div>
      <div>
        <router-link to="/search">
          <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
        </router-link>
      </div>
      <div>
        <router-link to="/chart">
          <font-awesome-icon icon="fas fa-chart-line" />
        </router-link>
      </div>
      <div>
        <!-- 로그인 됬으몈 -->
        <!-- <router-link ="isLogin" to="/user/profile/:username"> -->

        <router-link v-if="isLogin" :to="{ name: 'userProfile', params: { userid } }">
          <font-awesome-icon icon="fa-solid fa-circle-user" />
        </router-link>
        <!-- 로그인 안됬으면 -->
        <router-link v-if="!isLogin" to="/user">
          <font-awesome-icon icon="fa-solid fa-circle-user" />
        </router-link>
      </div>
      <div>
        <router-link v-if="isLogin" to="/logout">
          <font-awesome-icon icon="fas fa-power-off" />
          </router-link>
      </div>

    </div>
    </nav>
    <router-view />
  </div>
</template>

<script>


export default {
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    userid() {
      console.log(this.$store.getters.currentUser)
      return this.$store.getters.currentUser.pk
    }
  },
  created() {
    this.userid()
  }
  // methods: {
  //   getArticles() {
  //     if (this.isLogin === true) { 
  //       alert('로그인 되어있음')
  //     } else {
  //       alert('로그인이 필요한 서비스 입니다.')
  //       this.$router.push({ name: 'LogInView'})
  //     }
  //   }
  // }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
}

#app {
  width: 100%;
}

nav {
  background-color: black;
  padding-top: 10px;
  width: 50px;
  text-align: center;
  height: 100vh;
  z-index: 5;
  position: fixed;
}
.navDiv{
  height: 350px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  z-index: 6;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  font-size: 1.5rem;
}

nav a.router-link-active {
  color: #ffda4f;
}
a{text-decoration:none; color: white}
</style>
