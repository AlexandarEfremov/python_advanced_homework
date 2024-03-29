from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    RECOMMENDED_GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def get_recommended_gear(self):
        return ArcticPeak.RECOMMENDED_GEAR

    def calculate_difficulty_level(self):
        return "Extreme" if self.elevation > 3000 else "Advanced"



