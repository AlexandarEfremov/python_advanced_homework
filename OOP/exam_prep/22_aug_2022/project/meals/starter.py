from project.meals.meal import Meal


class Starter(Meal):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, 60)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
