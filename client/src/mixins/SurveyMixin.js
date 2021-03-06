export default {
  name: 'SurveyMixin',
  methods: {
    parseFinalSurveyForAPI (rawData) {
      const finalData = {}
      finalData.name = rawData.name
      finalData.instructions = rawData.instructions || ''

      finalData.sections = rawData.sections.map((sec) => {
        return {
          id: sec.id,
          name: sec.name,
          questions: sec.questions.map((ques) => {
            const temp = {
              id: ques.id,
              text: ques.text,
              is_required: ques.is_required,
              text_translation: ques.text_translation || ques.text,
              type: ques.type
            }
            if (['single_select', 'multiple_select'].includes(ques.type)) {
              temp.options = ques.options.map((opt) => {
                return {
                  id: opt.id,
                  name: opt.name,
                  name_translation: opt.name_translation || opt.name
                }
              })
            } else {
              temp.options = []
            }
            return temp
          })
        }
      })
      return finalData
    },
    parseApiSurveyToEditor (apiData) {
      const parsedData = {}
      parsedData.name = apiData.name
      parsedData.name_translation = apiData.name_translation
      parsedData.instructions = apiData.instructions
      parsedData.__id = apiData.slug
      parsedData.sections = apiData.sections.map((sec) => {
        return {
          __id: JSON.stringify(sec.id) || sec.name,
          id: sec.id,
          name: sec.name,
          questions: sec.questions.map((ques) => {
            return {
              __id: JSON.stringify(ques.id),
              id: ques.id,
              is_required: ques.is_required,
              text: ques.text,
              type: ques.type,
              text_translation: ques.text_translation,
              options: ques.options.map((opt) => {
                return {
                  __id: JSON.stringify(opt.id),
                  id: opt.id,
                  name: opt.name,
                  name_translation: opt.name_translation
                }
              })
            }
          })
        }
      })
      return parsedData
    }
  }
}
