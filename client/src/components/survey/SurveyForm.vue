<template>
  <div class="survey-form">
    <form @submit.prevent="saveSurvey">
      <b-field label="Survey Name">
        <b-input v-model="formData.name" required></b-input>
      </b-field>
      <b-field label="Instructions">
        <b-input maxlength="500" type="textarea" v-model="formData.instructions"></b-input>
      </b-field>

      <div class="questions-child-form">
        <survey-question-form
          v-for="(ques, index) in formData.questions" :key="index"
          :index="index" :question="question"
        />
      </div>

      <b-button type="is-primary">Save</b-button>
    </form>
  </div>
</template>

<script>
import SurveyQuestionForm from './SurveyQuestionForm.vue'

export default {
  name: 'SurveyForm',
  components: { SurveyQuestionForm },
  data () {
    return {
      formData: {
        questions: [
          { text: '', text_translation: '', type: 'text' }
        ]
      }
    }
  },
  methods: {
    saveSurvey () {
      console.log(this.formData)
    }
  }
}
</script>
