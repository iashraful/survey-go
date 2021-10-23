import uuid
from datetime import datetime
from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import session
from starlette.requests import Request

from api.auth.models import User
from api.core.auth import get_current_user
from api.core.database import get_db
from api.survey.models.survey_response import QuestionResponse, SurveyResponse
from api.survey.schemas.v1.survey_response import SurveyResponseCreateSchema, SurveyResponseDetailsSchema, \
    SurveyResponseListSchema

router = APIRouter()


@router.post('/survey-responses/',
             response_model=SurveyResponseDetailsSchema, status_code=201)
def create_survey_response(response: SurveyResponseCreateSchema, request: Request, db: session = Depends(get_db)):
    user = None
    if 'Authorization' in request.headers:
        _token = request.headers['Authorization'].split()[1]
        user = get_current_user(db=db, token=_token)
    instance = SurveyResponse(
        survey_id=response.survey_id, created_time=datetime.now(), slug=uuid.uuid4().hex
    )
    if user:
        instance.user_id = user.id
    db.add(instance)
    db.commit()
    _question_response_list = []
    for q_resp in response.question_responses:
        _question_response_list.append(QuestionResponse(
            question_id=q_resp.question_id,
            answer_text=q_resp.answer_text,
            survey_response_id=instance.id,
            created_time=datetime.now()
        ))
    db.bulk_save_objects(_question_response_list)
    db.commit()
    db.refresh(instance)
    return instance


@router.get('/survey-responses/', response_model=List[SurveyResponseListSchema], status_code=200)
def get_survey_responses(db: session = Depends(get_db), c_user: User = Depends(get_current_user)):
    responses = SurveyResponse.objects(session=db).order_by(SurveyResponse.created_time.desc()).all()
    return responses
