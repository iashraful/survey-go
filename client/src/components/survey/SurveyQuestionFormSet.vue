<template>
  <div>
    <survey-question-form
      v-for="(ques, _i) in questions" :key="ques.__id"
      :index="_i" :identity="ques.__id"
      @updateQuestion="dataPassToParentOnUpdate"
      @removeQuestion="dataPassToParentOnRemove"
    />
  </div>
</template>

<script>
import SurveyQuestionForm from './SurveyQuestionForm.vue'

export default {
  name: 'SurveyQuestionFormSet',
  components: { SurveyQuestionForm },
  props: {
    questions: {
      type: Array,
      required: true,
      default: () => []
    }
  },
  methods: {
    dataPassToParentOnUpdate (data) {
      this.$emit('onQuestionUpdate', data)
    },
    dataPassToParentOnRemove (identity) {
      this.$emit('onQuestionRemove', identity)
    }
  }
}
</script>
