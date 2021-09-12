import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'
import routes from './routes'
import middlewarePipeline from '../middlewares/middleware-pipeline'
import predefinedMiddlewares from '../middlewares/predefined-middlewares'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  let middlewares = to.meta.middleware
  if (!middlewares) {
    middlewares = [
      predefinedMiddlewares.request
    ]
  }

  const context = {
    to,
    from,
    next,
    store
  }

  return middlewares[0]({
    ...context,
    next: middlewarePipeline(context, middlewares, 1)
  })
})

export default router
