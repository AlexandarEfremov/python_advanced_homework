from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Laptop" or type_computer == "Desktop Computer":

            if type_computer == "Laptop":
                result = Laptop(manufacturer, model)
                result.configure_computer(processor, ram)
                self.warehouse.append(result)
            else:
                result = DesktopComputer(manufacturer, model)
                result.configure_computer(processor, ram)
                self.warehouse.append(result)

        raise ValueError(f"{type_computer} is not a valid type computer!")

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        pass

