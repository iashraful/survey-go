<template>
  <div>
    <b-table
      :data="surveys"
      :loading="loading">

      <b-table-column label="Survey Name" v-slot="props">
        {{ props.row.name }}
      </b-table-column>
      <b-table-column label="Instructions" v-slot="props">
        {{ props.row.instructions | truncate(50) | default }}
      </b-table-column>
      <b-table-column label="Status" v-slot="props">
        {{ props.row.status | default }}
      </b-table-column>
      <b-table-column label="Actions">
        <b-tooltip label="Publish the survey to collect data" position="is-top">
          <b-button
            style="margin-right: 2px"
            outlined type="is-success" size="is-small"
            icon-pack="fas" icon-left="check"></b-button>
        </b-tooltip>
        <b-tooltip label="Edit the survey before you publish it" position="is-top">
          <b-button
            style="margin-right: 2px"
            type="is-info" size="is-small" outlined
            icon-pack="fas" icon-left="edit"></b-button>
        </b-tooltip>
        <b-tooltip label="DELETE!! Will be lost forever" position="is-top">
          <b-button
            outlined
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
  name: 'SurveyList',
  data () {
    return {
      surveys: [],
      loading: true
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
          this.loading = false
        }
      } catch (e) {
        console.log(e.response)
        this.loading = false
      }
    }
  },
  filters: {
    truncate (text, stop, clamp) {
      return text.slice(0, stop) + (stop < text.length ? clamp || '...' : '')
    },
    default (value) {
      return value || 'N/A'
    }
  }
}
</script>
