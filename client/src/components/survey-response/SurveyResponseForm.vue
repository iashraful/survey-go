<template>
  <div>
    <h2 class="title">{{ config.name }}</h2>
    <v-form-maker
      submitBtnText="Submit"
      :config="config"
    />
  </div>
</template>

<script>
import VFormMaker from '../form-maker/VFormMaker'
import SurveyResponseMixin from '../../mixins/SurveyResponseMixin'

export default {
  components: { VFormMaker },
  name: 'SurveyResponseForm',
  mixins: [SurveyResponseMixin],
  props: {
    survey: {
      type: Object,
      default: () => {},
      required: true
    }
  },
  data () {
    return {
      config: {}
    }
  },
  methods: {
    parseToForm () {
      this.config = this.parseSurveyToResponseFormConfig(this.survey)
    }
  },
  watch: {
    survey: {
      handler (newValue) {
        this.parseToForm()
      },
      deep: true
    }
  }
}
</script>

<style scoped>

</style>
