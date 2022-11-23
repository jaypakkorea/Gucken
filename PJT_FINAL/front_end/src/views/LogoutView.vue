<template>
  <div class="mylogout">
    <div class="mylogout"></div>
  </div>
</template>

<script>
import Swal from "sweetalert2";

export default {
  name: "LogoutView",
  components: {},
  methods: {
    alserMessage() {
      Swal.fire({
        title: "로그아웃 하시겠습니까?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "로그아웃",
        cancelButtonText: "취소"
      }).then(result => {
        if (result.value) {
          this.logout()
          this.$router.push({name:'index'})
        }else{
          this.$router.push({name:'index'})
        }
      });
    },
    logout() {
      this.$store.dispatch("logout");
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },
  created() {
    if (this.isLoggedIn) {
      this.alserMessage();
    } else {
      Swal.fire("잘못된 접근입니다.", '', 'error');
      this.$router.back();
    }
  }
};
</script>

<style>
.mylogout {
  margin-left: 50px;
  background-color: black;
  min-height: 100vh;
  color: white;
}
</style>