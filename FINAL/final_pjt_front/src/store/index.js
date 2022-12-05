import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'
import Swal from "sweetalert2";


Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    topmovies: [],
    popularmovies : [],
    search: [],
    movie: [],
    token: localStorage.getItem("token") || "",
    currentUser: {},
    profile: {},
    genre : {},
    community:[],
    // recommendationMovies: [],
  },
  getters: {
    isLoggedIn: (state) => !!state.token,
    currentUser: (state) => state.currentUser,
    isLogin(state) {
      return state.token ? true : false
    },
    profile: (state) => state.profile,
    // recommendationMovies: (state) => state.recommendationMovies,
  },
  mutations: {
    GET_TOP10_MOVIES(state, topmovies) {
      state.topmovies = topmovies
    },
    GET_POPULAR_TOP10_MOVIES(state, popularmovies) {
      state.popularmovies = popularmovies
    },
    SET_SEARCH: (state, search) => (state.search = search),
    ADD_LIST: (state, movie) => (state.movie = movie),
    SIGN_UP(state,token){
      state.token = token
      router.push({name: 'index'})
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name: 'index'})
    },
    SET_TOKEN: (state, token) => (state.token = token),
    SET_CURRENT_USER: (state, user) => (state.currentUser = user),
    SET_PROFILE: (state, profile) => (state.profile = profile),
    SET_SEARCH_GENRE : (state, genre) => (state.genre = genre),
    // SET_RECOMMENDATION_MOVIES: (state, recommendation) => (state.recommendationMovies = recommendation),

  },
  actions: {
    getTop10Movies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/top/`,
      })
      .then((res) => {
        context.commit('GET_TOP10_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    popularTop10Movies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/popularity/`,
      })
      .then((res) => {
        context.commit('GET_POPULAR_TOP10_MOVIES', res.data)
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
        context.commit('SET_SEARCH', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 장르 선택 all
    searchGenreAll(context){
      axios({
        method: 'get',
        url: `${API_URL}/movies/search/genre/all`,
      })
      .then((res) => {
        context.commit('SET_SEARCH_GENRE', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 특정장르 선택
    searchGenre(context, genreId){
      axios({
        method: 'get',
        url: `${API_URL}/movies/search/genre/${genreId}`,
      })
      .then((res) => {
        context.commit('SET_SEARCH_GENRE', res.data)
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
          context.commit('SIGN_UP', res.data.key)
          localStorage.setItem("token", this.state.token)
          context.dispatch("fetchCurrentUser")
        })
        .catch((err) => {
          // Swal.fire(err.message, '', 'error')
          if (err.response.status === 400 && payload.password1 !== payload.password2) {
            Swal.fire('비밀번호가 다릅니다.', '', 'error')
            
          } else if (err.response.status === 400 ) {
            Swal.fire('이미 가입된 아이디 입니다.', '', 'error')
        } 
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
        Swal.fire(err.message, '', 'error')
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
        Swal.fire({html:"성공적으로 logout 되었습니다.", timer: 1500})
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
          console.error(err)})
      }
    },
    fetchProfile(context, payload) {
      axios({
        method: 'get',
        url: `${API_URL}/profile/${payload}/`,
      })
      .then((res) => {
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
    updateProfilePic(context, info){
      const userId = this.state.profile.id
      axios({
        url: `${API_URL}/profile/${userId}/update/`,
        method: "put",
        data : info,
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization : `Token ${context.state.token}`
        },
      })
      .then(() => {
      })
      .catch((err) => {
        Swal.fire(err.message, '', 'error')
      });
    },
    followIng(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/profile/${payload}/follow/`,
        headers : {
          Authorization : `Token ${context.state.token}`
        }
      })
      .then((res) => {
        context.commit('SET_PROFILE', res.data)
      })
      .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
