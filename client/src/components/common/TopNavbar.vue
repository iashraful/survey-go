<template>
    <b-navbar type="is-primary" fixed-top>
        <template #brand>
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                Survey Go
            </b-navbar-item>
        </template>
        <template #start>
            <b-navbar-item to="/" tag="router-link">
                Home
            </b-navbar-item>
            <b-navbar-item to="/surveys" tag="router-link">
                Surveys
            </b-navbar-item>
            <b-navbar-item to="/about" tag="router-link">
                About
            </b-navbar-item>
        </template>

        <template #end>
          <b-navbar-item tag="div">
            <div class="buttons">
              <router-link v-if="!isAuthenticated" class="button is-primary" to='/signup'>
                <strong>Sign up</strong>
              </router-link>
              <router-link v-if="!isAuthenticated" class="button is-light" to='/login'>
                Log in
              </router-link>
              <button v-if="isAuthenticated" class="button is-light" @click="logout">
                Logout
              </button>
            </div>
          </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'TopNavbar',
  computed: {
    ...mapGetters(['isAuthenticated'])
  },
  data () {
    return {}
  },
  methods: {
    logout () {
      this.$store.dispatch('triggerLogout')
      this.$router.push('/')
    }
  }
}
</script>
