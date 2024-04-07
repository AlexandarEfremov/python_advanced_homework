from typing import List

from project.robots.base_robot import BaseRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService,
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")
        service = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

