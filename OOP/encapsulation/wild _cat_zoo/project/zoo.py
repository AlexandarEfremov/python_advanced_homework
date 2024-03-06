class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self._budget = budget
        self._animal_capacity = animal_capacity
        self._worker_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self._budget >= price and self._animal_capacity != 0:
            self.animals.append(animal)
            self._budget -= price
            self._animal_capacity -= 1
            return f"{self.name} the {animal} added to the zoo"
        elif self._animal_capacity != 0 and self._budget <= price:
            return "Not enough budget"
        else:
            return f"Not enough space for animal"

    def hire_worker(self, worker):
        if self._worker_capacity != 0:
            return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
