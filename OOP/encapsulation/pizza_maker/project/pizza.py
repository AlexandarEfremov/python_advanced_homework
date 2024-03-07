from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int, toppings: dict):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = toppings

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("The name cannot be an empty string")
        self.name = value

    @property
    def dough(self):
        return self.dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.dough = value

    @property
    def max_number_of_toppings(self):
        return self.max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if self.max_number_of_toppings > len(self.toppings.keys()):
            self.toppings[topping] = 0
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        pass
