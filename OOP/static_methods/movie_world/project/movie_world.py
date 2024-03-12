from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    CAPACITY = 15
    CUS_CAPACITY = 10


    def __init__(self, name: str):
        self.name = name
        self.customers = List[Customer] = []
        self.dvds = List[DVD] = []

    def dvd_capacity(self):
        return MovieWorld.CAPACITY

    def customer_capacity(self):
        return MovieWorld.CUS_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUS_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.CAPACITY:
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
            customer.rented_dvds.append(dvd)
            return f"{customer.name} has successfully rented {dvd.name}"



