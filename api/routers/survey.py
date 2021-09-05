from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from api.core.database import get_db
from api.models import Survey, SurveyQuestion
from api.schemas.survey import SurveySchema, SurveyQuestionSchema

router = APIRouter()


@router.get('/surveys/', response_model=List[SurveySchema])
def get_surveys(db: Session = Depends(get_db)):
    surveys = db.query(Survey).order_by(Survey.published_time.desc()).all()
    return surveys


@router.get('/questions/{survey_id}/', response_model=List[SurveyQuestionSchema])
def get_questions(survey_id: int, db: Session = Depends(get_db)):
    """
    Get Questions for a specific survey
    :param survey_id: This is survey ID
    :param db: This is a session instance to access the database gently
    :return: Sqlalchemy queryset of objects
    """
    questions = db.query(SurveyQuestion).filter_by(survey_id=survey_id).all()
    return questions
