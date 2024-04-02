from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad,
    }

    VALID_TEAM_NAMES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam,
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENT:
            raise Exception("Invalid equipment type!")
        equipment = self.VALID_EQUIPMENT[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_NAMES:
            raise Exception("Invalid team type!")
        if len(self.teams) == self.capacity:
            return "Not enough tournament capacity."
        team = self.VALID_TEAM_NAMES[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equip = next((e for e in reversed(self.equipment) if e.__class__.__name__ == equipment_type), None)
        team = next(filter(lambda t: t.name == team_name, self.teams))

        if team.budget < equip.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equip)
        team.equipment.append(equip)
        team.budget -= equip.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            return "No such team!"

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        else:
            self.teams.remove(team)
            return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        eq_len = len([eq for eq in self.equipment if eq.__class__.__name__ == equipment_type])
        self.equipment = [eq.increase_price() for eq in self.equipment if eq.__class__.__name__ == equipment_type]
        return f"Successfully changed {eq_len}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_one = next(t for t in self.teams if t.name == team_name1)
        team_two = next(t for t in self.teams if t.name == team_name2)

        if team_one.__class__.__name__ != team_two.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team_one_protection = sum(e.protection for e in team_one.equipment)
        team_two_protection = sum(e.protection for e in team_two.equipment)

        team_one_result = team_one.advantage + team_one_protection
        team_two_result = team_two.advantage + team_two_protection

        if team_one_result > team_two_result:
            team_one.win()
            return f"The winner is {team_one.name}."
        elif team_one_result < team_two_result:
            team_two.win()
            return f"The winner is {team_two.name}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        teams = sorted(self.teams, key=lambda x: -x.wins)
        result = (f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\n"
                  f"Teams:\n")
        result += f"\n".join(t.get_statistics() for t in teams)

        return result





