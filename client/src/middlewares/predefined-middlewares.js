export default {
  request ({ to, next, store }) {
    // This will call in every request at first
    next()
  }
}
