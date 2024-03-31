from project.divers.base_diver import BaseDiver
from math import ceil


class ScubaDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, 540)

    def miss(self, time_to_catch: int):
        number = round(0.3 * time_to_catch)
        if (self.oxygen_level - number) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= number

    def renew_oxy(self):
        self.oxygen_level = 540

