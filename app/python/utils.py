def get_movies():
    """
    Returns a static list of movies.
    In a real app, this could query a database or external API.
    """
    return [
        {"id": 1, "title": "The Matrix", "year": 1999, "rating": 8.7},
        {"id": 2, "title": "Inception", "year": 2010, "rating": 8.8},
        {"id": 3, "title": "Interstellar", "year": 2014, "rating": 8.6},
        {"id": 4, "title": "The Dark Knight", "year": 2008, "rating": 9.0}
    ]


def get_movie_by_id(movie_id: int):
    """Get a single movie by ID"""
    movies = get_movies()
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return None


def calculate_average_rating():
    """Calculate average rating of all movies"""
    movies = get_movies()
    if not movies:
        return 0
    total = sum(movie["rating"] for movie in movies)
    return total / len(movies)