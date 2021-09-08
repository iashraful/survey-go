from datetime import datetime
from typing import List

from pydantic import BaseModel

from api.schemas.v1.survey import SurveyQuestionBasicSchema, SurveyQuestionDetailsSchema
from api.schemas.v1.user import UserBasicSchema


class QuestionResponseCreateSchema(BaseModel):
    question_id: int
    answer_text: str

    class Config:
        orm_mode = True


class SurveyResponseCreateSchema(BaseModel):
    survey_id: int
    question_responses: List[QuestionResponseCreateSchema]

    class Config:
        orm_mode = True


class QuestionResponseDetailsSchema(BaseModel):
    id: int
    question: SurveyQuestionBasicSchema
    answer_text: str
    created_time: datetime

    class Config:
        orm_mode = True


class SurveyResponseDetailsSchema(BaseModel):
    id: int
    survey_id: int
    user: UserBasicSchema
    created_time: datetime
    question_responses: List[QuestionResponseDetailsSchema]

    class Config:
        orm_mode = True
