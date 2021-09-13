<template>
<section class="hero is-fullheight">
  <div class="hero-body">
    <div class="container" style="top: -8rem">
      <div class="columns is-centered">
        <div class="column is-5-tablet is-4-desktop is-3-widescreen">
          <h2 style="text-align: center; font-size: 1.5rem; margin-bottom: 5px;">Login</h2>
          <form action="" class="box" @submit.prevent="login">
            <div class="field">
              <label for="" class="label">Email</label>
              <div class="control has-icons-left">
                <input type="email"
                  v-model="formData.username"
                  placeholder="e.g. bobsmith@gmail.com" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-envelope"></i>
                </span>
              </div>
            </div>
            <div class="field">
              <label for="" class="label">Password</label>
              <div class="control has-icons-left">
                <input type="password"
                  v-model="formData.password"
                  placeholder="*******" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-lock"></i>
                </span>
              </div>
            </div>
            <b-message type="is-danger" v-if="apiErrorData && apiErrorData.detail">
              {{ apiErrorData.detail }}
            </b-message>
            <div class="field">
              <router-link to="forgot-password">Forgotten your password??</router-link>
            </div>
            <div class="field">
              <button class="button is-success is-fullwidth" type="submit">
                Login
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import { _post } from '@/utils/api-request'

export default {
  name: 'Login',
  data () {
    return {
      formData: {},
      apiErrorData: {}
    }
  },
  methods: {
    async login () {
      const onSuccessRedirect = this.$route.query.onSuccess
      try {
        const response = await _post({ path: '/v2/login/', data: this.formData })
        if (response.status === 200) {
          this.$store.dispatch('updateAccessToken', response.data.access_token)
          if (onSuccessRedirect) {
            this.$router.push(onSuccessRedirect)
          } else {
            this.$router.push('/')
          }
        }
      } catch (e) {
        this.apiErrorData = e.response.data
      }
    }
  }
}
</script>
