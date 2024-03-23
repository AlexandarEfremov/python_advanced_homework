from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200,
    }

    VALID_RAM = [2 ** x for x in range(1, 7)]

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram not in self.VALID_RAM:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        return (f"Created {self.manufacturer} {self.model} with {self.processor} and"
                f" {self.ram}GB RAM for {self.AVAILABLE_PROCESSORS[processor]}$.")



