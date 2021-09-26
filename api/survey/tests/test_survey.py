from api.survey.models import Survey
from api.survey.enums.survey_enums import QuestionTypeEnum, SurveyStatusEnum
# WE MUST IMPORT ALL THE FIXTURES WE HAVE DEFINED DURING SETUP PHASE
from api.core.setup_tests import client, session, auth_token, test_data


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
    _data = response.json()
    assert _data['slug'] == _survey_slug


def test_update_survey(client, auth_token, test_data):
    _survey_slug = test_data[Survey.__name__][1]['slug']
    json_data = {
        "name": "My Test Survey",
        "instructions": "",
        "sections": [
            {
                "name": "Section 1",
                "questions": [
                    {
                        "text": "What's your name?",
                        "text_translation": "",
                        "type": "text",
                        "options": [],
                        "is_required": True
                    }
                ]
            }
        ]
    }
    response = client.put(
        url=f'/api/v1/surveys/{_survey_slug}/', json=json_data,
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 200
    _data = response.json()
    assert _data['slug'] == _survey_slug
    assert _data['name'] == 'My Test Survey'
    assert _data['sections'][0]['name'] == 'Section 1'
    assert len(_data['sections']) == 1
    assert len(_data['sections'][0]['questions']) == 1


def test_publish_survey(client, auth_token, test_data):
    _survey_slug = test_data[Survey.__name__][0]['slug']
    response = client.patch(
        url=f'/api/v1/surveys/{_survey_slug}/publish/',
        headers={'Authorization': f'Bearer {auth_token}'},
        json={'status': SurveyStatusEnum.Published.value}
    )
    assert response.status_code == 200
    _data = response.json()
    assert _data['status'] == SurveyStatusEnum.Published.value
    assert _data['slug'] == _survey_slug


def test_delete_survey(client, auth_token, test_data):
    _survey_slug = test_data[Survey.__name__][0]['slug']
    response = client.delete(
        url=f'/api/v1/surveys/{_survey_slug}/', headers={'Authorization': f'Bearer {auth_token}'}
    )
    assert response.status_code == 204
