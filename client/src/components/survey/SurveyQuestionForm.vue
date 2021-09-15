<template>
  <div class="question">
    <div class="actions">
      <div class="ques-title">
        <h3 class="subtitle">Question: #{{ index + 1 }}</h3>
      </div>
      <div class="ques-action">
        <b-button
          @click="handleQuestionRemove"
          size="is-small" icon-pack="fa"
          type="is-danger" icon-left="trash">
          Remove
        </b-button>
      </div>
      <hr/>
    </div>

    <div class="field">
      <b-field label="Type" horizontal>
        <b-select placeholder="Select a name" v-model="question.type" expanded size="is-small">
          <option
            v-for="option in questionsTypes"
            :value="option"
            :key="option">
            {{ option }}
          </option>
        </b-select>
      </b-field>
      <b-field label="Text" horizontal>
        <b-input v-model="question.text" required size="is-small"></b-input>
      </b-field>
      <b-field label="Translation" horizontal>
        <b-input v-model="question.text_translation" size="is-small"></b-input>
      </b-field>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SurveyQuestionForm',
  props: {
    index: {
      type: Number,
      required: true
    },
    identity: {
      type: Number,
      required: true
    }
  },
  data () {
    return {
      question: { text: '', text_translation: '', type: 'text', __id: this.identity },
      questionsTypes: [
        'text', 'single_select', 'multiple_select',
        'number', 'email'
      ]
    }
  },
  methods: {
    handleQuestionRemove () {
      this.$emit('removeQuestion', this.identity)
    }
  },
  watch: {
    question: {
      handler (newValue) {
        console.log(newValue)
        this.question = newValue
        this.$emit('updateQuestion', { identity: this.identity, data: newValue })
      },
      deep: true
    }
  }
}
</script>

<style scoped>
.question {
  display: block;
  width: 100%;
  border: 1px solid rgb(189, 179, 179);
  border-radius: 5px;
  padding: 5px;
  margin-bottom: 5px;
}
.question .actions {
  display: block;
}
.question .actions .ques-title {
  display: inline-block;
  width: 70%;
}
.question .actions .ques-action {
  display: inline-block;
  width: 30%;
  text-align: right;
}
.question hr{
  margin-top: 3px;
}
.question .subtitle{
  margin-bottom: 3px;;
}
</style>
