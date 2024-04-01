from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
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
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalphanum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        try:
            eq = self.VALID_EQUIPMENT[equipment_type]
        except KeyError:
            return "Invalid equipment type!"

        self.equipment.append(eq)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        try:
            team = self.VALID_TEAM_NAMES[team_type](team_name, country, advantage)
        except KeyError:
            return "Invalid team type!"

        if self.capacity > len(self.teams):
            self.teams.append(team)
            return f"{team_type} was successfully added."
        else:
            return "Not enough tournament capacity."

    def sell_equipment(self, equipment_type: str, team_name: str):

        equip = filter(lambda eq: eq.__class__.__name__ == equipment_type, self.equipment)
        team = filter(lambda t: t.name == team_name, self.teams)

        if team.budget - equip.price > 0:
            team.budget -= equip.price

            self.equipment.reverse()
            self.equipment.remove(equip)
            self.equipment.reverse()

            team.equipment.append(equip)
        else:
            return "Budget is not enough!"

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            return "No such team!"

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        else:
            self.teams.remove(team)
            return f"Successfully removed {team_name}."




