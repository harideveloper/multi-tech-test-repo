from fastapi import FastAPI, HTTPException
from typing import List, Optional
import requests
from utils import get_movies, get_movie_by_id

app = FastAPI(title="Movie List API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie List API", "endpoints": ["/movies", "/movies/{id}", "/health"]}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/movies", response_model=List[dict])
def list_movies(limit: Optional[int] = None):
    """Get all movies, optionally limited"""
    movies = get_movies()
    if limit:
        return movies[:limit]
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    """Get a specific movie by ID"""
    movie = get_movie_by_id(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.get("/external/popular")
def get_popular_movies():
    """Fetch popular movies from external API"""
    try:
        response = requests.get("https://api.themoviedb.org/3/movie/popular", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        raise HTTPException(status_code=503, detail="External API unavailable")