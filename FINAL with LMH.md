# FINAL with LMH



vueCLI + vueBOOTSTRAP + AXIOS + TMDB 활용한 프로젝트

```
https://loy124.tistory.com/296

네이버,구글로 로그인 가능
https://ssungkang.tistory.com/entry/Django-13-%EC%86%8C%EC%85%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B5%AC%ED%98%84-kakaogoogle-fackbook-%EB%93%B1


https://velog.io/@jin0106/Project-%EC%98%81%ED%99%94-%EC%B6%94%EC%B2%9C-%EC%84%9C%EB%B9%84%EC%8A%A4-%EB%A7%8C%EB%93%A4%EA%B8%B0
```



django

```
pip install django-cors-headers
```





**Vuejs 컴포넌트 이름 지을 때에 에러**

```
https://jeongkyun-it.tistory.com/145

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    lintOnSave:false
})
```



**fontawesome **

```
https://happy-jjang-a.tistory.com/123
```





**Animation on Scroll (AoS)**

https://michalsnik.github.io/aos/

https://egghead.io/blog/how-to-use-the-animate-on-scroll-aos-library-in-vue

https://jungkimhoon.tistory.com/17



**vue Carousel 3D**

https://vuejsprojects.com/vue-carousel-3d



**Font import in Vue**

https://www.folkstalk.com/tech/add-a-google-font-to-a-vuejs-with-code-examples/



**alt +  shift + F  **

indentation 자동 맞춤



Vue 

```
//한국어
https://loy124.tistory.com/296

//netflix

https://vuejsexamples.com/netflix-clone-built-using-vue-js/
https://vuejsexamples.com/a-netflix-clone-website-built-with-vue-and-tailwind-css/


//TMDB
https://github.com/hazarbelge/vuejs-the-moviedb-spa?ref=vuejsexamples.com
```





**API **

```
TMDB
2ee130f2ba9bf221b6fe5107cffcac46

YOUTUBE
AIzaSyCN9uPuXJyXoVjTvkOA8g5ivcUGsGKDiK8
AIzaSyDAes3uWN2F5a2_2EHBBFuIm0Ctv8Hpj1A
AIzaSyDvjcb7odUilSZEcCyXBY2rX9z0fTYYWvQ
```



https://creamilk88.tistory.com/194





iframe 높이 화면 맞춤 (출처:https://code-study.tistory.com/35)

```html
<template>
  <div class="VideoDetail">
    <h1>VideoDetail</h1>
    <div class="imagePosition" v-if="video">
      <div class="videoPosition">
        <iframe  class="youtubeFrame" :src="videoUrl" frameborder="0" allowfullscreen></iframe>
      </div>
      <img class="backMonitor" alt="Vue logo" src="../assets/backMonitor.png">
    </div>
  </div>
</template>

<script>
export default {
    name : 'VideoDetail',
    props: {
      video : Object
    },
    computed: {
      videoUrl() {
        const videoId = this.video.id.videoId
        return `https://www.youtube.com/embed/${videoId}`
    },
  }
}
</script>


<style>
.VideoDetail{
  margin-right:5rem;
}

.imagePosition{
  position : absolute;
}

.videoPosition{
  /* display : block;
  position : relative;
  width : 50%;
  height : auto; */
  position : absolute;
  width: 50%;
  height: 0;
  padding-bottom: 56.25%;
}
.videoPosition iframe{
  position : absolute;
  width: 100%;
  height: 60%;
}

.youtubeFrame{
  position : absolute;
  top: 0;
  left : 5px;
  width:98%;
  height : auto;
}

#video {
  position: absolute;
  width: 100%;
  height: 100%;
}

.backMonitor{
  display: block;
  width:50%;
  height: auto;
}
</style>
```

