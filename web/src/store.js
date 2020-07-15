import Vue from 'vue'
import Vuex from 'vuex'
import { postRequest } from './plugins/ApiConn'
import router from './router'
import { trace } from './tools'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    dialog: {
      show: false,
      text: ''
    },
    user: null
  },
  mutations: {
    SET_DIALOG(state, val) {
      state.dialog = val
    },
    SET_USER(state, val) {
      state.user = val
    }
  },
  actions: {
    userLogout({ commit }) {
      commit('SET_USER', null)
      localStorage.removeItem('token')
      router.push({ name: 'login' })
    },
    userLogged({ commit, dispatch }) {
      return postRequest('get_user', {})
        .then(response => {
          commit('SET_USER', response.data.user)
          router.push({ name: 'dashboard' })
        })
        .catch(e => {
          trace(e)
          dispatch('userLogout')
        })
    },
    showDialog({ commit }, text) {
      const dialog = {
        show: true,
        text: text
      }

      commit('SET_DIALOG', dialog)
    },
    hideDialog({ commit }) {
      const dialog = {
        show: false,
        text: ''
      }
      commit('SET_DIALOG', dialog)
    }
  }
})
