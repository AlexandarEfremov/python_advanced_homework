class Customer:
    def __init__(self, name: str, age: int, personal_id: int):
        self.name = name
        self.age = age
        self.personal_id = personal_id
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.personal_id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's \
        ({', '.join(self.rented_dvds)})"