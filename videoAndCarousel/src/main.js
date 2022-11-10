import Vue from 'vue'
import App from './App.vue'
import store from './store'
import AOS from 'aos'
import 'aos/dist/aos.css'
import Carousel3d from 'vue-carousel-3d';

Vue.config.productionTip = false
Vue.use(Carousel3d);
new Vue({
  store,
  render: h => h(App),
  mounted() {
  AOS.init()}

}).$mount('#app')

