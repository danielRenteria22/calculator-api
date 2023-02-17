import pytest

@pytest.mark.order(4)
def test_addition(client):
    operand_1 = 4
    operand_2 = 6
    operation_data = {
        'operation_type': 'ADDITION',
        'operand_1': operand_1,
        'operand_2': operand_2
    }
    headers = {
        'Authorization': f'Bearer {pytest.access_token}'
    }
    operation_response = client.post('/operation/execute',json=operation_data,headers=headers)
    assert operation_response.status_code == 200
    assert operation_response.json['data'] ==  operand_1 + operand_2

@pytest.mark.order(4)
def test_multiplication(client):
    operand_1 = 4
    operand_2 = 6
    operation_data = {
        'operation_type': 'MULTIPLICATION',
        'operand_1': operand_1,
        'operand_2': operand_2
    }
    headers = {
        'Authorization': f'Bearer {pytest.access_token}'
    }
    operation_response = client.post('/operation/execute',json=operation_data,headers=headers)
    assert operation_response.status_code == 200
    assert operation_response.json['data'] ==  operand_1 * operand_2

@pytest.mark.order(4)
def test_substraction(client):
    operand_1 = 4
    operand_2 = 6
    operation_data = {
        'operation_type': 'SUBSTRACTION',
        'operand_1': operand_1,
        'operand_2': operand_2
    }
    headers = {
        'Authorization': f'Bearer {pytest.access_token}'
    }
    operation_response = client.post('/operation/execute',json=operation_data,headers=headers)
    assert operation_response.status_code == 200
    assert operation_response.json['data'] ==  operand_1 - operand_2

@pytest.mark.order(4)
def test_substraction(client):
    operand_1 = 4
    operand_2 = 6
    operation_data = {
        'operation_type': 'DIVISION',
        'operand_1': operand_1,
        'operand_2': operand_2
    }
    headers = {
        'Authorization': f'Bearer {pytest.access_token}'
    }
    operation_response = client.post('/operation/execute',json=operation_data,headers=headers)
    assert operation_response.status_code == 200
    assert operation_response.json['data'] ==  operand_1 / operand_2

@pytest.mark.order(4)
def test_missing_operand(client):
    operand_1 = 4
    operand_2 = 6
    operation_data = {
        'operation_type': 'DIVISION',
        'operand_1': operand_1,
    }
    headers = {
        'Authorization': f'Bearer {pytest.access_token}'
    }
    operation_response = client.post('/operation/execute',json=operation_data,headers=headers)
    assert operation_response.json['error'] == True

@pytest.mark.order(4)
def test_divison_by_zero(client):
    operand_1 = 4
    operand_2 = 0
    operation_data = {
        'operation_type': 'DIVISION',
        'operand_1': operand_1,
        'operand_2': operand_2,
    }
    headers = {
        'Authorization': f'Bearer {pytest.access_token}'
    }
    operation_response = client.post('/operation/execute',json=operation_data,headers=headers)
    assert operation_response.json['error'] == True

@pytest.mark.order(4)
def test_negative_sqrt(client):
    operand_1 = -1
    operand_2 = 0
    operation_data = {
        'operation_type': 'SQUARE_ROOT',
        'operand_1': operand_1,
        'operand_2': operand_2,
    }
    headers = {
        'Authorization': f'Bearer {pytest.access_token}'
    }
    operation_response = client.post('/operation/execute',json=operation_data,headers=headers)
    assert operation_response.json['error'] == True

@pytest.mark.order(4)
def test_random_string(client):
    operation_data = {
        'operation_type': 'RANDOM_STRING',
        'operand_1': 0
    }
    headers = {
        'Authorization': f'Bearer {pytest.access_token}'
    }
    operation_response = client.post('/operation/execute',json=operation_data,headers=headers)
    assert type(operation_response.json['data']) == str