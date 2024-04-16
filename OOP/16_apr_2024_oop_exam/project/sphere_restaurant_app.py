from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_WAITER_TYPES = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter,
    }

    VALID_CLIENT_TYPES = {
        "RegularClient": RegularClient,
        "VIPClient": VIPClient,
    }

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.VALID_WAITER_TYPES:
            return f"{waiter_type} is not a recognized waiter type."
        check_if_duplicate_name = next((w for w in self.waiters if w.name == waiter_name), None)
        if check_if_duplicate_name:
            return f"{waiter_name} is already on the staff."
        waiter = self.VALID_WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.VALID_CLIENT_TYPES:
            return f"{client_type} is not a recognized client type."
        check_if_duplicate_client_name = next((c for c in self.clients if c.name == client_name), None)
        if check_if_duplicate_client_name:
            return f"{client_name} is already a client."
        client = self.VALID_CLIENT_TYPES[client_type](client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        if waiter:
            return waiter.report_shift()
        else:
            return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        client = next((c for c in self.clients if c.name == client_name), None)
        if client:
            info = client.earning_points(order_amount)
            return f"{client_name} earned {info} points from the order."
        else:
            return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        client = next((c for c in self.clients if c.name == client_name), None)
        if client:
            discount_info = client.apply_discount()
            return f"{client_name} received a {discount_info[0]}% discount. Remaining points {discount_info[1]}"
        else:
            return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        waiters_total_earnings = sum([w.calculate_earnings() for w in self.waiters])
        clients_unused_points = sum([c.points for c in self.clients])
        result = ["$$ Monthly Report $$",
                  f"Total Earnings: ${waiters_total_earnings:.2f}",
                  f"Total Clients Unused Points: {clients_unused_points}",
                  f"Total Clients Count: {len(self.clients)}",
                  f"** Waiter Details **",
                  ]

        sorted_waiters = sorted(self.waiters, key=lambda w: (-w.calculate_earnings()))
        for waiter in sorted_waiters:
            info = waiter.calculate_earnings()
            result.append(waiter.__str__())
        # [result.append(w.calculate_earnings()) for w in sorted_waiters]

        return "\n".join(result)


