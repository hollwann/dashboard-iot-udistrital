import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import DatetimePicker from 'vuetify-datetime-picker'

Vue.use(DatetimePicker)
Vue.config.productionTip = false

const initApp = () =>
  new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
  }).$mount('#app')

document.addEventListener('deviceready', initApp, false)