import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'
import SearchView from '../views/SearchView.vue'
import ChartView from '../views/ChartView.vue'
import UserView from '../views/UserView.vue'
import SearchDetailView from '../views/SearchDetailView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/home',
    name: 'index',
    component: IndexView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/search/detial/',
    name: 'SearchDetailView',
    component: SearchDetailView
  },
  {
    path: '/chart',
    name: 'chart',
    component: ChartView
  },
  {
    path: '/user',
    name: 'user',
    component: UserView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
