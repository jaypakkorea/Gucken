<template>
    <div>
        <h1 style="color:red">{{profile.ratings_count}}</h1>

        <div v-for="article in profile.ratings" :key="article.id">
            <p>{{article.title}}</p>
            <p>{{article.rate}}</p>
            <p>{{article.title}}</p>
            <p>{{article.content}}</p>
            <p>{{article.created_at}}</p>
            <p>{{article.movie}}</p>
        </div>
    </div>
  </template>
  
  <script>

  export default {
      name: "ProfileArticles",
      props : {
        profile : Object
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