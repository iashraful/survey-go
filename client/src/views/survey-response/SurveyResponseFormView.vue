<template>
  <div>
    <survey-response-form :survey="surveyDetails"/>
  </div>
</template>

<script>
import SurveyResponseForm from '@/components/survey-response/SurveyResponseForm'
import { _get } from '@/utils/api-request'

export default {
  name: 'SurveyResponseFormView',
  data () {
    return {
      surveyDetails: {}
    }
  },
  components: {
    SurveyResponseForm
  },
  mounted () {
    this.getSurveyDetailsFromAPI()
  },
  methods: {
    async getSurveyDetailsFromAPI () {
      const surveySlug = this.$route.params.surveySlug
      try {
        const response = await _get({ path: `/v1/surveys/${surveySlug}/` })
        this.surveyDetails = response.data
      } catch (e) {
        if (e.response.status === 404) {
          await this.$router.push('/404-not-found')
        }
        console.log(e.response)
      }
    }
  }
}
</script>
