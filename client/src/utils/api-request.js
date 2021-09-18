import Axios from 'axios'
import store from '../store'
export const API_URL = 'http://localhost:8081/api'

function makeApiUrl (path) {
  return `${API_URL}${path}`
}

export const _get = async function ({ path, noToken = false }) {
  const _headers = {}
  if (!noToken) {
    _headers.Authorization = `Bearer ${store.getters.getAccessToken}`
  }
  const url = makeApiUrl(path)
  return await Axios.get(url, { headers: _headers })
}

export const _post = async function ({ path, data, noToken = false }) {
  const _headers = {}
  if (!noToken) {
    _headers.Authorization = `Bearer ${store.getters.getAccessToken}`
  }
  const url = makeApiUrl(path)
  return await Axios.post(url, data, { headers: _headers })
}

export const createOrUpdate = async function ({ path, data, noToken = false, method = 'post' }) {
  const _headers = {}
  if (!noToken) {
    _headers.Authorization = `Bearer ${store.getters.getAccessToken}`
  }
  const url = makeApiUrl(path)
  console.log(method)
  if (method === 'put') {
    return await Axios.put(url, data, { headers: _headers })
  }
  return await Axios.post(url, data, { headers: _headers })
}
