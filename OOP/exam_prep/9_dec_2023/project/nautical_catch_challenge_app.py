from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {
        "FreeDiver": FreeDiver,
        "ScubaDiver": ScubaDiver,
    }

    FISH_TYPES = {
        "PredatoryFish": PredatoryFish,
        "DeepSeaFish": DeepSeaFish,
    }

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        try:
            diver = self.DIVER_TYPES[diver_type](diver_name)
        except KeyError:
            return f"{diver_type} is not allowed in our competition."

        if diver in self.divers:
            return f"{diver_name} is already a participant."
        else:
            self.divers.append(diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        try:
            fish = self.FISH_TYPES[fish_type](fish_name, points)
        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."

        if fish in self.fish_list:
            return f"{fish_name} is already permitted."
        else:
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        pass

    def health_recovery(self):
        pass

    def diver_catch_report(self, diver_name: str):
        pass

    def competition_statistics(self):
        pass

