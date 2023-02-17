import pytest

@pytest.mark.order(1)
def test_create_user(client):
    data = {
        'username': pytest.email,
        'password': pytest.password
    }
    response = client.post('/user/create',json=data)
    assert response.status_code == 200
    assert response.json['error'] == False

@pytest.mark.order(2)
def test_create_user_fail(client):
    data = {
        'username': '-- DROP DATABSE@mail.com',
        'password': pytest.password
    }
    response = client.post('/user/create',json=data)
    assert response.status_code == 400
    assert response.json['error'] == True

@pytest.mark.order(3)
def test_login(client):
    data = {
        'username': pytest.email,
        'password': pytest.password
    }
    response = client.post('/user/login',json=data)
    assert response.status_code == 200
    assert response.json['error'] == False
    assert 'access_token' in response.json['data']['access_token']
    assert 'refresh_token' in response.json['data']['access_token']

    pytest.access_token = response.json['data']['access_token']['access_token']
    