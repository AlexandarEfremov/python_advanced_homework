from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


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
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

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
                                        and r.end_point == end_point and r.length > length), None)
        if check_if_greater_length:
            check_if_greater_length.is_locked = True

        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int, is_accident_happened: bool):
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        route = next((r for r in self.routes if r.route_id == route_id), None)
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        ordered_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))

        if count >= len(damaged_vehicles):
            [(v.change_status(), v.recharge()) for v in ordered_vehicles]
            return f"{len(ordered_vehicles)} vehicles were successfully repaired!"
        else:
            counter = count
            for v in ordered_vehicles:
                if counter == 0:
                    break
                else:
                    v.change_status()
                    v.recharge()
                counter -= 1
            return f"{count} vehicles were successfully repaired!"

    def users_report(self):
        result = "*** E-Drive-Rent ***\n"
        all_users = [u for u in self.users]
        ordered_users = sorted(all_users, key=lambda u: (-u.rating))
        for user in ordered_users:
            result += f"{user.__str__()}\n"
        return result[:-1]
