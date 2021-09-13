import Home from '../views/Home.vue'
import middlewares from '../middlewares/middlewares'

export default [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
    meta: {
      middleware: [
        middlewares.isAuthenticated
      ]
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "login" */ '../components/auth/Login.vue'),
    meta: {
      middleware: [
        middlewares.publicOnly
      ]
    }
  },
  {
    path: '/signup',
    name: 'Signup',
    component: () => import(/* webpackChunkName: "signup" */ '../components/auth/Signup.vue'),
    meta: {
      middleware: [
        middlewares.publicOnly
      ]
    }
  }
]
