from typing import List

from project.band import Band
from project.band_members.musician import Musician
from project.concert import Concert
from project.band_members.singer import Singer
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer,
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        musician = next((m for m in self.musicians if m.name == name), None)
        if musician:
            raise Exception(f"{name} is already a musician!")
        else:
            self.musicians.append(musician)
            return f"{musician.name} is now a {musician_type}."
