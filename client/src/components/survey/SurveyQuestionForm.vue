<template>
  <div class="question">
    <div class="actions">
      <div class="ques-title">
        <h3 class="subtitle">Question: #{{ index + 1 }}</h3>
      </div>
      <div class="ques-action">
        <b-button
          v-if="showQuestionRemoveButton()"
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
            :value="option.value"
            :key="option.value">
            {{ option.title }}
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

    <div class="question-options" v-if="showOptionForm()">
      <question-option-form
        v-for="(opt, _i) in question.options" :key="opt.__id"
        :index="_i" :identity="opt.__id"
        :option-count="question.options.length"
        @onOptionRemove="handleOptionRemove"
        @onOptionUpdate="handleOptionUpdate"
      />
      <div class="option-actions">
        <b-button
          @click="handleOptionAdd"
          size="is-small" icon-pack="fa"
          type="is-info" icon-left="plus">
          Another Option
        </b-button>
      </div>
    </div>
  </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import QuestionOptionForm from './QuestionOptionForm.vue'

export default {
  name: 'SurveyQuestionForm',
  props: {
    index: {
      type: Number,
      required: true
    },
    identity: {
      type: String,
      required: true
    },
    questionCount: {
      type: Number,
      required: true
    }
  },
  components: { QuestionOptionForm },
  data () {
    return {
      question: {
        text: '',
        text_translation: '',
        type: 'text',
        __id: this.identity,
        options: [
          { name: '', __id: uuidv4() },
          { name: '', __id: uuidv4() }
        ]
      },
      questionsTypes: [
        { title: 'Text', value: 'text' },
        { title: 'Single Choice', value: 'single_select' },
        { title: 'Multiple Choice', value: 'multiple_select' },
        { title: 'Number', value: 'number' },
        { title: 'Email', value: 'email' }
      ]
    }
  },
  methods: {
    handleQuestionRemove () {
      this.$emit('removeQuestion', this.identity)
    },
    handleOptionRemove (identity) {
      const _index = this.question.options.findIndex(i => i.__id === identity)
      if (_index !== -1) {
        this.question.options.splice(_index, 1)
      }
    },
    handleOptionUpdate ({ identity, data }) {
      const _index = this.question.options.findIndex(i => identity === i.__id)
      if (_index !== -1) {
        this.question.options[_index] = data
      }
    },
    handleOptionAdd () {
      this.question.options.push({ name: '', __id: uuidv4() })
    },
    showQuestionRemoveButton () {
      if (this.index !== 0 || this.questionCount > 1) {
        return true
      }
    },
    showOptionForm () {
      return ['single_select', 'multiple_select'].includes(this.question.type)
    }
  },
  watch: {
    question: {
      handler (newValue) {
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

.question-options .option-actions {
  margin: 5px 5px 0 0;
  display: block;
  text-align: right;
}
</style>
