import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'


Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    topmovies: [],
    search: [],
    movie: [],
    token: localStorage.getItem("token") || "",
    currentUser: {},
    profile: {},
  },
  getters: {
    isLoggedIn: (state) => !!state.token,
    currentUser: (state) => state.currentUser,
    isLogin(state) {
      return state.token ? true : false
    },
    profile: (state) => state.profile,
  },
  mutations: {
    GET_TOP10_MOVIES(state, topmovies) {
      state.topmovies = topmovies
    },
    SET_SEARCH: (state, search) => (state.search = search),
    ADD_LIST: (state, movie) => (state.movie = movie),
    SIGN_UP(state,token){
      state.token = token
      console.log('회원가입 성공')
      router.push({name: 'user'})
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name: 'index'})
    },
    SET_TOKEN: (state, token) => (state.token = token),
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_PROFILE: (state, profile) => (state.profile = profile),

  },
  actions: {
    getTop10Movies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/top/`,
      })
      .then((res) => {
        console.log(res, context)
        // console.log(res.data)
        context.commit('GET_TOP10_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    search(context, movieName){
      axios({
        method: 'get',
        url: `${API_URL}/movies/search/${movieName}`,
      })
      .then((res) => {
        console.log(res, context)
        context.commit('SET_SEARCH', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SIGN_UP', res.data.key)
          localStorage.setItem("token", this.state.token)
          context.dispatch("fetchCurrentUser")
        })
        .catch((err) => {
          alert(err.message)
        })
    },
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username , password
        }
      })
      .then((res) => {
        const token = res.data.key
        context.commit('SAVE_TOKEN', token)
        localStorage.setItem("token", token)
        context.dispatch("fetchCurrentUser")
      })
      .catch((err) => {
        alert(err.message)
      })
    },
    logout(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
      .then(() => {
        context.commit("SET_TOKEN", "")
        localStorage.setItem("token", "")
        alert("성공적으로 logout 되었습니다.")
        router.push({ name: "index" })
      })
      .catch((err) => console.error(err));
    },

    fetchCurrentUser(context) {
      if (this.getters.isLoggedIn) {
        axios({
          method: 'get',
          url: `${API_URL}/accounts/user/`,
          headers : {
            Authorization : `Token ${context.state.token}`
          }
        })
        .then((res) => {
          context.commit("SET_CURRENT_USER", res.data)
        })
        .catch((err) => {
          console.log('잠깐만') 
          console.error(err)})
      }
    },
    fetchProfile(context, payload) {
      axios({
        method: 'get',
        url: `${API_URL}/profile/${payload}/`,
      })
      .then((res) => {
        console.log(res.data)
        context.commit("SET_PROFILE", res.data)
      })
    },
    
    addList(context, moviePk) {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${moviePk}/addlist/`,
        headers : {
          Authorization : `Token ${context.state.token}`
        }
      })
      .then((res) => {
        context.commit('ADD_LIST', res.data)
      })
      .catch(err => console.log(err))
    },
  },
  modules: {
  }
})
