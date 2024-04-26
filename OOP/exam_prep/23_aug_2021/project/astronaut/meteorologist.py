from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    UNIT = 15

    def __init__(self, name: str, oxygen=90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.UNIT
