import Axios from 'axios'
import store from '../store'
export const API_URL = 'http://localhost:8081/api'

function makeApiUrl (path) {
  return `${API_URL}${path}`
}

function _triggerEmergencyLogout () {
  store.dispatch('triggerLogout')
}

export const _get = async function ({ path, noToken = false }) {
  const _headers = {}
  if (!noToken) {
    _headers.Authorization = `Bearer ${store.getters.getAccessToken}`
  }
  const url = makeApiUrl(path)
  const response = await Axios.get(url, { headers: _headers }).catch((err) => {
    if (err.response.status === 479) {
      _triggerEmergencyLogout()
    }
    throw err
  })
  return response
}

export const createOrUpdate = async function ({ path, data, noToken = false, method = 'post' }) {
  const _headers = {}
  if (!noToken) {
    _headers.Authorization = `Bearer ${store.getters.getAccessToken}`
  }
  const url = makeApiUrl(path)
  if (method === 'put') {
    return await Axios.put(url, data, { headers: _headers }).catch((err) => {
      if (err.response.status === 479) {
        _triggerEmergencyLogout()
      }
      throw err
    })
  } else if (method === 'patch') {
    return await Axios.patch(url, data, { headers: _headers }).catch((err) => {
      if (err.response.status === 479) {
        _triggerEmergencyLogout()
      }
      throw err
    })
  }
  const response = await Axios.post(url, data, { headers: _headers }).catch((err) => {
    if (err.response.status === 479) {
      _triggerEmergencyLogout()
    }
    throw err
  })
  return response
}

export const _del = async function ({ path, noToken = false }) {
  const _headers = {}
  if (!noToken) {
    _headers.Authorization = `Bearer ${store.getters.getAccessToken}`
  }
  const url = makeApiUrl(path)
  const response = await Axios.delete(url, { headers: _headers }).catch((err) => {
    if (err.response.status === 479) {
      _triggerEmergencyLogout()
    }
    throw err
  })
  return response
}
