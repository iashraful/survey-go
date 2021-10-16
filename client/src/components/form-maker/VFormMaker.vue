<template>
  <div class="form-builder">
    <form @submit.prevent="handleSubmit">
      <div v-for="(each, _i) in config.props" :key="_i">
        <h4 v-if="each.group !== undefined" class="label group-title">{{ each.group }}</h4>
        <div v-for="(item, index) in each.fields" :key="index" class="field-item">
          <text-input-field
            v-if="item.type === fieldTypes.text"
            :field="item"
            :submitted="submitted" @validate="checkValidation">
          </text-input-field>
          <number-input-field
            v-if="item.type === fieldTypes.number"
            :field="item"
            :submitted="submitted" @validate="checkValidation">
          </number-input-field>
          <positive-number-input-field
            v-if="item.type === fieldTypes.positiveNumber"
            :field="item"
            :submitted="submitted" @validate="checkValidation">
          </positive-number-input-field>
          <email-input-field
            v-if="item.type === fieldTypes.email"
            :field="item"
            :submitted="submitted" @validate="checkValidation">
          </email-input-field>
          <image-input-field
            v-if="item.type === fieldTypes.image"
            :field="item" :submitted="submitted"
            out-format="base64" @validate="checkValidation">
          </image-input-field>
          <multiple-select-field
            v-if="item.type === fieldTypes.multipleSelect"
            :field="item" :submitted="submitted" @validate="checkValidation">
          </multiple-select-field>
          <single-select-field
            v-if="item.type === fieldTypes.singleSelect"
            :field="item" :submitted="submitted" @validate="checkValidation">
          </single-select-field>
        </div>
      </div>
      <b-button
        class="submit-btn" type="is-primary"
        native-type="submit">{{ submitBtnText | setDefault('Submit') }}
      </b-button>
    </form>
  </div>
</template>

<script>
import './fields'
import fieldTypes from '@/utils/field-types'

export default {
  name: 'VFormMaker',
  props: ['config', 'submitBtnText'],
  data () {
    return {
      fieldTypes: fieldTypes,
      errors: false,
      formData: {},
      submitted: false
    }
  },
  methods: {
    handleSubmit () {
      this.submitted = true
      this.runValidation().then(() => {
        this.$emit('onSubmit', this.formData)
      }).catch((err) => {
        console.error(err)
      })
    },
    runValidation () {
      return new Promise((resolve, reject) => {
        let _error = false
        let errorItem
        Object.values(this.formData).map((item) => {
          if (!(item.status)) {
            _error = true
            errorItem = item
          }
        })
        if (_error) {
          reject(errorItem)
        } else {
          resolve(this.formData)
        }
      })
    },
    checkValidation (validatedData) {
      this.formData[validatedData.field.name] = validatedData
    }
  },
  filters: {
    setDefault (value, arg) {
      if (value === '' || value === undefined) {
        return arg
      }
      return value
    }
  }
}
</script>

<style scoped>
.form-builder {
  width: 100%;
}

.form-builder .group-title {
  margin-bottom: 5px;
  margin-top: 1.5rem;
  border-bottom: 1px solid #1f1d1d
}

.form-builder .field-item {
  padding-top: 8px;
  padding-left: 12px;
}

.form-builder .submit-btn {
  margin-top: 1.5rem;
  margin-bottom: 1.5rem;
  padding: 5px 20px;
}
</style>
