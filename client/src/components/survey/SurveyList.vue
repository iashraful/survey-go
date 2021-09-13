<template>
  <div>
    <b-table :data="surveys" :columns="columnsConfig"></b-table>
  </div>
</template>

<script>
import { _get } from '@/utils/api-request'

export default {
  name: 'SurveyList',
  data () {
    return {
      surveys: [],
      columnsConfig: [
        {
          field: 'name',
          label: 'Name'
        },
        {
          field: 'instructions',
          label: 'Instructions'
        },
        {
          field: 'status',
          label: 'Status'
        }
      ]
    }
  },
  mounted () {
    this.getSurveysFromApi()
  },
  methods: {
    async getSurveysFromApi () {
      try {
        const response = await _get({ path: '/v1/surveys/' })
        if (response.status === 200) {
          this.surveys = response.data
        }
      } catch (e) {
        console.log(e.response)
      }
    }
  }
}
</script>
