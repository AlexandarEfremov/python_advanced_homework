from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        pass

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        pass

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        pass

    def health_recovery(self):
        pass

    def diver_catch_report(self, diver_name: str):
        pass

    def competition_statistics(self):
        pass

