<template>
  <div>
    <!-- 이 창에 들어온 유저가 로그인이 안된상태면 -->
    <!-- <LoginUser/> -->
    <UserInfo/>
  </div>
</template>

<script>
// import LoginUser from './login.vue'
import UserInfo from './userInfo.vue'

export default {
  name:'userIndex',
  components:{
    // LoginUser,
    UserInfo,
  }

}
</script>

<style>

</style>