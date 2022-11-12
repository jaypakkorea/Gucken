<template>
  <div id="app">
    <Sidebar/>
    <section>
      <div class="mainVideo">
        <video muted autoplay loop>
          <source src="./assets/mainVideo2.mp4" type="video/mp4" />
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

      <carousel-3d class="carousel">
        <slide :index="0"><img alt="Vue logo" src="./assets/logo.png"/></slide>
        <slide :index="1"><img alt="Vue logo" src="./assets/NBLpng.png"/></slide>
        <slide :index="2"><img alt="Vue logo" src="./assets/logo.png"/></slide>
        <slide :index="3"><img alt="Vue logo" src="./assets/NBLpng.png"/></slide>
        <slide :index="4"><img alt="Vue logo" src="./assets/logo.png"/></slide>
      </carousel-3d>
    </section>
  </div>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";
import Sidebar from "@/components/sidebar/Sidebar"

export default {
  name: "App",
  components: {
    Carousel3d,
    Slide,
    Sidebar,
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
  width: auto;
  height: 100%;
  position:relative;
  right :10%;
}

.mainVideo {
  width: auto;
  height: 100vh;
  overflow: hidden;
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
.carousel{
  margin-bottom : 4rem;
}

.header__overlay {
  background-image: -webkit-gradient(
    linear,
    left top,
    left bottom,
    color-stop(10%, rgba(0, 0, 0, 0.7)),
    color-stop(10%, rgba(0, 0, 0, 0))
  );
  background-image: -webkit-linear-gradient(
    top,
    rgba(0, 0, 0, 0.7) 10%,
    rgba(0, 0, 0, 0)
  );
  background-image: -o-linear-gradient(
    top,
    rgba(0, 0, 0, 0.7) 10%,
    rgba(0, 0, 0, 0)
  );
  background-image: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.7) 10%,
    rgba(0, 0, 0, 0)
  );
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
