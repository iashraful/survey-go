export default {
  isAuthenticated ({ to, next, store }) {
    if (!store.getters.isAuthenticated) {
      return next(`/login?onSuccess=${to.path}`)
    }
    return next()
  },
  allowAny ({ next, store }) {
    return next()
  }
}
