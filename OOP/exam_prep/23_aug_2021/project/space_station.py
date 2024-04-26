from typing import List

from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUT_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }

    def __init__(self):
        self.planet_repository: List[PlanetRepository] = []
        self.astronaut_repository: List[AstronautRepository] = []

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")
        for item in self.astronaut_repository:
            for astr in item.astronauts:
                if astr.name == name:
                    return f"{name} is already added."

        new_astro = self.ASTRONAUT_TYPES[astronaut_type](name)
        new_astr_repo = AstronautRepository()
        new_astr_repo.add(new_astro)
        self.astronaut_repository.append(new_astr_repo)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        for item in self.planet_repository:
            for pla in item.planets:
                if pla.name == name:
                    return f"{name} is already added."

        new_pla = Planet(name)
        new_pla.items.extend(items)
        new_pla_repo = PlanetRepository()
        new_pla_repo.add(new_pla)
        self.planet_repository.append(new_pla_repo)
        return f"Successfully added Planet: {new_pla.name}."

    def retire_astronaut(self, name: str):
        pass

    def recharge_oxygen(self):
        pass

    def send_on_mission(self, planet_name: str):
        pass

    def report(self):
        pass
