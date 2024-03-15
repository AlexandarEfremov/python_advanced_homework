from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSE_PER_RACE = 200000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos == 1:
            revenue = 1000000 - self.EXPENSE_PER_RACE
            self.budget += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
        elif race_pos == 3:
            revenue = 500000 - self.EXPENSE_PER_RACE
            self.budget += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
        elif race_pos == 5:
            revenue = 100000 - self.EXPENSE_PER_RACE
            self.budget += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
        elif race_pos == 6 or race_pos == 7:
            revenue = 50000 - self.EXPENSE_PER_RACE
            self.budget += revenue
            return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
