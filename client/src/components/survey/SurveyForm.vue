<template>
  <div class="survey-form">
    <form @submit.prevent="saveSurvey">
      <div class="survey-container">
        <div class="survey-basic">
          <b-field label="Survey Name">
            <b-input v-model="formData.name" required></b-input>
          </b-field>
          <b-field label="Instructions">
            <b-input maxlength="500" type="textarea" v-model="formData.instructions"></b-input>
          </b-field>
        </div>

        <div class="survey-questions">
          <survey-question-form-set
            :questions="formData.questions"
            @onQuestionRemove="removeQuestionByIdentity"
            @onQuestionUpdate="updateQuestionByIdentity"
            :submitted="formSubmit"
          />
          <div class="add-more-btn">
            <b-button
              @click="addMoreQuestion"
              icon-pack="fa" size="is-small"
              class="is-info" icon-left="plus">
              Add More
            </b-button>
          </div>
        </div>

        <div class="survey-action-btns">
          <b-button
            @click="saveSurvey"
            icon-pack="fa" class="is-primary"
            icon-left="save" type="submit">Save</b-button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import SurveyQuestionFormSet from './SurveyQuestionFormSet.vue'

export default {
  name: 'SurveyForm',
  components: { SurveyQuestionFormSet },
  data () {
    return {
      formSubmit: false,
      formData: {
        name: '',
        questions: []
      }
    }
  },
  methods: {
    saveSurvey () {
      this.formSubmit = true
      console.log('Survey Form')
      console.log(this.formData)
      // TODO: We must set formSubmit =false if there is any error or user needed to edit the form
    },
    addMoreQuestion () {
      this.formData.questions.push(
        { text: '', text_translation: '', type: 'text', __id: new Date().getTime() }
      )
    },
    updateQuestionByIdentity ({ identity, data }) {
      const _index = this.formData.questions.findIndex(i => identity === i.__id)
      this.formData.questions[_index] = data
    },
    removeQuestionByIdentity (identity) {
      const _index = this.formData.questions.findIndex(i => identity === i.__id)
      this.formData.questions.splice(_index, 1)
    }
  }
}
</script>

<style scoped>
.survey-container {
  display: block;
  width: 100%;
}

.survey-container .survey-basic {
  display: inline-block;
  width: 25%;
  position: fixed;
  right: 17.5rem;
}

.survey-container .survey-questions {
  display: inline-block;
  width: 50%;
}

.survey-container .survey-action-btns {
  display: block;
  width: 100%;
}
.survey-container .survey-questions .add-more-btn {
  display: block;
  text-align: right;
}
</style>
