from abc import ABC, abstractmethod


class Horse(ABC):
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @abstractmethod
    @property
    def speed(self):
        ...

    @abstractmethod
    @speed.setter
    def speed(self, value):
        ...

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @abstractmethod
    def train(self):
        ...
