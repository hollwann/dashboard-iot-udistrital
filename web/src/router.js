import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const lazyLoad = view => () => import(`@/views/${view}.vue`)

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'login',
    component: lazyLoad('Login')
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: lazyLoad('Dashboard')
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: lazyLoad('SignUp')
  },
  {
    path: '/devices',
    name: 'devices',
    component: lazyLoad('Devices')
  },
  {
    path: '/device',
    name: 'device',
    component: lazyLoad('Device')
  },
  {
    path: '/variable-data',
    name: 'variable-data',
    component: lazyLoad('VariableData')
  },
  {
    path: '/profile',
    name: 'profile',
    component: lazyLoad('Profile')
  },
  {
    path: '/help',
    name: 'help',
    component: lazyLoad('Help')
  }
]
export default new Router({
  routes
})
