from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {
        "Gingerbread": Delicacy,
        "Stolen": Stolen,
    }

    BOOTH_TYPES = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth,
    }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = next((d for d in self.delicacies if d.name == name), None)
        if delicacy:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        deli = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(deli)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth_num = next((b for b in self.booths if b.booth_number == booth_number), None)
        if booth_num:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")
        new_booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        reserved_boot = next((b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people), None)
        if reserved_boot is None:
            raise Exception(f"No available booth for {number_of_people} people!")
        reserved_boot.is_reserved = True
        return f"Booth {reserved_boot.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        needed_booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        needed_deli_in_booth = next((d for d in needed_booth.delicacy_orders if d.name == delicacy_name), None)
        if needed_booth is None:
            raise Exception(f"Could not find booth {booth_number}!")
        if needed_deli_in_booth is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        else:
            return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        wanted_booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        total_bill = wanted_booth.price_for_reservation + sum((d.price for d in wanted_booth.delicacy_orders))
        self.income += total_bill
        wanted_booth.delicacy_orders = []
        wanted_booth.is_reserved = False
        wanted_booth.price_for_reservation = 0
        return f"Booth {booth_number}:\nBill: {total_bill:.2f}lv."

