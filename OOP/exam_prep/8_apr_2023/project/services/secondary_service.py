from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        if self.robots:
            return (f"{self.name} Secondary Service:\n"
                    f"Robots: {' '.join(el.name for el in self.robots)}")
        else:
            return (f"{self.name} Secondary Service:\n"
                    f"Robots: none")