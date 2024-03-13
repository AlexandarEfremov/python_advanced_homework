from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_capacity: float, fuel_consumption: float):
        self.fuel_capacity = fuel_capacity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    CONDITIONER_ON = 0.9

    def drive(self, distance):
        consumption = (Car.CONDITIONER_ON + self.fuel_consumption) * distance


class Truck(Vehicle):
    CONDITIONER_ON = 1.6
    TANK_CAPACITY = 0.95

    def drive(self, distance):


