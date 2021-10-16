import Home from '../views/Home.vue'
import middlewares from '../middlewares/middlewares'

export default [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/surveys',
    name: 'SurveyListView',
    component: () => import(/* webpackChunkName: "survey-list" */ '../views/survey/SurveyListView.vue'),
    meta: {
      middleware: [
        middlewares.isAuthenticated
      ]
    }
  },
  {
    path: '/surveys/create',
    name: 'SurveyCreateView',
    component: () => import(/* webpackChunkName: "survey-create" */ '../views/survey/SurveyCreateView.vue'),
    meta: {
      middleware: [
        middlewares.isAuthenticated
      ]
    }
  },
  {
    path: '/surveys/edit/:slug',
    name: 'SurveyEditView',
    component: () => import(/* webpackChunkName: "survey-edit" */ '../views/survey/SurveyEditView.vue'),
    meta: {
      middleware: [
        middlewares.isAuthenticated
      ]
    }
  },
  {
    path: '/survey-responses',
    name: 'SurveyResponseListView',
    component: () => import(/* webpackChunkName: "survey-response-list" */ '../views/survey-response/SurveyResponseListView.vue'),
    meta: {
      middleware: [
        middlewares.isAuthenticated
      ]
    }
  },
  {
    path: '/survey-responses/:surveySlug/create',
    name: 'SurveyResponseFormView',
    component: () => import(/* webpackChunkName: "survey-response-form" */ '../views/survey-response/SurveyResponseFormView.vue')
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
