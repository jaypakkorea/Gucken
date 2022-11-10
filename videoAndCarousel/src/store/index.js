import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    popupText(){
      console.log('start')
      // let whoweare = document.querySelector(".whoweare");

      // let value = window.scrollY
      // // console.log(whoweare)
      // console.log("scrollY", value);


      // if(value>300){
      //     whoweare.style.animation='disappear 1s ease-out forwards';
      //     console.log("!");
      // }else{
      //     whoweare.style.animation='slide 1s ease-out'
      // }
    },
  },

  modules: {
  }
})
