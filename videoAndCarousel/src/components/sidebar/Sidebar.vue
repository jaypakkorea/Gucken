<template>
    <div class="sidebar" :style="{ width: sidebarWidth }">
        <font-awesome-icon icon="fa-solid fa-house" />
        <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
        <font-awesome-icon icon="fa-solid fa-video" />
        <font-awesome-icon icon="fa-solid fa-circle-user" />
    </div>
  </template>
  
<script>

export default {
    name : 'Sidebar'
}
</script>


<style>
:root {
  --sidebar-bg-color: rgb(0, 0, 0);
}
</style>


<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);
  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;
  transition: 0.3s ease;
  display: flex;
  flex-direction: column;
  width : 35px;
  justify-content: space-around;
}
</style>
