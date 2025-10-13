from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()

# Sample movie data
movies = [
    {"id": 1, "title": "Inception"},
    {"id": 2, "title": "Interstellar"},
]

@app.get("/movies")
def list_movies():
    return movies

@app.get("/movies/{movie_id}")
def read_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

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