from typing import List

from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUT_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }

    def __init__(self):
        self.planet_repository = []
        self.astronaut_repository = []

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")
        astro = next((a for a in self.astronaut_repository if a.name == name), None)
        if astro:
            return f"{name} is already added."
        new_astro = self.ASTRONAUT_TYPES[astronaut_type](name)
        self.astronaut_repository.append(new_astro)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        pass

    def retire_astronaut(self, name: str):
        pass

    def recharge_oxygen(self):
        pass

    def send_on_mission(self, planet_name: str):
        pass

    def report(self):
        pass
