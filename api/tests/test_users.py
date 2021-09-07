# WE MUST IMPORT ALL THE FIXTURES WE HAVE DEFINED DURING SETUP PHASE
from .test_setup import client, session


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



# def test_login(client):
#     response = client.post('/api/v1/login', files={
#         'username': (None, 'tester@mail.com'),
#         'password': (None, '1234')
#     }, headers={'Content-Type': 'form-data'})
#     assert response.status_code == 200



# def test_get_user_list(client):
#     response = client.get('/api/v1/users/', headers={'Authorization': f'Bearer TEST.TEST.TEST'})
#
#     assert response.status_code == 200
#     assert response.json() == []
