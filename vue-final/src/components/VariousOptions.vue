<template>
  <div>
    <ProfileChart/>
    <IndexCarousel3D/>
    <HeatMap/>
  </div>
</template>

<script>
import ProfileChart from "@/components/ProfileChart";
import IndexCarousel3D from "@/components/IndexCarousel3D";
import HeatMap from "@/components/HeatMap";


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