from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from api.core.model_base import ModelBase
from api.enums.survey_enums import SurveyStatusEnum


class Survey(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    slug = Column(String, unique=True)
    instructions = Column(String, nullable=True)
    status = Column(String)
    published_time = Column(DateTime, nullable=True)

    # Define relationship
    user = relationship("User")
    questions = relationship(
        "SurveyQuestion", back_populates="survey",
    )
    sections = relationship("SurveySection", back_populates='survey')
    responses = relationship("SurveyResponse", back_populates='survey')

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'surveys'


class SurveySection(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    # Define relationship
    questions = relationship(
        "SurveyQuestion", back_populates="section",
    )
    survey = relationship(
        "Survey", back_populates="sections",
    )

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'sections'


class SurveyQuestion(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    section_id = Column(Integer, ForeignKey('sections.id'))
    text = Column(String)
    text_translation = Column(String, nullable=True)
    type = Column(String)
    status = Column(String)
    is_required = Column(Boolean, nullable=False)

    # Relationships
    options = relationship(
        "QuestionOption", cascade="all",
        back_populates="question",
    )
    section = relationship(
        "SurveySection", back_populates="questions",
    )
    survey = relationship(
        "Survey", back_populates="questions",
    )

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'questions'


class QuestionOption(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship(
        "SurveyQuestion", cascade="all",
        back_populates="options",
    )
    name = Column(String)
    name_translation = Column(String, nullable=True)

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'question_options'
