from typing import List, Optional

from pydantic import BaseModel

from api.enums.survey_enums import SurveyStatusEnum
from api.schemas.v1.user import UserBasicSchema


class SurveySchema(BaseModel):
    id: int
    user_id: int
    name: str
    slug: str
    instructions: str
    status: Optional[str] = SurveyStatusEnum.Draft.value

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
    status: Optional[str] = SurveyStatusEnum.Draft.value
    is_required: Optional[bool] = False
    options: List[QuestionOptionCreateSchema]

    class Config:
        orm_mode = True


class SurveySectionCreateSchema(BaseModel):
    name: str
    questions: List[SurveyQuestionCreateSchema]

    class Config:
        orm_mode = True


class SurveyCreateSchema(BaseModel):
    name: str
    instructions: str
    status: Optional[str] = SurveyStatusEnum.Draft.value
    sections: List[SurveySectionCreateSchema]

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
    type: str
    status: Optional[str]
    is_required: Optional[bool]
    options: List[QuestionOptionDetailsSchema]

    class Config:
        orm_mode = True


class SurveySectionDetailsSchema(BaseModel):
    id: int
    name: str
    questions: List[SurveyQuestionDetailsSchema]

    class Config:
        orm_mode = True


class SurveyDetailsSchema(BaseModel):
    id: int
    user_id: int
    user: UserBasicSchema
    name: str
    slug: str
    instructions: str
    status: Optional[str]
    sections: List[SurveySectionDetailsSchema]

    class Config:
        orm_mode = True


class SurveyQuestionBasicSchema(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True
