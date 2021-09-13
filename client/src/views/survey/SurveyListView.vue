<template>
  <div>
    <div class="survey-list-view" style="margin-bottom: 2px">
      <div class="title">Surveys</div>
      <div class="action-btns">
        <router-link :to="`${$route.path}/create`">
        <b-button size="is-small" icon-pack="fa" type="is-info" icon-left="plus">
          Add
        </b-button>
        </router-link>
      </div>
    </div>
    <hr style="margin-top: 0"/>
    <survey-list />
  </div>
</template>

<script>
import SurveyList from '../../components/survey/SurveyList.vue'

export default {
  name: 'SurveyListView',
  components: { SurveyList }
}
</script>

<style scoped>
  .survey-list-view {
    display: block;
    width: 100%;
  }
  .survey-list-view .title {
    margin-bottom: 5px;
  }
  .survey-list-view div {
    display: inline;
  }
  .survey-list-view .action-btns {
    float: right
  }
  .survey-list-view .action-btns button {
    margin-right: 5px;
  }
</style>
