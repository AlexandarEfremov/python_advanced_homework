from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSE_PER_RACE = 250000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int) -> object:
        if race_pos == 1:
            revenue = 1_500_000 - self.EXPENSE_PER_RACE + 20_000
            self.budget += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
        elif race_pos == 2:
            revenue = 800000 - self.EXPENSE_PER_RACE + 20_000
            self.budget += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
        elif race_pos == 8:
            revenue = 20000 - self.EXPENSE_PER_RACE
            self.budget += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
        elif race_pos == 9 or race_pos == 10:
            revenue = 10000 - self.EXPENSE_PER_RACE
            self.budget += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"



