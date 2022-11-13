import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import AOS from 'aos'
import 'aos/dist/aos.css'
import VueCarousel from 'vue-carousel';
import Carousel3d from 'vue-carousel-3d';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHouse, faMagnifyingGlass, faVideo, faCircleUser} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'



library.add(faHouse, faMagnifyingGlass, faVideo, faCircleUser)
Vue.component('font-awesome-icon', FontAwesomeIcon)


Vue.config.productionTip = false
Vue.use(VueCarousel);
Vue.use(Carousel3d);
Vue.use(BootstrapVue)
Vue.use(VueGlide)


new Vue({
  store,
  router,
  render: h => h(App),
  mounted() {
  AOS.init()}
  
}).$mount('#app')
