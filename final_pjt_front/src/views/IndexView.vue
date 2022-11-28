<template>
    <div class="SearchContainer">
        <IndexPage />
    </div>
</template>

<script>
import IndexPage from '../components/home/index.vue'
export default {
    components:{
        IndexPage,

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