from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity(self):
        return 15

    @staticmethod
    def customer_capacity(self):
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next(filter(lambda c: c.personal_id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.dvd_id == dvd_id, self.dvds))

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            customer.rented_dvds.append(dvd.dvd_id)
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = next(filter(lambda c: c.personal_id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.dvd_id == dvd_id, self.dvds))

        if dvd.dvd_id not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        else:
            customer.rented_dvds.remove(dvd.dvd_id)
            return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        return "\n".join([
            *[str(c) for c in self.customers],
            *[str(d) for d in self.dvds],
        ])
