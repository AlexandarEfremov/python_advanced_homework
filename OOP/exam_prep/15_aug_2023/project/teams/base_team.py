from abc import ABC, abstractmethod
from math import floor

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team name cannot be empty!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value < 0:
            raise ValueError("Team name cannot be empty!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        ...

    def get_statistics(self):
        eq_price_formula = sum([x.price for x in self.equipment])
        eq_formula = floor(sum([x.protection for x in self.equipment]) / len(self.equipment))
        return (f"Name: {self.name}\nCountry: {self.country}\nAdvantage: {self.advantage} points\n"
                f"Budget: {self.budget}EUR\nWins: {self.wins}\n"
                f"Total Equipment Price: {eq_price_formula:.2f}\n"
                f"Average Protection: {eq_formula}")
