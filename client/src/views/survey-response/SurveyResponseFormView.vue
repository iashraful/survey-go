<template>
  <div>
    <div class="survey-response-list-view" style="margin-bottom: 2px">
      <div class="title">Survey Responses</div>
      <div class="action-btns">
        <router-link :to="`${$route.path}/create`">
        <b-button size="is-small" icon-pack="fa" type="is-info" icon-left="plus">
          Add
        </b-button>
        </router-link>
      </div>
    </div>
    <hr style="margin-top: 0"/>
    <survey-response-form/>
  </div>
</template>

<script>
import SurveyResponseForm from '@/components/survey-response/SurveyResponseForm'

export default {
  name: 'SurveyResponseFormView',
  components: {
    SurveyResponseForm
  }
}
</script>

<style scoped>
  .survey-response-list-view {
    display: block;
    width: 100%;
  }
  .survey-response-list-view .title {
    margin-bottom: 5px;
  }
  .survey-response-list-view div {
    display: inline;
  }
  .survey-response-list-view .action-btns {
    float: right
  }
  .survey-response-list-view .action-btns button {
    margin-right: 5px;
  }
</style>
