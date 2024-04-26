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
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.number_of_successful_missions = 0
        self.number_of_not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        self.astronaut_repository.add(self.ASTRONAUT_TYPES[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items.extend(items.split(", "))
        self.planet_repository.add(planet)

        return f"Successfully added Planet: {planet.name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def __astronaut_list(self):
        available_to_go = []
        for astronaut in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen):
            if astronaut.oxygen > 30:
                available_to_go.append(astronaut)
        if available_to_go:
            return available_to_go[0:5]
        raise Exception("You need at least one astronaut to explore the planet!")

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if planet is None:
            raise Exception('Invalid planet name!')

        astronauts = self.astronaut_repository.find_astronauts_for_mission(5, 30)

        if len(astronauts) == 0:
            raise Exception('You need at least one astronaut to explore the planet!')

        participated_astronauts = 0

        for astronaut in astronauts:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated_astronauts += 1

        if len(planet.items) == 0:
            self.number_of_successful_missions += 1
            return f'Planet: {planet_name} was explored. {participated_astronauts} astronauts participated in collecting items.'
        else:
            self.number_of_not_completed_missions += 1
            return f'Mission is not completed.'

    def report(self):
        output = [f"{self.number_of_successful_missions} successful missions!",
                  f"{self.number_of_not_completed_missions} missions were not completed!", "Astronauts' info:"]

        for astronaut in self.astronaut_repository.astronauts:
            output.append(f'Name: {astronaut.name}')
            output.append(f"Oxygen: {astronaut.oxygen}")
            if astronaut.backpack:
                output.append(f"Backpack items: {', '.join(astronaut.backpack)}")
            else:
                output.append(f"Backpack items: none")

        return '\n'.join(output)
