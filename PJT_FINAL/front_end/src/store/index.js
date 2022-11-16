import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  state: {
    topmovies: [],
  },
  getters: {
  },
  mutations: {
    GET_TOP10_MOVIES(state, topmovies) {
      state.topmovies = topmovies
    },
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
    }
  },
  modules: {
  }
})
