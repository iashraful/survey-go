from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from api.core.auth import get_current_user
from api.core.database import get_db
from api.models import Survey, SurveyQuestion, User, QuestionOption
from api.schemas.v1.survey import SurveySchema, SurveyQuestionSchema, SurveyCreateSchema, SurveyDetailsSchema

router = APIRouter()


@router.get('/surveys/', response_model=List[SurveySchema])
def get_surveys(db: Session = Depends(get_db), c_user: User = Depends(get_current_user)):
    surveys = Survey.objects(db).filter_by(user_id=c_user.id).order_by(Survey.published_time.desc()).all()
    return surveys


@router.get('/surveys/{survey_id}/', response_model=SurveyDetailsSchema)
def get_survey_details(survey_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    survey_details = Survey.objects(db).get(ident=survey_id)
    return survey_details


@router.get('/questions/{survey_id}/', response_model=List[SurveyQuestionSchema])
def get_questions(survey_id: int, db: Session = Depends(get_db)):
    """
    Get Questions for a specific survey
    :param survey_id: This is survey ID
    :param db: This is a session instance to access the database gently
    :return: Sqlalchemy queryset of objects
    """
    questions = SurveyQuestion.objects(db).filter_by(survey_id=survey_id).all()
    return questions


@router.post('/surveys/', response_model=SurveyDetailsSchema)
def create_survey(survey: SurveyCreateSchema, db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    _survey = Survey(
        user_id=current_user.id, name=survey.name, instructions=survey.instructions
    )
    db.add(_survey)
    db.commit()
    _ques_option_list = []
    for question in survey.questions:
        _ques = SurveyQuestion(
            text=question.text, text_translation=question.text_translation,
            type=question.type, survey_id=_survey.id
        )
        db.add(_ques)
        db.commit()
        for opt in question.options:
            _ques_option_list.append(QuestionOption(
                name=opt.name, name_translation=opt.name_translation,
                question_id=_ques.id
            ))
    db.bulk_save_objects(_ques_option_list)
    db.commit()
    db.refresh(_survey)
    return _survey
