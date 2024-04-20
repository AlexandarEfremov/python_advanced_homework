from project.movie_specification.movie import Movie


class Action(Movie):
    def __init__(self, title: str, year: int, owner: object):
        super().__init__(title, year, owner, age_restriction=12)

    def details(self):
        return (f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction},"
                f" Likes:{self.likes}, Owned by:{self.owner.name}")
