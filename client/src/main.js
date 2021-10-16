import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import EventBus from '@/utils/event-bus'

import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

import './assets/main.css'
import './assets/override-bulma.css'

Vue.use(Buefy)

Vue.config.productionTip = false
Vue.prototype.$ebus = EventBus
// This will help to call super
Vue.prototype.$super = function (options) {
  return new Proxy(options, {
    get: (options, name) => {
      if (options.methods && name in options.methods) {
        return options.methods[name].bind(this)
      }
    }
  })
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
