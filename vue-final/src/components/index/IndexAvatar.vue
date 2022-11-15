<template>
  <div>
    <div class="bg-overlay"></div>
      <div class="mainVideo min-w-full min-h-full">
        <video muted autoplay loop class="object-cover w-full h-full">
          <source src="../../assets/mainVideo2.mp4" type='video/mp4; codecs="av01.0.00M.08, opus"' />
        </video>
      </div>
      <div class="mainSection">
        <div
          data-aos="fade-up"
          data-aos-ease="ease"
          data-aos-duration="2000"
          data-aos-delay="1000"
        >
          <p class = "avatarTitle" >AVATAR :
            <br>THE WAY OF WATER
          </p>

          <div class = "avatarHead">
            <b-button variant="secondary" size="sm">ALL</b-button>
            <p style = "margin-left : 3rem;">2022</p>
          </div>

          <p class="avatarText"> A musician helps a young singer find fame as age and alcoholism send his 
            <br> own career into a downward spiral.
          </p>

          <div class = "avatarButtons">
            <b-button variant="warning" >Watch</b-button>
            <div>
              <b-button variant="secondary" style="margin-right:2rem;">Detail</b-button>
              <b-button variant="secondary" >Add List</b-button>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
    name : 'IndexAvatar'
}
</script>

<style>

@font-face {
  font-family: Staatliches;
  src: url(../../../public/fonts/Staatliches-Regular.ttf);
}
@font-face {
  font-family: Netflix_Medium;
  src: url(../../../public/fonts/Netflix_Medium.woff2);
}

* {
  margin: 0;
  padding: 0;
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

.bg-overlay {
  display: block;
  position: absolute;
  top: 0;
  right : 26%;
  width: 100%;
  height: 100vh;
  content: ' ';
  z-index: 2;
  backface-visibility: hidden;
  background: black;
  background: linear-gradient(77deg,rgba(0,0,0,.6), transparent 85%);
  opacity: 1;
}

.mainSection {
  color : white;
  text-align: center;
  position: absolute;
  top: 10%;
  left: 10%;
  font-family: Staatliches;
  text-align : left;
  font-size : 5rem;
  z-index: 3;
}

.avatarHead{
  font-family: Staatliches;
  font-size : 1rem;
  display:flex; 
  flex-direction : row;
  justify-content: start;
  align-items: baseline;
  z-index: 3;
}

.avatarText{
  font-family: Arial, Helvetica, sans-serif;
  font-size : 1rem;
  line-height: 1.2rem;
  opacity: 0.8;
  margin-top : 1rem;
}

.avatarButtons{
  display : flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top : 4rem;
  font-size : 1rem;
  font-family: Netflix_Medium;
  font-weight: bold;
}
</style>