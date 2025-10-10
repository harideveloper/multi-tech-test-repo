import json

def get_movies():
    """
    Returns a static list of movies.
    In a real app, this could query a database or external API.
    """
    return [
        {"id": 1, "title": "The Matrix", "year": 1999},
        {"id": 2, "title": "Inception", "year": 2010},
        {"id": 3, "title": "Interstellar", "year": 2014},
        {"id": 4, "title": "The Dark Knight", "year": 2008}
    ]