import Vue from 'vue'
import VTooltip from 'v-tooltip'
import App from './App.vue'
import store from './store'
import router from './router'
import AOS from 'aos'
import 'aos/dist/aos.css'
import VueCarousel from 'vue-carousel';
import Carousel3d from 'vue-carousel-3d';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHeart, faTrash, faPaperPlane, faPlus, faHouse, faMagnifyingGlass, faVideo, faCircleUser, faAngleLeft, faMedal, faTrophy, faAward, faPowerOff,faChartLine} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'
import VueCalendarHeatmap from 'vue-calendar-heatmap'

library.add( faHeart, faTrash, faPaperPlane, faPlus, faHouse, faMagnifyingGlass, faVideo, faCircleUser, faAngleLeft, faMedal, faTrophy, faAward, faPowerOff,faChartLine)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.use(VueCarousel);
Vue.use(Carousel3d);
Vue.use(BootstrapVue)
Vue.use(VueGlide)
Vue.use(VueCalendarHeatmap)
Vue.use(VTooltip)

new Vue({
  store,
  router,
  render: h => h(App),
  mounted() {
    AOS.init()}
    
}).$mount('#app')
