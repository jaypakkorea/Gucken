<template>
  <div>
    <ProfileChart/>
    <IndexCarousel3D/>
    <HeatMap/>
  </div>
</template>

<script>
import ProfileChart from "@/components/user/ProfileChart";
import IndexCarousel3D from "@/components/index/IndexCarousel3D";
import HeatMap from "@/components/user/HeatMap";


export default {
    name : 'VariousOptions',
    components: {
        ProfileChart,
        IndexCarousel3D,
        HeatMap
    },
}
</script>

<style>

</style>