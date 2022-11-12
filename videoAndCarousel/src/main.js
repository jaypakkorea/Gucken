import Vue from 'vue'
import App from './App.vue'
import store from './store'
import AOS from 'aos'
import 'aos/dist/aos.css'
import Carousel3d from 'vue-carousel-3d';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHouse, faMagnifyingGlass, faVideo, faCircleUser} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* 위에서 import한 아이콘들을 Core library에 등록 */
library.add(faHouse, faMagnifyingGlass, faVideo, faCircleUser)

/* font awesome 컴포넌트를 전역으로 등록 */
Vue.component('font-awesome-icon', FontAwesomeIcon)



Vue.config.productionTip = false
Vue.use(Carousel3d);
new Vue({
  store,
  render: h => h(App),
  mounted() {
  AOS.init()}

}).$mount('#app')

