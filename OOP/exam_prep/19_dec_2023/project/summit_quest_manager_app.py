class SummitQuestManagerApp:
    CLIMBER_TYPES = ["ArcticClimber", "SummitClimber"]

    def __init__(self, climbers: list, peaks: list):
        self.climbers = climbers
        self.peaks = peaks

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."
        if climber_name in self.climbers:
            return f"{climber_name} has been already registered."
        self.climbers.append(climber_name)
        return f"{climber_name} is successfully registered as a {climber_type}."

