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
        client = Client(client_phone_number)
        client_num = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if client_num:
            return "The client has already been registered!"
        else:
            self.clients_list.append(client)
            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        [self.menu.append(m) for m in meals if m.__class__.__name__ in self.MEAL_TYPES]

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = []
        [result.append(m.details()) for m in self.menu]
        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        client_num = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if client_num is None:
            self.register_client(client_phone_number)
        for meal, quantity in meal_names_and_quantities.items():
            m_name = next((mn for mn in self.menu if mn.name == meal), None)
            if m_name is None:
                raise Exception(f"{meal} is not on the menu!")
            if quantity > m_name.quantity:
                raise Exception(f"Not enough quantity of {m_name.__class__.__name__}: {meal}!")
            else:
                client_num.shopping_list.append(m_name)
                bill_price = m_name.price * quantity
                client_num.bill += bill_price
                m_name.quantity -= quantity
        return f"Client {client_phone_number} successfully ordered {', '.join([m.name for m in client_num.shopping_list])} for {client_num.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        wanted_client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if not wanted_client.shopping_list:
            raise Exception("There are no ordered meals!")
        else:
            for meal in wanted_client.shopping_list:
                self.menu[meal].quantity += meal.quantity
            wanted_client.shopping_list = []
            wanted_client.bill = 0
            return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        wanted_client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)
        if not wanted_client.shopping_list:
            raise Exception("There are no ordered meals!")
        else:
            receipt_id = self.RECEIPT_NUMBER + 1
            return (f"Receipt #{receipt_id} with total amount of {wanted_client.bill:.2f} "
                    f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."



