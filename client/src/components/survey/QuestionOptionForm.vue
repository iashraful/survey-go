<template>
  <div class="option-form">
    <div class="input-div">
      <b-field :label="`Option ${index + 1}`" horizontal>
        <b-input v-model="option.name" required size="is-small"></b-input>
      </b-field>
    </div>
    <div class="option-action">
      <b-button
        v-if="showOptionRemoveButton()"
        @click="handleRemoveOption"
        size="is-small" icon-pack="fa"
        type="is-danger" icon-left="trash">
      </b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuestionOptionForm',
  props: {
    index: {
      type: Number,
      required: true
    },
    optionCount: {
      type: Number,
      required: true
    },
    identity: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      option: { name: '', __id: this.identity }
    }
  },
  methods: {
    handleRemoveOption () {
      this.$emit('onOptionRemove', this.identity)
    },
    showOptionRemoveButton () {
      if (this.index !== 0 || this.optionCount > 1) {
        return true
      }
    }
  },
  watch: {
    option: {
      handler (newValue) {
        this.$emit('onOptionUpdate', { identity: this.identity, data: newValue })
      },
      deep: true
    }
  }
}
</script>

<style scoped>
.option-form {
  display: block;
  margin-left: 7rem;
}
.option-form .input-div {
  display: inline-block;
  width: 80%;
}
.option-form .option-action {
  display: inline-block;
  width: 20%;
  text-align: center;
}
</style>
