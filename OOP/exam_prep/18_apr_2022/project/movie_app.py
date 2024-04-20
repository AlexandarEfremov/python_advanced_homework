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
        user = next((u for u in self.users_collection if u.username == username), None)
        if user is None:
            raise Exception("This user does not exist!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception(f"Movie already added to the collection!")
        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = next((u for u in self.users_collection if u.username == username), None)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for attribute, new_attribute in kwargs.items():
            setattr(movie, attribute, new_attribute)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)
        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = next((u for u in self.users_collection if u.username == username), None)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if self.movies_collection:
            sorted_movies_by_year = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))
            result = []
            [result.append(m.details()) for m in sorted_movies_by_year]
            return "\n".join(result)
        else:
            return "No movies found."

    def __str__(self):
        result = []
        if self.users_collection:
            result.append(f"All users: {', '.join([u.username for u in self.users_collection])}")
        else:
            result.append("All users: No users.")
        if self.movies_collection:
            result.append(f"All movies: {', '.join([m.title for m in self.movies_collection])}")
        else:
            result.append("All movies: No movies.")
        return "\n".join(result)