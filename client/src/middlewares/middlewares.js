export default {
  isAuthenticated ({ to, next, store }) {
    if (!store.getters.isAuthenticated) {
      return next(`/login?onSuccess=${to.path}`)
    }
    return next()
  },
  allowAny ({ next, store }) {
    return next()
  },
  publicOnly ({ to, next, store }) {
    if (store.getters.isAuthenticated) {
      return next(`/?warning=${to.path} is allowed only public access. Please logout and try again.`)
    }
    return next()
  }
}
