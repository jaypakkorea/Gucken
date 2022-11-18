<template>
  <div>
    <img id="Addcard" alt="Vue logo" :src="link_url" />
  </div>
</template>

<script>
export default {
  name: "AddCardDiv",
  data() {
    return {
        link_url: `https://image.tmdb.org/t/p/original/${this.topmovie}`,
    };
  },
  props:{
    topmovie:String
  },

};
</script>

<style>
#Addcard{
  opacity: 0.8;
  width: 80%;
  object-fit: cover;
  border-radius: 10px;
  margin: 20px;
}
</style>