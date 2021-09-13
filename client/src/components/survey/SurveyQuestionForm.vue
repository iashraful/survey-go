<template>
  <div>
    <h3 class="subtitle">Question: #{{ index + 1 }}</h3>
    <b-field label="Question">
      <b-input v-model="question.text" required></b-input>
    </b-field>
    <b-field label="Translation">
      <b-input v-model="question.text_translation"></b-input>
    </b-field>
    <b-field label="Question Type">
      <b-select placeholder="Select a name" v-model="question.type">
        <option
          v-for="option in questionsTypes"
          :value="option"
          :key="option">
          {{ option }}
        </option>
      </b-select>
    </b-field>
  </div>
</template>

<script>
export default {
  name: 'SurveyQuestionForm',
  props: {
    index: {
      type: Number,
      required: true
    }
  },
  data () {
    return {
      question: {},
      questionsTypes: [
        'text', 'single_select', 'multiple_select',
        'number', 'email'
      ]
    }
  }
}
</script>
