from pydantic import BaseModel


class SurveySchema(BaseModel):
    id: int
    name: str
    instructions: str
    status: str

    class Config:
        orm_mode = True


class SurveyQuestionSchema(BaseModel):
    id: int
    text: str
    survey_id: int
    text_translation: str
    status: str

    class Config:
        orm_mode = True


class QuestionAnswerSchema(BaseModel):
    id: int
    question_id: int
    answer_text: str

    class Config:
        orm_mode = True
