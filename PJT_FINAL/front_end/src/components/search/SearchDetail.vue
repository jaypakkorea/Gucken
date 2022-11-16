<template>
  <div>
    <router-link :to="{ name: 'search' }">
      <font-awesome-icon icon="fa-solid fa-angle-left" /> Home
    </router-link>

      
  </div>
</template>

<script>

export default {
  name:'DetailVue',
}
</script>

<style>
/* .detailDiv{
  background-image: url('../../assets/starisborn.jpg');
    background-repeat:no-repeat ;
} */
.homeTag{
  text-decoration: none;
  color: rgb(151, 148, 148);
  margin-left: 2rem;
}
</style>