from typing import List

from project.meals.meal import Meal
from project.client import Client


class FoodOrdersApp:
    MEAL_TYPES = ["Starter", "MainDish", "Dessert"]
    RECEIPT_NUMBER = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        find_if_client_exists = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if find_if_client_exists:
            raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ not in self.MEAL_TYPES:
                continue
            self.menu.append(meal)

    def show_menu(self):
        result = []

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        for m in self.menu:
            result.append(m.details())

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if client is None:
            self.register_client(client_phone_number)
            new_client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
            for meal, quantity in meal_names_and_quantities.items():
                desired_meal = next((m for m in self.menu if m.name == meal), None)
                if desired_meal is None:
                    raise Exception(f"{meal} is not on the menu!")
                if quantity > desired_meal.quantity:
                    raise Exception(f"Not enough quantity of {type(desired_meal).__name__}: {desired_meal.name}!")
                new_client.shopping_cart.append(desired_meal)
                new_client.bill += desired_meal.price * quantity
                desired_meal.quantity -= quantity
            return (f"Client {client_phone_number} successfully ordered "
                    f"{', '.join([m.name for m in new_client.shopping_cart])} for {new_client.bill:.2f}lv.")

        else:
            for meal, quantity in meal_names_and_quantities.items():
                desired_meal = next((m for m in self.menu if m.name == meal), None)
                if desired_meal is None:
                    raise Exception(f"{meal} is not on the menu!")
                if quantity > desired_meal.quantity:
                    raise Exception(f"Not enough quantity of {type(desired_meal).__name__}: {desired_meal.name}!")
                client.shopping_cart.append(desired_meal)
                client.bill += desired_meal.price * quantity
                desired_meal.quantity -= quantity
        return (f"Client {client_phone_number} successfully ordered {', '.join([m.name for m in client.shopping_cart])} "
                f"for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        for meal in client.shopping_cart:
            meal_in_menu = next((m for m in self.menu if m.name == meal.name), None)
            meal_in_menu.quantity += meal.quantity
        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        self.RECEIPT_NUMBER += 1
        current_bill = client.bill
        client.shopping_cart = []
        client.bill = 0
        return (f"Receipt #{self.RECEIPT_NUMBER} with total amount of {current_bill:.2f} "
                f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
