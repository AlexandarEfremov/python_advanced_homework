from project.animals.animal import Bird
from project.food import Meat, Seed, Vegetable, Fruit


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    @property
    def gained_weight(self):
        return 0.25

    @property
    def food_that_eats(self):
        return [Meat]


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def gained_weight(self):
        return 0.35

