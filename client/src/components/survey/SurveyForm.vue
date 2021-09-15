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
            icon-pack="fa" class="is-primary"
            icon-left="save" native-type="submit">Save</b-button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { _post } from '@/utils/api-request'
import SurveyQuestionFormSet from './SurveyQuestionFormSet.vue'
import SurveyMixin from '../../mixins/SurveyMixin'

export default {
  name: 'SurveyForm',
  components: { SurveyQuestionFormSet },
  mixins: [SurveyMixin],
  data () {
    return {
      formData: {
        name: '',
        questions: [
          {
            text: '',
            text_translation: '',
            type: 'text',
            __id: uuidv4(),
            options: [
              { name: '' },
              { name: '' }
            ]
          }
        ]
      }
    }
  },
  methods: {
    checkValidation () {
      let valid = true
      let msg = ''
      if (this.formData.questions.length === 0) {
        valid = false
        msg = 'A good survey should consist of one or more questions.'
      }
      return { status: valid, message: msg }
    },
    async saveSurvey () {
      const validation = this.checkValidation()
      if (validation.status) {
        const serializableData = this.parseFinalSurveyForAPI(this.formData)
        console.log('Survey Form')
        console.log(serializableData)
        try {
          const response = await _post({ path: '/v1/surveys/', data: serializableData })
          if (response.status === 201) {
            this.$buefy.toast.open({
              message: 'Survey saved successful.',
              type: 'is-success'
            })
            this.$router.push('/surveys')
          }
        } catch (e) {
          this.$buefy.toast.open({
            message: e.response.data.msg,
            type: 'is-danger'
          })
        }
      } else {
        this.$buefy.toast.open({
          message: validation.message,
          type: 'is-danger'
        })
      }
    },
    addMoreQuestion () {
      this.formData.questions.push(
        { text: '', text_translation: '', type: 'text', __id: uuidv4() }
      )
    },
    updateQuestionByIdentity ({ identity, data }) {
      const _index = this.formData.questions.findIndex(i => identity === i.__id)
      if (_index !== -1) {
        this.formData.questions[_index] = data
      }
    },
    removeQuestionByIdentity (identity) {
      const _index = this.formData.questions.findIndex(i => identity === i.__id)
      if (_index !== -1) {
        this.formData.questions.splice(_index, 1)
      }
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
