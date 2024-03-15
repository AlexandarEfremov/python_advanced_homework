from project.formula_teams.formula_team import FormulaTeam
from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp(FormulaTeam):
    def __init__(self, red_bull_team: None, mercedes_team: None, budget: int):
        super().__init__(budget)
        self.red_bull_team = red_bull_team
        self.mercedes_team = mercedes_team

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name == "Red Bull" or team_name == "Mercedes":
            if team_name == "Red Bull":
                self.red_bull_team = team_name
                self.budget = budget
                return f"{ team_name } has joined the new F1 season."
            else:
                self.mercedes_team = team_name
                self.budget = budget
                return f"{team_name} has joined the new F1 season."
        raise ValueError("Invalid team name!")

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")
        return (f"Red Bull: {RedBullTeam.calculate_revenue_after_race(red_bull_pos)}. "
                f"Mercedes: {MercedesTeam.calculate_revenue_after_race(mercedes_pos)}. "
                f"{'Red Bull' if red_bull_pos > mercedes_pos else 'Mercedes'} is ahead at the {race_name} race.")

