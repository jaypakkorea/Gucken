<template>
  <div id="app">
    <section>
      <div class="mainVideo">
        <video muted autoplay loop>
          <source src="./assets/mainVideo.mp4" type="video/mp4" />
        </video>
      </div>
      <div class="myguide">
        <div
          data-aos="zoom-in"
          data-aos-ease="ease"
          data-aos-duration="1500"
          data-aos-delay="1000"
        >
          <img
            alt="Vue logo"
            src="./assets/NBLpng.png"
          />
        </div>
      </div>

    <carousel-3d>
      <slide :index="0"> Slide 1 Content </slide>
      <slide :index="1"> Slide 2 Content </slide>
      <slide :index="2"> Slide 2 Content </slide>
      <slide :index="3"> Slide 2 Content </slide>
      <slide :index="4"> Slide 2 Content </slide>
    </carousel-3d>
    </section>

    
  </div>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";

export default {
  name: "App",
  components: {
    Carousel3d,
    Slide,
  },
  methods: {
    popupText() {
      this.$store.dispatch("popupText");
    },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Merienda&display=swap');
@import url('https://fonts.googleapis.com/css?family=Roboto:700,900');




* {
  margin: 0;
  padding: 0;
}

#app {
  background-color:black;
}

video {
  width: 100%;
  height: auto;
  position:relative;

}

.mainVideo {

  width: 100%;
  height: auto;
  /* overflow: hidden; */
  margin: 0px;
  object-fit: fill;
}

.myguide {
  opacity: 0.7;
	text-align: center;
	position: absolute;
	top: 80%;
	left: 50%;
  transform: translate( -50%, -50% );

}

.intro {
  display: flex;
  background: #fff3e2;
  justify-content: space-evenly;
  padding-top: 80px;
  height: 500px;
}
.introDescription {
  font-size: 30px;
  color: #632b2b;
  padding-top: 120px;
}
.introDescription p {
  font-size: 60px;
  color: #632b2b;
  font-weight: 900;
}
.guide1 {
  display: flex;
  background: #ffd4a9;
  justify-content: space-evenly;
  padding-top: 80px;
  height: 500px;
  overflow: hidden;
}
.guide1Description h1 {
  font-size: 48px;
  color: #632b2b;
  padding: 120px 0px 20px 0px;
}
.guide1Description div {
  background: #fff3e2;
  color: #632b2b;
  font-size: 20px;
  padding: 10px;
  border-radius: 10px;
}
.guide2 {
  display: flex;
  background: #fff3e2;
  justify-content: space-evenly;
  padding-top: 80px;
  height: 500px;
  overflow: hidden;
}
.guide2Description h1 {
  font-size: 48px;
  color: #632b2b;
  padding: 120px 0px 20px 0px;
}
.guide2Description div {
  background: #ffd4a9;
  color: #632b2b;
  font-size: 20px;
  padding: 10px;
  border-radius: 10px;
}
footer {
  background: #ffd4a9;
  color: #632b2b;
  padding: 10px;
  text-align: right;
  font-weight: 900;
}
/* responsiveness */
@media screen and (max-width: 500px) {
  .intro {
    display: block;
    padding-top: 10px;
    height: auto;
  }
  .introImage {
    width: 100%;
  }
  .introDescription {
    padding: 30px 0px 0px 20px;
  }
  .guide1 {
    display: block;
    padding-top: 10px;
    height: auto;
  }
  .guide1Image {
    width: 100%;
  }
  .guide1Description {
    padding: 20px;
  }
  .guide1Description h1 {
    padding: 30px 0px;
  }
  .guide2 {
    display: block;
    padding-top: 10px;
    height: auto;
  }
  .guide2Image {
    width: 100%;
  }
  .guide2Description {
    padding: 20px;
  }
  .guide2Description h1 {
    padding: 30px 0px;
  }
}
</style>
