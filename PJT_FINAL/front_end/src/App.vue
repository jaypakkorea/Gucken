<template>
  <div id="app">
    <nav class="navDiv">
      <div>
        <router-link to="/">
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
    </nav>
    <router-view />
  </div>
</template>

<style>
body {
  margin: 0;

}
#app {

  background-color: rgb(143, 83, 83);
  
}

nav {
  background-color: black;
  padding-top: 10px;
  /* z-index: 100; */
  width: 50px;
}
.navDiv{
  height: 350px;
  display: flex;
  justify-content: space-around;
  flex-direction: column;

}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #ffda4f;
}

</style>
