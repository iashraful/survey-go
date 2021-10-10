<template>
  <div id="app">
    <top-navbar />
    <div class="container" style="margin-top: .5rem">
      <b-message
        v-if="routeWarning" auto-close type="is-danger" :duration="5000">
          {{ routeWarning }}
      </b-message>
      <router-view/>
    </div>
  </div>
</template>

<script>
import TopNavbar from './components/common/TopNavbar.vue'

export default {
  name: 'App',
  components: { TopNavbar },
  data () {
    return {
      routeWarning: ''
    }
  },
  mounted () {
    // Check for route warning
    this.routeWarning = this.$route.query.warning
    this.$ebus.$on('TRIGGERED_LOGOUT', () => {
      console.log('Logout due to security purpose.')
    })
  }
}
</script>
