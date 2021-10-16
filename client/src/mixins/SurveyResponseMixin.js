import fieldTypes from '../utils/field-types'

export default {
  name: 'SurveyResponseMixin',
  methods: {
    parseSurveyToResponseFormConfig (surveyDetails) {
      const config = {}
      config.name = surveyDetails.name
      config.slug = surveyDetails.slug
      config.instructions = surveyDetails.instructions
      config.props = surveyDetails.sections.map((sec) => {
        const temp = {}
        temp.group = sec.name
        temp.id = sec.id
        temp.fields = sec.questions.map((ques) => {
          return {
            title: ques.text,
            type: ques.type,
            name: ques.id,
            required: ques.is_required,
            options: ques.options.map((opt) => {
              return {
                label: opt.name,
                value: opt.name
              }
            })
          }
        })
        return temp
      })
      return config
    },
    parseFormDataToAPI (data, survey) {
      const result = {
        survey_id: survey.id,
        question_responses: []
      }
      result.question_responses = Object.keys(data).map((_key) => {
        const temp = {
          question_id: _key,
          answer_text: data[_key][_key]
        }
        if (data[_key].field.type === fieldTypes.multipleSelect) {
          temp.answer_text = data[_key][_key].join('\n')
        }
        return temp
      })
      return result
    }
  }
}
