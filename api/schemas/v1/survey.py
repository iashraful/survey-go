from typing import List

from pydantic import BaseModel

from api.schemas.v1.user import UserBasicSchema


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


# CREATE SCHEMAS
class QuestionOptionCreateSchema(BaseModel):
    name: str
    name_translation: str

    class Config:
        orm_mode = True


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


# DETAILS SCHEMAS
class QuestionOptionDetailsSchema(BaseModel):
    id: int
    name: str
    name_translation: str

    class Config:
        orm_mode = True


class SurveyQuestionDetailsSchema(BaseModel):
    id: int
    text: str
    text_translation: str
    status: str
    options: List[QuestionOptionDetailsSchema]

    class Config:
        orm_mode = True


class SurveyDetailsSchema(BaseModel):
    id: int
    user_id: int
    user: UserBasicSchema
    name: str
    instructions: str
    status: str
    questions: List[SurveyQuestionDetailsSchema]

    class Config:
        orm_mode = True
