# tests/test_app.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_list_movies():
    response = client.get("/movies")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 4  # matches your static utils.py


def test_list_movies_with_limit():
    response = client.get("/movies?limit=2")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_get_movie_success():
    response = client.get("/movies/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "The Matrix"


def test_get_movie_not_found():
    response = client.get("/movies/999")
    assert response.status_code == 404
