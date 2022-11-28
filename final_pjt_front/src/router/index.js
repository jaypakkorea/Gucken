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
// import LikeRecommendation from '../components/chart/LikeRecommendation.vue'
import InputRecommendtion from '../components/chart/InputRecommendtion.vue'
import NotFount404 from "@/views/NotFound_404";
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
  // {
  //   path: '/chart/like',
  //   name: 'LikeRecommendation',
  //   component: LikeRecommendation
  // },
  {
    path: '/chart/input',
    name: 'InputRecommendtion',
    component: InputRecommendtion
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
    path: '/user/profile/:userid',
    name: 'userProfile',
    component: userProfile
  }, {
    path: "/404",
    name: "NotFount404",
    component: NotFount404,
  }, {
    path: "*",
    redirect:'/404',
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
