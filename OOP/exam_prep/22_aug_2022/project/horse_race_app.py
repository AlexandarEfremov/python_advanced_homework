from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    AVAILABLE_RACES = ["Winter", "Spring", "Autumn", "Summer"]

    HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = next((h for h in self.horses if h.name == horse_name), None)
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")
        else:
            new_horse = self.HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        else:
            new_jockey = Jockey(jockey_name, age)
            self.jockeys.append(new_jockey)
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type not in self.AVAILABLE_RACES:
            return f"Race {race_type} has been already created!"
        else:
            race = HorseRace(race_type)
            self.AVAILABLE_RACES.remove(race_type)
            self.horse_races.append(race)
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        horse = next((h for h in self.horses if h.__class__.__name__ == horse_type and h.is_taken is False), None)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if horse and jockey.horse:
            raise Exception(f"Jockey {jockey_name} already has a horse.")
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        wanted_race = next((r for r in self.horse_races if r.__class__.__name__ == race_type), None)
        if wanted_race is None:
            raise Exception(f"Race {race_type} could not be found!")
        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in wanted_race.jockeys:
            raise Exception(f"Jockey {jockey_name} has been already added to the {race_type} race.")
        wanted_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."
