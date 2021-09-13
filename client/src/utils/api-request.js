import Axios from 'axios'
import store from '../store'
export const API_URL = 'http://localhost:8081/api'

function makeApiUrl (path) {
  return `${API_URL}${path}`
}

export const _get = async function ({ path, noToken = false }) {
  const _headers = {}
  if (!noToken) {
    _headers.Authentication = `Bearer ${store.getters.getAccessToken}`
  }
  const url = makeApiUrl(path)
  return await Axios.post(url, _headers)
}

export const _post = async function ({ path, data, noToken = false }) {
  const _headers = {}
  if (!noToken) {
    _headers.Authentication = `Bearer ${store.getters.getAccessToken}`
  }
  const url = makeApiUrl(path)
  return await Axios.post(url, data, _headers)
}
