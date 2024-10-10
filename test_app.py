from app import is_birthday_today
from datetime import date
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_is_birthday_today():
    today = date.today()
    assert is_birthday_today(f"{today.year}-{today.month:02d}-{today.day:02d}") == True
    assert is_birthday_today("1990-01-01") == (date.today().month == 1 and date.today().day == 1)

def test_birthday_today(client):
    today = date.today()
    response = client.post('/', data={
        'name': 'John Doe',
        'dob': f"{today.year}-{today.month:02d}-{today.day:02d}"
    }, follow_redirects=True)
    assert b"Happy Birthday!" in response.data