<template>
  <div v-b-modal ="this.actor.name">
    <img class="detail_actors_img_crop" alt="Vue logo" :src="link_url" />
    <b-modal ref="my-modal" hide-footer size="xl" :id="this.actor.name">
      <iframe class="actoriframe" :src="iframe_url" frameborder="0"></iframe>
      
    </b-modal>
  </div>
</template>

<script>
export default {
  name: "actorImgCard",
  data() {
    return {
        link_url: `https://image.tmdb.org/t/p/original/${this.actor.profile_path}`,
        iframe_url:`https://www.themoviedb.org/person/${this.actor.pk}-${this.actor.name.replace(/ /g,'-')}?language=ko`
      };
  },
  props:{
    actor:String,
  },

};
</script>

<style>
.actoriframe{
  width: 100%;
  height: 80vh;
}
#Michael\ Caine___BV_modal_header_ > button{
  background-color: transparent;
  border: none;
  font-size: 3rem;
  margin-top: -10px;
}
</style>