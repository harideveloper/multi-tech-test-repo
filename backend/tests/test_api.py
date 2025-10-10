import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Test the hello endpoint"""
    rv = client.get('/')
    assert b"Hello from Flask!" in rv.data

def test_process_endpoint(client):
    """Test the process endpoint"""
    rv = client.post('/api/process', 
                     json={'data': 'test'},
                     content_type='application/json')
    assert rv.status_code == 200

# BUG: This test will fail if json import is missing in app.py
def test_process_with_json(client):
    """Test processing with JSON encoding"""
    rv = client.post('/api/process',
                     json={'key': 'value'},
                     content_type='application/json')
    assert rv.status_code == 200  # Updated assertion
    data = rv.get_json()
    assert data['status'] == 'success'