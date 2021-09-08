from datetime import date, datetime
from api.models.survey_response import QuestionResponse, SurveyResponse
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import session

from api.core.auth import get_current_user
from api.models.user import User
from api.core.database import get_db
from api.schemas.v1.survey_response import SurveyResponseCreateSchema, SurveyResponseDetailsSchema

router = APIRouter()


@router.post('/survey-responses/',
             response_model=SurveyResponseDetailsSchema, status_code=201)
def create_survey_response(response: SurveyResponseCreateSchema, db: session = Depends(get_db),
                           current_user: User = Depends(get_current_user)):
    instance = SurveyResponse(
        survey_id=response.survey_id, created_time=datetime.now(),
        user_id=current_user.id
    )
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
    db.refresh(instance)
    return instance
