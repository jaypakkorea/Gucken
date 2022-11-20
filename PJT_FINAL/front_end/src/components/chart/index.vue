<template>
  <div class="chartIndexDiv">
    <LankIndexCard />
  </div>
</template>

<script>
import LankIndexCard from "./cardDiv.vue";

export default {
  name: "ChartIndex",
  components: {
    LankIndexCard
  }
};
</script>

<style>
.chartIndexDiv {
  padding: 3rem;
}
</style>