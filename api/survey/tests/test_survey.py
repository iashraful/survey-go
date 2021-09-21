from api.survey.models import Survey
from api.survey.enums.survey_enums import QuestionTypeEnum
# WE MUST IMPORT ALL THE FIXTURES WE HAVE DEFINED DURING SETUP PHASE
from .setup import client, session, auth_token, test_data


def test_create_survey(client, auth_token):
    json_data = {
        "name": "Test Survey",
        "instructions": "As usual to follow...",
        "sections": [
            {
                "name": "Test Section",
                "questions": [
                    {
                        "text": "What's you name?",
                        "text_translation": "What's you name?",
                        "type": QuestionTypeEnum.Text.value,
                        "is_required": True,
                        "options": [

                        ]
                    },
                    {
                        "text": "What's your favorite from following?",
                        "text_translation": "",
                        "type": QuestionTypeEnum.SingleSelect.value,
                        "is_required": True,
                        "options": [
                            {
                                "name": "Apple",
                                "name_translation": ""
                            },
                            {
                                "name": "Money",
                                "name_translation": ""
                            },
                            {
                                "name": "iPhone",
                                "name_translation": ""
                            }
                        ]
                    }
                ]
            }
        ],

    }
    response = client.post('/api/v1/surveys/', json=json_data,
                           headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 201


def test_get_survey_list(client, auth_token):
    response = client.get('/api/v1/surveys/',
                          headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200


def test_get_survey_details(client, auth_token, test_data):
    _survey_slug = test_data[Survey.__name__][0]['slug']
    response = client.get(
        f'/api/v1/surveys/{_survey_slug}/',
        headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
