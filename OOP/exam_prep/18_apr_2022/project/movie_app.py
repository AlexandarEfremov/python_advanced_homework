from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        pass

    def upload_movie(self, username: str, movie: Movie):
        pass

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        pass

    def delete_movie(self, username: str, movie: Movie):
        pass

    def like_movie(self, username: str, movie: Movie):
        pass

    def dislike_movie(self, username: str, movie: Movie):
        pass

    def display_movies(self):
        pass

    def __str__(self):
        pass
