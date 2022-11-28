<template>
  <div class="SearchContainer">
    <SearchPage/>
  </div>
</template>

<script>
import SearchPage from '../components/search/index.vue' 
export default {
  components:{
    SearchPage,
  }
}
</script>

<style>
.SearchContainer{
  margin-left: 50px;
  background-color: black;
  min-height: 100vh;
}
</style>