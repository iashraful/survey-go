<template>
  <div class="section-form">
    <div
      class="card-header"
      role="button">
      <p class="card-header-title">
        <b-field :label="`Section #${index + 1}`" horizontal>
          <b-input v-model="section.name" required size="is-small"></b-input>
        </b-field>
      </p>
      <div class="card-header-icon">
        <b-button
          v-if="showRemoveSectionButton()"
          @click="handleRemoveSection"
          size="is-small" icon-pack="fa"
          type="is-danger" icon-left="times">
        </b-button>
      </div>
    </div>
    <b-collapse
      class="card"
      animation="slide"
      :open="true"
      @open="isOpen = index">
      <template #trigger="props">
        <b-icon
          class="collapse-btn"
          pack="fas"
          :icon="props.open ? 'chevron-up' : 'chevron-down'">
        </b-icon>
      </template>
      <div class="card-content">
        <div class="content">
          <survey-question-form
            v-for="(ques, _i) in section.questions" :key="ques.__id"
            :index="_i" :identity="ques.__id"
            :question-count="section.questions.length"
            :existing-question="ques"
            @onQuestionRemove="removeQuestionByIdentity"
            @onQuestionUpdate="updateQuestionByIdentity"
          />
          <div style="text-align: right;">
            <b-button
              @click="addMoreQuestion"
              icon-pack="fa" size="is-small"
              class="is-info" icon-left="plus">
              Add Question
            </b-button>
          </div>
        </div>
      </div>
    </b-collapse>
  </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import SurveyQuestionForm from './SurveyQuestionForm.vue'

export default {
  name: 'SurveySectionForm',
  components: { SurveyQuestionForm },
  props: {
    identity: {
      type: String,
      required: true
    },
    index: {
      type: Number,
      required: true
    },
    sectionCount: {
      type: Number,
      required: true
    },
    existingSection: {
      type: Object,
      required: false,
      default: () => {
      }
    }
  },
  data () {
    return {
      isOpen: 0,
      section: this.existingSection || {
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
    dataPassToParentOnUpdate (data) {
      this.$emit('onQuestionUpdate', data)
    },
    dataPassToParentOnRemove (identity) {
      this.$emit('onQuestionRemove', identity)
    },
    handleRemoveSection () {
      this.$buefy.dialog.confirm({
        title: 'Delete Section!!',
        message: 'Are you sure you want to <b>delete</b> this section? This action cannot be undone.',
        confirmText: 'Delete',
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () => this.$emit('onSectionRemove', this.identity)
      })
    },
    addMoreQuestion () {
      this.section.questions.push({
        text: '', text_translation: '', type: 'text', __id: uuidv4(), is_required: true, options: []
      })
    },
    updateQuestionByIdentity ({ identity, data }) {
      const _index = this.section.questions.findIndex(i => identity === i.__id)
      if (_index !== -1) {
        this.section.questions[_index] = data
      }
    },
    removeQuestionByIdentity (identity) {
      const _index = this.section.questions.findIndex(i => identity === i.__id)
      if (_index !== -1) {
        this.section.questions.splice(_index, 1)
      }
    },
    showRemoveSectionButton () {
      return this.index !== 0 || this.sectionCount > 1
    }
  },
  watch: {
    section: {
      handler (newValue) {
        this.$emit('onSectionUpdate', { identity: this.identity, data: newValue })
      },
      deep: true
    }
  }
}
</script>

<style scoped>
.section-form {
  margin-bottom: 1rem;
}

.section-form .card-header {
  padding-left: 10px;
}

.is-horizontal {
  width: 100% !important;
  font-weight: normal;
}

.collapse-btn {
  position: absolute;
  padding-left: 5px;
  top: -2.5rem;
  margin-right: 5px;
}
</style>
