from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        if self.robots:
            return f"{self.name} Main Service:\nRobots: {' '.join(el.name for el in self.robots)}"
        else:
            return f"{self.name} Main Service:\nRobots: none"

