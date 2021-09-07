# WE MUST IMPORT ALL THE FIXTURES WE HAVE DEFINED DURING SETUP PHASE
from .test_setup import client, session, auth_token


def test_user_create(client):
    response = client.post('/api/v1/users/', json={
        'name': 'Tester',
        'email': 'tester@mail.com',
        'password': '1234',
        'confirm_password': '1234'
    })
    assert response.status_code == 201
    assert response.json()['name'] == 'Tester'
    assert response.json()['email'] == 'tester@mail.com'



def test_login(client):
    # Create User
    client.post('/api/v1/users/', json={
        'name': 'Tester',
        'email': 'tester@mail.com',
        'password': '1234',
        'confirm_password': '1234'
    })
    # Login with the created User
    response = client.post('/api/v2/login/', json={
        "username": "tester@mail.com",
        "password": "1234"
    })
    assert response.status_code == 200
    assert response.json()['token_type'] == 'bearer'



def test_get_user_list(client, auth_token):
    response = client.get('/api/v1/users/', headers={'Authorization': f'Bearer {auth_token}'})

    assert response.status_code == 200
