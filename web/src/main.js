import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import DatetimePicker from 'vuetify-datetime-picker'
import { postRequest } from './plugins/ApiConn'
import 'vuelayers/lib/style.css' // needs css-loader
import VueLayers from 'vuelayers'

Vue.use(DatetimePicker)
Vue.config.productionTip = false
Vue.prototype.$post = postRequest

Vue.use(VueLayers)

const initApp = async () => {
  const token = localStorage.getItem('token')
  if (token) await store.dispatch('userLogged')
  new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
  }).$mount('#app')
}

document.addEventListener('deviceready', initApp, false)
