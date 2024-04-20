from typing import List

from project.movie_specification.movie import Movie


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List[Movie] = []
        self.movies_owned: List[Movie] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.strip() == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}",
                  f"Liked movies:",
                  ]
        if self.movies_liked:
            result.extend(m.details() for m in self.movies_liked)
        else:
            result.append("No movies liked.")
        result.extend("Owned movies:")

        if self.movies_owned:
            result.extend(m.details() for m in self.movies_owned)
        else:
            result.append("No movies owned.")
        return "\n".join(result)
