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
        <router-link @click.native="loginAlert" to="/chart" >
          <font-awesome-icon icon="fa-solid fa-video" />
        </router-link>

      </div>
      <div>
        <router-link  v-if="isLogin"  :to="{ name: 'userProfile', params: { userid } }" >
          <font-awesome-icon @click="reload" icon="fa-solid fa-circle-user" />
        </router-link>
        <!-- 로그인 안됬으면 -->
        <router-link v-if="!isLogin" to="/user">
          <font-awesome-icon icon="fa-solid fa-circle-user" />
        </router-link>
      </div>
      <div>
        <router-link v-if="isLogin" to="/logout">
          <font-awesome-icon v-b-tooltip.hover.right title="LOGOUT" icon="fas fa-power-off" />
          </router-link>
      </div>

    </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
import Swal from "sweetalert2";

export default {
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    userid() {
      return this.$store.getters.currentUser.pk
    }
  },
  created() {
    this.userid()
  },
  methods: {
    loginAlert() {
      if (!this.isLogin) {
        Swal.fire('로그인이 필요한 서비스 입니다', '', 'error')
        this.$router.push({name:'user'})
    }
  },
  reload(){
    console.log(this.$store.getters.currentUser.pk, 'hi')
    console.log(typeof this.$store.getters.currentUser.pk, 'wow')
  }

}
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
