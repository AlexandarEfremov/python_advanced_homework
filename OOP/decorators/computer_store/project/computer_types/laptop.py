from project.computer_types.computer import Computer
import math


class Laptop(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @property
    def type(self):
        return "laptop"

    @property
    def available_processors(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200,
        }

    @property
    def available_ram(self):
        return [2 ** x for x in range(1, 7)]
