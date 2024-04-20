from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        user = next((u for u in self.users_collection if u.username == username), None)
        if user:
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

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
