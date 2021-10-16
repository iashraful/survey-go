from api.core.model_base import ModelBase
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class SurveyResponse(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    slug = Column(String, unique=True)
    survey_id = Column(Integer, ForeignKey('surveys.id', ondelete='SET NULL'), nullable=True)

    # Relationship
    user = relationship("User", back_populates='responses')
    survey = relationship("Survey", back_populates='responses')
    question_responses = relationship(
        "QuestionResponse", back_populates='survey_response')
    created_time = Column(DateTime)

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'survey_responses'


class QuestionResponse(ModelBase):
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('questions.id', ondelete='SET NULL'), nullable=True)
    survey_response_id = Column(Integer, ForeignKey('survey_responses.id'))
    answer_text = Column(String(512))
    created_time = Column(DateTime)

    # Relationship
    survey_response = relationship(
        "SurveyResponse", back_populates='question_responses')
    question = relationship("SurveyQuestion")

    @classmethod
    def get_table_name(cls, make_plural=True):
        return 'question_responses'
