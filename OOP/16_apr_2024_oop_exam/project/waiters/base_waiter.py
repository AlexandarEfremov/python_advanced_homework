from abc import ABC, abstractmethod


class BaseWaiter(ABC):
    def __init__(self, name: str, hours_worked: int):
        self.name = name
        self.hours_worked = hours_worked

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if 3 <= len(value) <= 50:
            self.__name = value
        else:
            raise ValueError("Waiter name must be between 3 and 50 characters in length!")

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if value < 0:
            raise ValueError("Cannot have negative hours worked!")
        self.__hours_worked = value

    @abstractmethod
    def calculate_earnings(self):
        ...

    @abstractmethod
    def report_shift(self):
        ...

    def __str__(self):
        return f"Name: {self.name}, Total earnings: ${self.calculate_earnings():.2f}"