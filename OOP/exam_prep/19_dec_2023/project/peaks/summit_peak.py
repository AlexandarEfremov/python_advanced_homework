from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    RECOMMENDED_GEAR = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def get_recommended_gear(self):
        return SummitPeak.RECOMMENDED_GEAR

    def calculate_difficulty_level(self):
        return "Extreme" if self.elevation > 2500 else "Advanced"
