from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_list_movies():
    response = client.get("/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_movie():
    response = client.get("/movies/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

def test_read_movie_not_found():
    response = client.get("/movies/999")
    assert response.status_code == 404