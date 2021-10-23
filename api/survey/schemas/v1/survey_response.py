from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from api.survey.schemas.v1.survey import SurveyQuestionBasicSchema
from api.auth.schemas.v1.user import UserBasicSchema


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

class SurveyBasicInfo(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class SurveyResponseListSchema(BaseModel):
    id: int
    survey_id: Optional[int]
    survey: Optional[SurveyBasicInfo]
    slug: str
    user: Optional[UserBasicSchema]
    created_time: datetime

    class Config:
        orm_mode = True

class SurveyResponseDetailsSchema(BaseModel):
    id: int
    survey_id: int
    slug: str
    user: Optional[UserBasicSchema]
    created_time: datetime
    question_responses: List[QuestionResponseDetailsSchema]

    class Config:
        orm_mode = True
