from fastapi.testclient import TestClient
from app.main import app  # Ensure 'main' is correctly imported from 'app'

client = TestClient(app)

def test_list_movies():
    response = client.get("/movies")
    assert response.status_code == 200