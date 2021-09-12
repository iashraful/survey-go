const state = {
  auth: localStorage.getItem('accessToken') || false,
  accessToken: localStorage.getItem('accessToken') || undefined
}

const mutations = {
  updateLoginStatus (state, payload) {
    state.auth = payload
  },
  updateAccessToken (state, token) {
    state.accessToken = token
  },
  logout (state) {
    state.auth = false
    state.accessToken = null
    localStorage.setItem('accessToken', undefined)
  }
}

const actions = {
  updateAccessToken ({ commit }, payload) {
    console.log(payload)
    localStorage.setItem('accessToken', payload)
    commit('updateAccessToken', payload)
    commit('updateLoginStatus', true)
  },
  triggerLogout ({ commit }) {
    commit('logout')
  }
}

const getters = {
  isAuthenticated (state) {
    return state.auth
  },
  getAccessToken (state) {
    return state.accessToken
  }
}

export default {
  state,
  mutations,
  getters,
  actions
}
