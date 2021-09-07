import os

import pytest
import sqlalchemy
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.core.database import get_db
from api.core.model_base import ModelBase
from api.main import app

SQLALCHEMY_DATABASE_URL = os.environ.get('TESTING_DB_CONN_STRING')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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
