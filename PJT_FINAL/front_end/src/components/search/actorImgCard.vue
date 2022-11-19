<template>
  <div v-b-modal.modal-actor >
    <img class="detail_actors_img_crop" alt="Vue logo" :src="link_url" />
    <b-modal ref="my-modal" hide-footer size="lg" id="modal-actor">
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
</style>