import axios from 'axios'
import store from './../store'
import { trace } from './../tools'

const getBaseURL = buildType =>
  buildType == 'production'
    ? `https://api-ry73nip7ha-uc.a.run.app/sicopu/`
    : `http://127.0.0.1:5000/users/`

let apiClient = axios.create({
  baseURL: getBaseURL(process.env.NODE_ENV),
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  },
  timeout: 10000
})

const setHeaderAuthorization = () =>
  (apiClient.defaults.headers.common['Authorization'] = localStorage.getItem(
    'token'
  ))

const postRequest = (route, data) => {
  return new Promise((resolve, rej) => {
    setHeaderAuthorization()
    apiClient
      .post(route, data)
      .then(response => {
        trace(response.data)
        const res = response.data.res
        if (res == 200) resolve(response.data)
        else if (res == 'UD006') {
          store.dispatch('showDialog', response.data.msg)
          store.dispatch('userLogout')
          rej()
        } else {
          store.dispatch('showDialog', response.data.msg)
          rej()
        }
      })
      .catch(e => {
        trace(e)
        store.dispatch('showDialog', 'Ocurrio un error en la conexión')
        rej()
      })
  })
}

export { postRequest }
