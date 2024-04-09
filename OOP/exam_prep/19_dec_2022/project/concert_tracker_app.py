from typing import List

from project import concert
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
            new_musician = Musician(name, age)
            self.musicians.append(new_musician)
            return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = next((b for b in self.bands if b.name == name), None)
        if band:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if place in Concert.place:
            raise Exception(f"{place} is already registered for {Concert.genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

    def add_musician_to_band(self, musician_name: str, band_name: str):
        m_name = next((m for m in self.musicians if m.name == musician_name), None)
        if m_name is None:
            raise Exception(f"{musician_name} isn't a musician!")
        b_name = next((b for b in self.bands if b.name == band_name), None)
        if b_name is None:
            raise Exception(f"{band_name} isn't a band!")
        b_name.members.append(m_name)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        b_name = next((b for b in self.bands if b.name == band_name), None)
        if b_name is None:
            raise Exception(f"{band_name} isn't a band!")
        desired_musician = next((m for m in b_name.members if m.name == musician_name), None)
        if desired_musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        b_name.members.remove(desired_musician)
        return f"{musician_name} was removed from {band_name}."

