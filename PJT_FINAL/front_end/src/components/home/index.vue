<template>
  <div>
    <div class="bg-overlay"></div>
    <div class="mainVideo min-w-full min-h-full">
      <video muted autoplay loop class="w-full h-full">
        <source
          src="../../assets/mainVideo2.mp4"
          type='video/mp4;'
        />
      </video>
    </div>

    <div class="mainSection">
      <div
        data-aos="fade-up"
        data-aos-ease="ease"
        data-aos-duration="2000"
        data-aos-delay="1000"
      >
        <p class="avatarTitle">AVATAR : <br />THE WAY OF WATER</p>
        <div class="avatarHead">
          <b-button variant="secondary" size="sm">ALL</b-button>
          <p style="margin-left: 3rem">2022</p>
        </div>
        <p class="avatarText">
          A musician helps a young singer find fame as age and alcoholism send
          his <br />
          own career into a downward spiral.
          <br />
        </p>
        <div class="avatarButtons">
          <b-button variant="warning">Watch</b-button>
          <div>
            <b-button variant="secondary" style="margin-right: 2rem"
              >Detail</b-button
            >
            <b-button variant="secondary">Add List</b-button>
          </div>
        </div>
      </div>
    </div>
    <IndexCarousel2D/>
  </div>
</template>
  
<script>
import IndexCarousel2D from './IndexCarousel2D.vue'

export default {
  name: "IndexPage",
  components:{
    IndexCarousel2D
  }
};
</script>
  
<style>
@font-face {
  font-family: Staatliches;
  /* src: url(../../../public/fonts/Staatliches-Regular.ttf); */
  src: url(../../fonts/Staatliches-Regular.ttf);
}
@font-face {
  font-family: Netflix_Medium;
  src: url(../../fonts/Netflix_Medium.woff2);
}


.mainVideo {
  position: absolute;
  /* left: 50px; */
  top : 0;
  width: 100%;
  overflow: hidden;
  margin: 0px;
  object-fit: fill;
  z-index: -1;

}


video {
  /* margin-top: -350px; */
  top : 0;
  width:100%;
  height: 100%;
  position: relative;
  /* border: 3px solid red */
}

.bg-overlay {
  
  display: block;
  position: absolute;
  top: 0;
  width: 100%;
  min-height: 150vh;
  content: " ";
  z-index: -2;
  backface-visibility: hidden;
  background: black;
  background: linear-gradient(77deg, rgba(0, 0, 0, 0.6), transparent 85%);
  opacity: 1;
}
.mainSection {
  color: white;
  text-align: center;
  position: absolute;
  top: 10%;
  left: 10%;
  font-family: Staatliches;
  text-align: left;
  font-size: 5rem;
  z-index: 3;
}

.avatarHead {
  font-family: Staatliches;
  font-size: 1rem;
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: baseline;
  z-index: 3;
}

.avatarText {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 1rem;
  line-height: 1.2rem;
  opacity: 0.8;
  margin-top: 1rem;
}

.avatarButtons {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 4rem;
  font-size: 1rem;
  font-family: Netflix_Medium;
  font-weight: bold;
}
</style>