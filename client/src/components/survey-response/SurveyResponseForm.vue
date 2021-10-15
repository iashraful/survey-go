<template>
  <div>
    <h2 class="title">Example 1</h2>
    <v-form-maker
      submitBtnText="Submit"
      :config="config"
    />
  </div>
</template>

<script>
import VFormMaker from '../form-maker/VFormMaker'

export default {
  components: { VFormMaker },
  name: 'SurveyResponseForm',
  data () {
    return {
      config: {
        props: [
          {
            group: 'Basic Information',
            fields: [
              {
                title: 'First Name',
                type: 'text',
                name: 'first_name',
                required: true
              },
              {
                title: 'Last Name',
                type: 'text',
                name: 'last_name'
              },
              {
                title: 'What do you use?',
                type: 'select',
                name: 'what_do_you_use',
                options: [
                  { label: 'Mobile Phone', value: 'Mobile Phone' },
                  { label: 'Land Line', value: 'Land Line' },
                  { label: 'Multiple Mobile Phones', value: 'Multiple Mobile Phones' },
                  { label: 'Nothing', value: 'Nothing' }
                ]
              },
              {
                title: 'What do Love?',
                type: 'multi_select',
                name: 'what_do_you_love',
                options: [
                  { label: 'Mobile Phone', value: 'Mobile Phone' },
                  { label: 'Land Line', value: 'Land Line' },
                  { label: 'Multiple Mobile Phones', value: 'Multiple Mobile Phones' },
                  { label: 'Nothing', value: 'Nothing' }
                ]
              },
              {
                title: 'Email',
                type: 'email',
                name: 'email',
                required: true
              },
              {
                title: 'Phone',
                type: 'number',
                name: 'phone_number',
                required: false
              },
              {
                title: 'Profile Picture',
                type: 'image',
                name: 'profile_photo',
                required: true
              }
            ]
          },
          {
            group: 'Location Information',
            fields: [
              {
                title: 'Address',
                type: 'text',
                name: 'address',
                required: true
              }
            ]
          }
        ]
      }
    }
  }
}
</script>

<style scoped>

</style>
