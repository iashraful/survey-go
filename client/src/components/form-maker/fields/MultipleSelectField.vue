<template>
  <div class="text-input">
    <b-field :label="field.title">
      <b-select
        placeholder="Select multiple"
        multiple expanded
        v-model="value">
        <option
          v-for="option in field.options"
          :value="option.value"
          :key="option.value">
          {{ option.label }}
        </option>
      </b-select>
    </b-field>
  </div>
</template>

<script>
import AbstractField from '@/components/form-maker/fields/AbstractField'

export default {
  name: 'SingleSelectField',
  extends: AbstractField,
  data () {
    return {
      value: [],
      errorText: '',
      displayErrorMgs: false
    }
  }
}
</script>

<style scoped>

</style>
