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

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1

        route_check = next((r for r in self.routes if r.start_point == start_point and r.end_point == end_point and
                            r.length == length), None)
        if route_check:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        second_check = next((r for r in self.routes if r.start_point == start_point and r.end_point == end_point and
                             r.length < length), None)
        if second_check:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        check_if_greater_length = next((r for r in self.routes if r.start_point == start_point
                                        and r.end_point == end_point and r.length > length))
        if check_if_greater_length:
            check_if_greater_length.is_locked = True

        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."



