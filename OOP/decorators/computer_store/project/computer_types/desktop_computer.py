from project.computer_types.computer import Computer
import math


class DesktopComputer(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def available_ram(self):
        return [2 ** x for x in range(1, 8)]

    def available_processors(self):
        return {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800,
    }

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram not in self.VALID_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        price = self.AVAILABLE_PROCESSORS[processor] + (math.log(2, self.ram)) * 100
        self.price = price
        return (f"Created {self.manufacturer} {self.model} with {self.processor} and "
                f"{self.ram}GB RAM for {price}$.")
