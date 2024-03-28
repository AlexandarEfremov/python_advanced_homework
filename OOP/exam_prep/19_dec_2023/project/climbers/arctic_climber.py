from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200

    def __init__(self, name: str, conquered_peaks: list, is_prepared: bool):
        super().__init__(name, self.INITIAL_STRENGTH, conquered_peaks, is_prepared)

    def can_climb(self):
        if self.strength >= 100:
            return True

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 20
            self.strength *= 2
        else:
            self.strength -= 20
            self.strength *= 1.5
        self.conquered_peaks.append(peak)


