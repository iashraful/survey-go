<template>
  <div id="app">
    <top-navbar />
    <div class="container" style="margin-top: .5rem">
      <router-view/>
    </div>
  </div>
</template>

<script>
import TopNavbar from './components/common/TopNavbar.vue'

export default {
  name: 'App',
  components: { TopNavbar }
}
</script>
