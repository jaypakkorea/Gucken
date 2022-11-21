<template>
  <div class='mylogout'>
    <div class='mylogout'></div>
  </div>
</template>

<script>
import Swal from 'sweetalert2';


export default {
  name: 'LogoutView',
  components: {
  },
  methods: {
    alserMessage(){
      Swal.fire('제목을 입력해주세요', '', 'error')
    },
    logout() {
      this.$store.dispatch('logout')
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
  }
  },
  created() {
    if (this.isLoggedIn) {
      this.logout()
    } else {
      alert('잘못된 접근입니다.')
      this.$router.back()
    }
  }
}
</script>

<style>
.mylogout{
  margin-left: 50px;
  background-color: black;
  min-height: 100vh;
}
</style>