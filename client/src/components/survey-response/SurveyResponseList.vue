<template>
  <div>
    <b-table
      :data="responses"
      :loading="loading">

      <b-table-column label="Survey Name" v-slot="props">
        {{ props.row.survey ? props.row.survey.name : 'N/A'}}
      </b-table-column>
      <b-table-column label="Posted by" v-slot="props">
        {{ props.row.user ? props.row.user.name : 'N/A' }}
      </b-table-column>
      <b-table-column label="Survey time" v-slot="props">
        {{ props.row.created_time | humanTime }}
      </b-table-column>
      <b-table-column label="Actions" v-slot="props">
        <b-tooltip
          label="View the whole response."
          position="is-top">
          <b-button
            style="margin-right: 2px"
            outlined
            type="is-primary" size="is-small"
            icon-pack="fas" icon-left="eye"></b-button>
        </b-tooltip>
        <b-tooltip label="DELETE!! Will be lost forever" position="is-top">
          <b-button
            outlined @click="deleteSurveyResponse(props.row.id)"
            type="is-danger" size="is-small"
            icon-pack="fas" icon-left="trash"></b-button>
        </b-tooltip>
      </b-table-column>

      <template #empty>
        <div class="has-text-centered">No records</div>
      </template>
    </b-table>
  </div>
</template>

<script>
import { _get } from '@/utils/api-request'

export default {
  name: 'SurveyResponseList',
  data () {
    return {
      responses: [],
      loading: false
    }
  },
  mounted () {
    this.getSurveyResponses()
  },
  methods: {
    async getSurveyResponses () {
      try {
        this.loading = true
        const response = await _get({ path: '/v1/survey-responses/' })
        if (response.status === 200) {
          this.responses = response.data
          this.loading = false
        }
      } catch (e) {
        console.log(e.response)
        this.loading = false
      }
    },
    async deleteSurveyResponse (surveyResponseId) {
      console.log(surveyResponseId)
    }
  },
  filters: {
    humanTime (value) {
      return new Date(value).toUTCString()
    }
  }
}
</script>

<style scoped>

</style>
