import pytest
from app import app

client = app.test_client()

def test_process_data():
    response = client.post('/api/data', json={'value': 10})
    assert response.json()['result'] == 10