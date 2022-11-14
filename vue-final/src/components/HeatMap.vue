<template>
  <div>
    <calendar-heatmap
      class="mt-5"
      :values="reviewDateCountList"
      :end-date="today"
      :range-color="[
        '#ebedf0',
        '#dae2ef',
        '#c0ddf9',
        '#73b3f3',
        '#3886e1',
        '#17459e',
      ]"
      :max="10"
      tooltip-unit="stars"
    />
  </div>
</template>

<script>
import { CalendarHeatmap } from 'vue-calendar-heatmap'
import "vue-calendar-heatmap/dist/vue-calendar-heatmap.css";

import Vue from 'vue'
Vue.component('calendarHeatmap', CalendarHeatmap)


export default {
  name : 'HeatMap',
  components: {
      CalendarHeatmap
  },
  props: {
    reviewDateCountList: {
      type: Array,
    },
    reviewGenreCountList: {
      type: Array,
    },
    reviewCountList: {
      type: Array,
    },
    genreList: {
      type: Array,
    },
    movieGenreList: {
      type: Array,
    },
  },
}
</script>

<style>

</style>