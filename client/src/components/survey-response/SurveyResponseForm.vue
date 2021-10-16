<template>
  <div>
    <h2 class="title">{{ config.name }}</h2>
    <v-form-maker
      submitBtnText="Submit"
      :config="config"
      @onSubmit="handleSubmit"
    />
  </div>
</template>

<script>
import VFormMaker from '../form-maker/VFormMaker'
import SurveyResponseMixin from '../../mixins/SurveyResponseMixin'
import { createOrUpdate } from '@/utils/api-request'
import { mapGetters } from 'vuex'

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
  computed: {
    ...mapGetters(['isAuthenticated'])
  },
  methods: {
    parseToForm () {
      this.config = this.parseSurveyToResponseFormConfig(this.survey)
    },
    async handleSubmit (data) {
      const serializedData = this.parseFormDataToAPI(data, this.survey)
      try {
        const response = await createOrUpdate(
          {
            path: '/v1/survey-responses/',
            data: serializedData,
            method: 'post',
            noToken: !this.isAuthenticated
          })
        if (response.status === 201) {
          this.$buefy.toast.open({
            message: 'Survey response saved successfully.',
            type: 'is-success'
          })
          await this.$router.push('/')
        }
      } catch (e) {
        console.log(e.response)
      }
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
