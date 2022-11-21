<template>
  <div>
    <div class="detailCommunityDiv">
        <div class="CommunitysDiv">
            <div v-b-modal="article.id+'가나다'"  class="CommunityDiv" v-for="article in articles" :key="article.pk">
              <!-- <divstyle="display:flex; border:1px solid red;"> -->
                <avatarProfile :article="article.user" />
                <div class="communutyText">{{article.user.username.split('@')[0]}}</div>
                  <div class="communityScore">{{article.rate}}</div>
                <div style="margin-right:20px;">{{article.title}}</div>
                <div style="margin-right:20px;">{{article.content}}</div>
                <div >{{article.created_at.split('T')[0].replace(/-/g,' / ')}}</div>
                <p>{{article.id}}</p>
                <b-modal centered ref="my-modal" hide-footer size="xl" :id="article.id+'가나다'">
                  <commentList :article=article />
                </b-modal>
              <!-- </div> -->
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import avatarProfile from"./avatarProfile.vue"
import commentList from"./commentList.vue"


export default {
    name: "MovieArticles",
    props : {
      articles : Array
    },
    data() {
    return {
      recontent:null,
    };
  },
  components : {avatarProfile, commentList},
  computed: {
    userProfile(){
      if (this.article.user.profile_pic) {
        return `http://localhost:8000${this.article.user.profile_pic}`  
      } else {
        return 'http://localhost:8000/media/profile/images/default.jpg'
      }
    } 
  },
}
</script>

<style>
.communityDetailDate{
  font-size:1rem;
   margin-top:0.5rem;
    text-align: right;
}
.communityDetailModal{
  background-color: aliceblue;
  width: 80%;
  margin: 0 auto;
  border-radius: 10px;
  padding: 3rem;
  margin-bottom: 3rem;
}
.communityDetailTitle{
  width: 100%;
  font-size: 3rem;
  margin-bottom: 3rem;
  font-weight: bold;
}
.communityDetailContent{
  width: 100%;
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 3rem;
  display: flex;
  justify-content: space-between;
}
.communityDetailListDiv{
  font-size: 1.5rem;
  color: gray;
  margin-bottom: 1rem;
}
#textarea-no-resize2{
  margin: 3rem 0 2rem 0;
}
</style>