import pytest

def test_create_user(client):
    data = {
        'username': pytest.email,
        'password': pytest.password
    }
    response = client.post('/user/create',json=data)
    assert response.status_code == 200
    assert response.json['error'] == False

def test_create_user_fail(client):
    data = {
        'username': '-- DROP DATABSE@mail.com',
        'password': pytest.password
    }
    response = client.post('/user/create',json=data)
    assert response.status_code == 400
    assert response.json['error'] == True

    