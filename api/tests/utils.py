from .test_setup import client, test_db

def login(test_db):
    response = client.post('/api/v1/login', json={
        'username': 'test'
    })
