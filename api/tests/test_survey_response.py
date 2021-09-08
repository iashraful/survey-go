import json

from api.models.survey import Survey, SurveyQuestion

from .setup import auth_token, client, session, test_data


def test_create_survey_response(client, auth_token, test_data):
    json_data = {
        "survey_id": test_data[Survey.__name__][0]['id'],
        "question_responses": [
            {
                "question_id": test_data[SurveyQuestion.__name__][0]['id'],
                "answer_text": "Apple Test"
            },
            {
                "question_id": test_data[SurveyQuestion.__name__][1]['id'],
                "answer_text": "Test Money"
            }
        ]
    }
    response = client.post('/api/v1/survey-responses/', json=json_data,
                           headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 201
