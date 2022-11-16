<template>
  <div id="app">
    <nav >
      <div class="navDiv">
      <div>
        <router-link to="/home">
          <font-awesome-icon icon="fa-solid fa-house" />
        </router-link>
      </div>
      <div>
        <router-link to="/search">
          <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
        </router-link>
      </div>
      <div>
        <router-link to="/chart">
          <font-awesome-icon icon="fa-solid fa-video" />
        </router-link>
      </div>
      <div>
        <router-link to="/user">
          <font-awesome-icon icon="fa-solid fa-circle-user" />
        </router-link>
      </div>
    </div>
    </nav>
    <router-view />
  </div>
</template>

<style>
body {
  margin: 0;
  padding: 0;
}

#app {
  width: 100%;
}

nav {
  background-color: black;
  padding-top: 10px;
  width: 50px;
  text-align: center;
  height: 100vh;
  z-index: 5;
  position: fixed;
}
.navDiv{
  height: 350px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  z-index: 6;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-active {
  color: #ffda4f;
}

</style>
