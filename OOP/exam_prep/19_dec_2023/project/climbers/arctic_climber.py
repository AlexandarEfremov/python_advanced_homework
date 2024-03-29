from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200

    def __init__(self, name: str):
        super().__init__(name, ArcticClimber.INITIAL_STRENGTH)

    def can_climb(self):
        if self.strength >= 100:
            return True

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5
        self.conquered_peaks.append(peak.name)


