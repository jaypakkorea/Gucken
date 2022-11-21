<template>
  <div>
    <div class="detailCommunityDiv">
        <div class="CommunitysDiv">
            <div v-b-modal="article.id+'가나다'"  class="CommunityDiv" v-for="article in movie.ratings" :key="article.id">
              <!-- <divstyle="display:flex; border:1px solid red;"> -->
                <avatarProfile :article="article.user" />
                <div class="communutyText">{{article.user.username.split('@')[0]}}</div>
                  <div class="communityScore">{{article.rate}}</div>
                <div style="margin-right:20px;">{{article.title}}</div>
                <div style="margin-right:20px;">{{article.content}}</div>

                <div >{{article.created_at.split('T')[0].replace(/-/g,' / ')}}</div>
                
                <b-modal centered ref="my-modal" hide-footer size="xl" :id="article.id+'가나다'">
                  <commentList :article=article />
                  <!-- <div class="communityDetailModal">
                    <div  class="communityDetailDate">{{article.created_at.split('T')[0].replace(/-/g,' / ')}}</div>
                    <div  class="communityDetailDate">작성자 : {{article.user.username.split('@')[0]}}</div>

                  <div class="communityDetailTitle">{{article.title}} </div>
                  <div class="communityDetailContent">
                    <div>{{article.content}} </div>
                  </div>
                  <div>
                    <div class="communityDetailListDiv">댓글 목록</div>
                    <div> 댓글1</div>
                    <div> 댓글2</div>
                    <div>{{article.id}}</div>
                  </div>
                  <div>
                    <b-form-textarea v-model="recontent" size="lg" 
                      placeholder="댓글을 입력하세요"
                      no-resize rows="3" 
                      id="textarea-no-resize2" 
                      type="text" 
                      @keyup.enter="addReCommunity"
                      ></b-form-textarea>
                      <div style="display:flex; justify-content:right;">
                      <b-button v-on:click="addReCommunity">작성</b-button>
                      </div>
                  </div>
                  </div> -->
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
      movie : Object
    },
    data() {
    return {
      articles: this.movie.ratings,
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