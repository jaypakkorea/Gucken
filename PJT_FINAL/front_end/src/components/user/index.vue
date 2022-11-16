<template>
  <div>
    <!-- 이 창에 들어온 유저가 로그인이 안된상태면 -->
    <LoginUser/>
    <!-- <signUp/> -->
  </div>
</template>

<script>
import LoginUser from './login.vue'
// import signUp from './signUp.vue'

export default {
  name:'userIndex',
  components:{
    LoginUser,
    // signUp,
  }

}
</script>

<style>

</style>