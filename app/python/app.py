from fastapi import FastAPI
from typing import List
from utils import get_movies


app = FastAPI(title="Movie List API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie List API"}


@app.get("/movies", response_model=List[dict])
def list_movies():
    return get_movies()
