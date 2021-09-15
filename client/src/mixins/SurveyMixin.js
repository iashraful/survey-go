export default {
  name: 'SurveyMixin',
  methods: {
    parseFinalSurveyForAPI (rawData) {
      const finalData = {}
      finalData.name = rawData.name
      finalData.instructions = rawData.instructions || ''

      finalData.questions = rawData.questions.map((ques) => {
        const temp = {
          text: ques.text,
          text_translation: ques.text_translation || ques.text,
          type: ques.type
        }
        if (['single_select', 'multiple_select'].includes(ques.type)) {
          temp.options = ques.options.map((opt) => {
            return {
              name: opt.name,
              name_translation: opt.name_translation || opt.name
            }
          })
        } else {
          temp.options = []
        }
        return temp
      })
      return finalData
    }
  }
}
