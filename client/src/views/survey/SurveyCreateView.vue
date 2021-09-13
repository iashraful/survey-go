<template>
  <div>
    <div class="survey-create-view" style="margin-bottom: 2px">
      <div class="title">Create new Survey</div>
      <hr style="margin-top: 0"/>
      <survey-form/>
    </div>
  </div>
</template>

<script>
import SurveyForm from '../../components/survey/SurveyForm.vue'

export default {
  name: 'SurveyCreateView',
  components: { SurveyForm }
}
</script>

<style scoped>
.survey-create-view .title{
  margin-bottom: 5px;
}
</style>
