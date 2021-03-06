import os
import uuid

import pytest
import sqlalchemy
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.core.database import get_db
from api.core.model_base import ModelBase
from api.survey.enums.survey_enums import SurveyStatusEnum
from api.main import app
from api.survey.models import Survey, SurveyQuestion, SurveySection
from api.auth.models.user import User

SQLALCHEMY_DATABASE_URL = os.environ.get('TESTING_DB_CONN_STRING')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# Set up the database once
ModelBase.metadata.drop_all(bind=engine)
ModelBase.metadata.create_all(bind=engine)


@pytest.fixture()
def session():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    # Begin a nested transaction (using SAVEPOINT).
    nested = connection.begin_nested()

    # If the application code calls session.commit, it will end the nested
    # transaction. Need to start a new one when that happens.
    @sqlalchemy.event.listens_for(session, "after_transaction_end")
    def end_savepoint(session, transaction):
        nonlocal nested
        if not nested.is_active:
            nested = connection.begin_nested()

    yield session

    # Rollback the overall transaction, restoring the state before the test ran.
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]


@pytest.fixture()
def auth_token(client):
    user_create_response = client.post('/api/v1/users/', json={
        'name': 'Tester',
        'email': 'tester@mail.com',
        'password': '1234',
        'confirm_password': '1234'
    })
    if user_create_response.status_code == 201:
        response = client.post('/api/v2/login/', json={
            "username": "tester@mail.com",
            "password": "1234"
        })
        if response.status_code == 200:
            yield response.json()['access_token']


@pytest.fixture()
def test_data(client, session):
    """
    This fixures is mean to create some test data as the dependency of the each unit of
    tests. We will always access the with O(n) time. The data format is following...
    {
        'KEY': [ # A key is must be the model name. i.e: User.__name__
            # A list of objects
            {
                id: 1,
                name: 'test maybe'
            }
        ]
    }
    """
    # Create Test users
    _users = []
    for i in range(1, 4):
        user_create_response = client.post('/api/v1/users/', json={
            'name': f'Tester {i}',
            'email': f'test{i}@mail.com',
            'password': '1234',
            'confirm_password': '1234'
        })
        _users.append(user_create_response.json())
    # Create Surveys
    _surveys = []
    for i in range(1, 4):
        survey = Survey(
            name=f'Test {i}', instructions=f'Instruction {i}',
            status=SurveyStatusEnum.Published.value, slug=uuid.uuid4().hex,
            user_id=_users[0]['id']
        )
        session.add(survey)
        session.commit()
        _surveys.append({
            'id': survey.id,
            'slug': survey.slug,
            'name': survey.name
        })
    # Create Sections
    _sections = []
    for i in range(1, 4):
        sec = SurveySection(name=f'Section {i}', survey_id=_surveys[i-1]['id'])
        session.add(sec)
        session.commit()
        _sections.append({
            'id': sec.id,
            'name': sec.name
        })
    # Create Questions
    _questions = []
    for i in range(1, 4):
        ques = SurveyQuestion(
            text=f'Test {i}', text_translation=f'Test {i}', type='text',
            section_id=_sections[i-1]['id'], survey_id=_surveys[i-1]['id'],
            status=SurveyStatusEnum.Published.value, is_required=True
        )
        session.add(ques)
        session.commit()
        _questions.append({
            'id': ques.id,
            'text': ques.text
        })
    yield {
        User.__name__: _users,
        Survey.__name__: _surveys,
        SurveyQuestion.__name__: _questions,
    }
