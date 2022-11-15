<template>
  <div>
    <carousel-3d class="carousel">
        <slide :index="0"><img alt="Vue logo" src="../../assets/logo.png"/></slide>
        <slide :index="1"><img alt="Vue logo" src="../../assets/NBLpng.png"/></slide>
        <slide :index="2"><img alt="Vue logo" src="../../assets/logo.png"/></slide>
        <slide :index="3"><img alt="Vue logo" src="../../assets/NBLpng.png"/></slide>
        <slide :index="4"><img alt="Vue logo" src="../../assets/logo.png"/></slide>
    </carousel-3d>
  </div>
</template>

<script>
export default {
    name : 'IndexCarousel3D'
}
</script>

<style>

</style>