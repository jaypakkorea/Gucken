import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'
import SearchView from '../views/SearchView.vue'
import ChartView from '../views/ChartView.vue'
import UserView from '../views/UserView.vue'
import userSignUp from '../views/UserSignUp.vue'
import SearchDetailView from '../views/SearchDetailView.vue'
import userProfile from '../views/UserProfileView.vue'
import LogoutView from '../views/LogoutView.vue'


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
    path: '/movies/:moviePk',
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
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/user/signup',
    name: 'userSignUp',
    component: userSignUp
  },
  {
    path: '/user/profile/:username',
    name: 'userProfile',
    component: userProfile
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
