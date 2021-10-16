from typing import List, Optional

from pydantic import BaseModel

from api.auth.schemas.v1.user import UserBasicSchema
from api.survey.enums.survey_enums import SurveyStatusEnum


class SurveySchema(BaseModel):
    id: int
    user_id: int
    name: str
    slug: str
    instructions: str
    status: Optional[str]

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
    is_required: Optional[bool]
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


# Update Schemas
class QuestionOptionUpdateSchema(QuestionOptionCreateSchema):
    id: Optional[int]
    name: str
    name_translation: str

    class Config:
        orm_mode = True


class SurveyQuestionUpdateSchema(SurveyQuestionCreateSchema):
    id: Optional[int]
    text: str
    text_translation: Optional[str]
    type: str
    status: Optional[str] = SurveyStatusEnum.Draft.value
    is_required: Optional[bool]
    options: List[QuestionOptionUpdateSchema]

    class Config:
        orm_mode = True


class SurveySectionUpdateSchema(SurveySectionCreateSchema):
    id: Optional[int]
    name: str
    questions: List[SurveyQuestionUpdateSchema]


class SurveyUpdateSchema(SurveyCreateSchema):
    id: Optional[int]
    name: str
    instructions: str
    status: Optional[str] = SurveyStatusEnum.Draft.value
    sections: List[SurveySectionUpdateSchema]

    class Config:
        orm_mode = True


# Survey Partial Update Schema
class SurveyPublishSchema(BaseModel):
    status: str

    class Config:
        orm_mode = True
