import pytest
from app import app

@pytest.fixture
def client():

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):

    response = client.get('/')
    assert response.status_code == 200
    assert b'Shopping List' in response.data

def test_add_item(client):

    response = client.post('/add', data={'item': 'Milk'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Milk' in response.data

def test_delete_item(client):

    client.post('/add', data={'item': 'Bread'}, follow_redirects=True)

    response = client.get('/delete/Bread', follow_redirects=True)
    assert response.status_code == 200
    assert b'Bread' not in response.data
