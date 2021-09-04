from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.core.model_base import ModelBase
from api.enums.survey_enums import SurveyStatusEnum


class Survey(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    instructions = Column(String, nullable=True)
    status = Column(String, default=SurveyStatusEnum.Draft.value)

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'surveys'


class SurveyQuestion(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    text_translation = Column(String, nullable=True)
    status = Column(String, default=SurveyStatusEnum.Draft.value)

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'questions'


class QuestionAnswer(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship(
        "SurveyQuestion",
        cascade="all",
        back_populates="answers",
    )
    answer_text = Column(String, nullable=True)

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'answers'
