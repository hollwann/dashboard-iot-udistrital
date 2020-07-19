import Vue from 'vue'
import Router from 'vue-router'
import store from './store'

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
    component: lazyLoad('Dashboard'),
    meta: {
      authRequired: true
    }
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: lazyLoad('SignUp')
  },
  {
    path: '/devices',
    name: 'devices',
    component: lazyLoad('Devices'),
    meta: {
      authRequired: true
    }
  },
  {
    path: '/device/:id',
    name: 'device',
    component: lazyLoad('Device'),
    props: true,
    meta: {
      authRequired: true
    }
  },
  {
    path: '/variable-data',
    name: 'variable-data',
    component: lazyLoad('VariableData'),
    meta: {
      authRequired: true
    }
  },
  {
    path: '/profile',
    name: 'profile',
    component: lazyLoad('Profile'),
    meta: {
      authRequired: true
    }
  },
  {
    path: '/help',
    name: 'help',
    component: lazyLoad('Help'),
    meta: {
      authRequired: true
    }
  },
  {
    path: '*',
    redirect: '/dashboard'
  }
]

const router = new Router({
  routes
})

router.beforeEach((to, from, next) => {
  const authRequired = to.meta.authRequired || false
  const user = store.state.user

  if (authRequired && user) next()
  else if (authRequired && !user) next({ name: 'login' })
  else if (!authRequired && user) next({ name: 'dashboard' })
  else next()
})

export default router
