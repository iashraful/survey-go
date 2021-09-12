export default {
  isAuthenticated ({ next, store }) {
    if (!store.getters.isAuthenticated) {
      return next('/login')
    }
    return next()
  },
  allowAny ({ next, store }) {
    return next()
  },
  hasPermission ({ to, next, store }) {
    // TODO: Will fix with real data
    // console.log(next)
    // eslint-disable-next-line no-constant-condition
    if (false) {
      return next()
    }
    return next(`/login?onSuccess=${to.path}`)
  }
}
