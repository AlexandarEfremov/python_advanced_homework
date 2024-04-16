from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    def __init__(self, name: str, membership_type="Regular"):
        super().__init__(name, membership_type)

    def earning_points(self, order_amount: float):
        earned_amount = int(order_amount / 10)
        self.points += earned_amount
        return earned_amount
