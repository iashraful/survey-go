<template>
  <div>
    <div class="survey-edit-view" style="margin-bottom: 2px">
      <div class="title">Update Survey</div>
      <hr style="margin-top: 0"/>
      <survey-form :existing-survey="surveyDetails"/>
    </div>
  </div>
</template>

<script>
import { _get } from '../../utils/api-request'
import SurveyForm from '../../components/survey/SurveyForm.vue'

export default {
  name: 'SurveyEditView',
  components: { SurveyForm },
  data () {
    return {
      surveyDetails: {}
    }
  },
  mounted () {
    this.getSurveyDetailsFromAPI()
  },
  methods: {
    async getSurveyDetailsFromAPI () {
      try {
        const response = await _get({ path: `/v1/surveys/${this.$route.params.slug}` })
        if (response.status === 200) {
          this.surveyDetails = response.data
        }
      } catch (e) {
        console.log(e.response)
      }
    }
  }
}
</script>

<style scoped>
.survey-edit-view .title{
  margin-bottom: 5px;
}
</style>
