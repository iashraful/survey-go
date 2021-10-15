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
    }
  }
}
