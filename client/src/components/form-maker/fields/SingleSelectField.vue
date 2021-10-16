<template>
  <div class="text-input">
    <b-field :label="field.title">
      <b-select
        placeholder="Select one"
        expanded v-model="value">
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
  extends: AbstractField
}
</script>

<style scoped>

</style>
