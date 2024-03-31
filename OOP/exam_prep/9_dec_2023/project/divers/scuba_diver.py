from project.divers.base_diver import BaseDiver
from math import ceil


class ScubaDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=540)

    def original_ox(self):
        return 540

    def miss(self, time_to_catch: int):
        number = 0.3 * time_to_catch
        if isinstance(number, float):
            if self.oxygen_level >= ceil(number):
                self.oxygen_level -= ceil(number)
            else:
                self.oxygen_level = 0
        else:
            if self.oxygen_level >= number:
                self.oxygen_level -= number
            else:
                self.oxygen_level = 0

    def renew_oxy(self):
        add = self.original_ox()
        self.oxygen_level = add

