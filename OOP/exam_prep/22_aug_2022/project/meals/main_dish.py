from project.meals.meal import Meal


class MainDish(Meal):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, 50)

    def details(self):
        return f"Main Dish {self.name}: {self.price:.2f}lv/piece"
