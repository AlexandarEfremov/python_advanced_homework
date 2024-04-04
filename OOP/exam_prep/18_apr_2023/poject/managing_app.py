from typing import List

from poject.route import Route
from poject.user import User
from poject.vehicles.base_vehicle import BaseVehicle
from poject.vehicles.cargo_van import CargoVan
from poject.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan,
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        if user:
            return f"{driving_license_number} has already been registered to our platform."
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."
        other_car = next((l for l in self.vehicles if l.license_plate_number == license_plate_number), None)
        if other_car:
            return f"{license_plate_number} belongs to another vehicle."
        car = self.VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(car)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."



