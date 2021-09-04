from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from api.core.model_base import ModelBase
from api.enums.survey_enums import SurveyStatusEnum


class Survey(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    instructions = Column(String, nullable=True)
    status = Column(String, default=SurveyStatusEnum.Draft.value)
    published_time = Column(DateTime, nullable=True)

    # Define relationship
    questions = relationship(
        "SurveyQuestion", cascade="all",
        back_populates="survey",
    )

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'surveys'


class SurveyQuestion(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    survey = relationship(
        "Survey", cascade="all",
        back_populates="questions",
    )
    text = Column(String)
    text_translation = Column(String, nullable=True)
    status = Column(String, default=SurveyStatusEnum.Draft.value)

    answers = relationship(
        "QuestionAnswer", cascade="all",
        back_populates="question",
    )

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'questions'


class QuestionAnswer(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship(
        "SurveyQuestion", cascade="all",
        back_populates="answers",
    )
    answer_text = Column(String, nullable=True)

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'answers'
