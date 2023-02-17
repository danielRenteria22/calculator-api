import pytest
import random
import string
from dotenv import load_dotenv

def pytest_configure(config):
    load_dotenv()
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(10))
    pytest.email = f'{result_str}@email.com'
    pytest.password = 'Admin_123'

@pytest.fixture()
def app():
    from main import app
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()