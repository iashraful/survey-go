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
      <b-table-column label="Actions" v-slot="props">
        <b-tooltip label="Publish the survey to collect data" position="is-top">
          <b-button
            style="margin-right: 2px"
            @click="publishSurvey(props.row.slug)"
            outlined type="is-success" size="is-small"
            icon-pack="fas" icon-left="check"></b-button>
        </b-tooltip>
        <b-tooltip label="Edit the survey before you publish it" position="is-top">
          <b-button
            tag="router-link"
            :to="`${$route.path}/edit/${props.row.slug}`"
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
import { _get, createOrUpdate } from '@/utils/api-request'

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
    },
    async publishSurvey (slug) {
      this.$buefy.dialog.confirm({
        title: 'Publish Survey!!',
        message: 'Are you sure you want to <b>Publish</b> this survey?',
        confirmText: 'Publish',
        type: 'is-success',
        iconPack: 'fas',
        hasIcon: true,
        onConfirm: async () => {
          try {
            const response = await createOrUpdate({
              path: `/v1/surveys/${slug}/publish/`, method: 'patch', data: { status: 'Published' }
            })
            if (response.status === 200) {
              this.findSurveyAndUpdateStatus('Published', slug)
              this.$buefy.toast.open({
                message: 'Survey published successfully.',
                type: 'is-success'
              })
            }
          } catch (e) {
            this.$buefy.toast.open({
              message: 'Error occurred during publish the survey.',
              type: 'is-danger'
            })
          }
        }
      })
    },
    findSurveyAndUpdateStatus (status, slug) {
      const _index = this.surveys.findIndex((i) => i.slug === slug)
      if (_index !== -1) {
        this.surveys[_index].status = status
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
