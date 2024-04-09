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

    @staticmethod
    def __check_members(band):
        singer = next((s for s in band.members if s.__class__.__name__ == "Singer"), None)
        drummer = next((d for d in band.members if d.__class__.__name__ == "Drummer"), None)
        guitarist = next((g for g in band.members if g.__class__.__name__ == "Guitarist"), None)
        if singer and drummer and guitarist:
            return True
        return False

    @staticmethod
    def __type_concert(concert, band):
        cond = True
        if concert.genre == "Rock":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    cond = False
                if member.__class__.__name__ == "Singer" and "sing high pitch notes" not in member.skills:
                    cond = False
                if member.__class__.__name__ == "Guitarist" and "play rock" not in member.skills:
                    cond = False
        elif concert.genre == "Metal":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    cond = False
                if member.__class__.__name__ == "Singer" and "sing low pitch notes" not in member.skills:
                    cond = False
                if member.__class__.__name__ == "Guitarist" and "play metal" not in member.skills:
                    cond = False
        elif concert.genre == "Jazz":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drum brushes" not in member.skills:
                    cond = False
                if member.__class__.__name__ == "Singer"\
                        and ("sing high pitch notes" not in member.skills or "sing low pitch notes" not in member.skills):
                    cond = False
                if member.__class__.__name__ == "Guitarist" and "play jazz" not in member.skills:
                    cond = False
        return cond

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        musician = next((m for m in self.musicians if m.name == name), None)
        if musician:
            raise Exception(f"{name} is already a musician!")
        else:
            new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
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
        same_place = next((p for p in self.concerts if p.place == place), None)
        if same_place:
            raise Exception(f"{place} is already registered for {same_place.genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{new_concert.genre} concert in {new_concert.place} was added."

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

    def start_concert(self, concert_place: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)
        if self.__check_members(band) is False:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")
        concert_event = next((c for c in self.concerts if c.place == concert_place), None)
        if self.__type_concert(concert_event, band) is False:
            raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profits = (concert_event.ticket_price * concert_event.audience) - concert_event.expenses
        return f"{band_name} gained {profits:.2f}$ from the {concert_event.genre} concert in {concert_place}."

