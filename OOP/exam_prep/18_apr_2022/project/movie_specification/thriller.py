from project.movie_specification.movie import Movie


class Thriller(Movie):
    def __init__(self, title: str, year: int, owner: object):
        super().__init__(title, year, owner, age_restriction=16)

    def details(self):
        return (f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction},"
                f" Likes:{self.likes}, Owned by:{self.owner.name}")
