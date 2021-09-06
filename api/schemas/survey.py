from typing import List

from pydantic import BaseModel


class SurveySchema(BaseModel):
    id: int
    user_id: int
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

class QuestionOptionCreateSchema(BaseModel):
    name: str
    name_translation: str


class SurveyQuestionCreateSchema(BaseModel):
    text: str
    text_translation: str
    type: str
    options: List[QuestionOptionCreateSchema]

    class Config:
        orm_mode = True


class SurveyCreateSchema(BaseModel):
    name: str
    instructions: str
    questions: List[SurveyQuestionCreateSchema]

    class Config:
        orm_mode = True
