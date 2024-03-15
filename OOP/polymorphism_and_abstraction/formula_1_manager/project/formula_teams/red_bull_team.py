from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSE_PER_RACE = 250000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos == 1:
            revenue = 1500000 - self.EXPENSE_PER_RACE
        elif race_pos == 2:
            revenue = 800000 - self.EXPENSE_PER_RACE
        elif race_pos == 8:
            revenue = 20000 - self.EXPENSE_PER_RACE
        elif race_pos == 9 or race_pos == 10:
            revenue = 10000 - self.EXPENSE_PER_RACE
        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget {self.budget}$"
