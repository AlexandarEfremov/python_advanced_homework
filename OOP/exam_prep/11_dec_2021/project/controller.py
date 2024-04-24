from typing import List
from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar,
    }

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.VALID_CAR_TYPES:
            car_match = next((c for c in self.cars if c.model == model), None)
            if car_match:
                raise Exception(f"Car {model} is already created!")
            car = self.VALID_CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver_match = next((d for d in self.drivers if d.name == driver_name), None)
        if driver_match:
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race_match = next((r for r in self.races if r.name == race_name), None)
        if race_match:
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def __check_if_driver_exists(self, name):
        driver_match = next((d for d in self.drivers if d.name == name), None)
        if driver_match is None:
            raise Exception(f"Driver {name} could not be found!")
        return driver_match

    def __check_if_car_is_available(self, car_type):
        for i in range(len(self.cars) - 1, 0, -1):
            if type(self.cars[i]).__name__ == car_type and self.cars[i].is_taken is False:
                return self.cars.pop(i)
        else:
            raise Exception(f"Car {car_type} could not be found!")

    def __check_if_race_exists(self, name):
        race_match = next((r for r in self.races if r.name == name), None)
        if race_match is None:
            raise Exception(f"Race {name} could not be found!")
        return race_match

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver_object = self.__check_if_driver_exists(driver_name)
        car_object = self.__check_if_car_is_available(car_type)

        if driver_object.car:
            old_model = driver_object.car.model
            driver_object.car = car_object
            car_object.is_taken = True
            return f"Driver {driver_object.name} changed his car from {old_model} to {car_object.model}."

        driver_object.car = car_object
        car_object.is_taken = True
        return f"Driver {driver_object.name} chose the car {car_object.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race_object = self.__check_if_race_exists(race_name)
        driver_object = self.__check_if_driver_exists(driver_name)

        if driver_object.car is None:
            raise Exception(f"Driver {driver_object.name} could not participate in the race!")

        if driver_object not in race_object.drivers:
            race_object.drivers.append(driver_object)
            return f"Driver {driver_object.name} added in {race_object.name} race."

        return f"Driver {driver_object.name} is already added in {race_object.name} race."


    def start_race(self, race_name: str):
        pass
