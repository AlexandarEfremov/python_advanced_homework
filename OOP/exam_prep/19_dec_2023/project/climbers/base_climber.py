from abc import ABC, abstractmethod

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    MIN_STRENGTH = 0
    STRENGTH_INCREASE = 15

    def __init__(self, name: str, strength: float, conquered_peaks: list, is_prepared: bool):
        self.name = name
        self.strength = strength
        self.conquered_peaks = conquered_peaks
        self.is_prepared: is_prepared = True

    @staticmethod
    def climber_types():
        return ["Arctic "]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= self.MIN_STRENGTH:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        ...

    @abstractmethod
    def climb(self, peak : BasePeak):
        ...

    def rest(self):
        self.strength += self.STRENGTH_INCREASE

    def __str__(self):
        return (f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: "
                f"{self.strength:.1f} * Conquered peaks: {', '.join(self.conquered_peaks)} ///")




