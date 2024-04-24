from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if ((type(value).__name__ == "MuscleCar" and 250 <= value <= 450) or
                (type(value).__name__ == "SportsCar" and 400 <= value <= 600)):
            self.__speed_limit = value
        else:
            if type(value).__name__ == "MuscleCar":
                raise ValueError(f"Invalid speed limit! Must be between {250} and {450}!")
            else:
                raise ValueError(f"Invalid speed limit! Must be between {400} and {600}!")


