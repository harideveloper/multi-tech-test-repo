from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_movie():
    response = client.get("/movies/1")
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}. Check if the endpoint /movies/1 is implemented correctly."