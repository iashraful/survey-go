<template>
  <div class="survey-form">
    <form @submit.prevent="saveSurvey">
      <div class="survey-container">
        <div class="d-flex-container">
          <div class="survey-basic">
            <b-field label="Survey Name">
              <b-input v-model="formData.name" required></b-input>
            </b-field>
            <b-field label="Instructions">
              <b-input maxlength="500" type="textarea" v-model="formData.instructions"></b-input>
            </b-field>
          </div>

          <div class="survey-questions">
            <survey-section-form
              v-for="(sec, _i) in formData.sections"
              :key="sec.__id"
              :index="_i"
              :identity="sec.__id"
              :section-count="formData.sections.length"
              @onSectionRemove="handleSectionRemove"
              @onSectionUpdate="handleSectionUpdate"
            />
            <div class="add-more-btn">
              <b-button
                @click="addMoreSection"
                icon-pack="fa" size="is-small"
                class="is-info" icon-left="plus">
                Add Section
              </b-button>
            </div>
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
import SurveySectionForm from './SurveySectionForm.vue'
import SurveyMixin from '../../mixins/SurveyMixin'

export default {
  name: 'SurveyForm',
  components: { SurveySectionForm },
  mixins: [SurveyMixin],
  data () {
    return {
      formData: {
        name: '',
        sections: [
          { name: '', __id: uuidv4() }
        ]
      }
    }
  },
  methods: {
    checkValidation () {
      let valid = true
      let msg = ''
      if (this.formData.sections.length === 0) {
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
    addMoreSection () {
      this.formData.sections.push(
        { name: '', __id: uuidv4() }
      )
    },
    handleSectionRemove (identity) {
      const _index = this.formData.sections.findIndex(i => i.__id === identity)
      if (_index !== -1) {
        this.formData.sections.splice(_index, 1)
      }
    },
    handleSectionUpdate ({ identity, data }) {
      const _index = this.formData.sections.findIndex(i => i.__id === identity)
      if (_index !== -1) {
        this.formData.sections[_index] = { __id: identity, ...data }
      }
    }
  }
}
</script>

<style scoped>
.survey-container .survey-basic {
  width: 28%
}
.survey-container .survey-questions {
  margin-left: 1.8rem;;
  width: 70%
}
.survey-container .survey-action-btns {
  display: block;
  width: 100%;
  margin: 1rem 0 3rem 0;
  text-align: center;
}
.survey-container .survey-action-btns button {
  padding: 0 4rem 0 4rem;
}
.survey-container .survey-questions .add-more-btn {
  display: block;
  text-align: right;
}

@media (max-width: 1023px) {
  .survey-container .survey-basic {
    width: 100%;
  }
  .survey-container .survey-questions {
    margin-left: 0;
    width: 100%;
  }
  .survey-container .survey-action-btns button {
    padding: unset;
    width: 100%;
  }
}

</style>
