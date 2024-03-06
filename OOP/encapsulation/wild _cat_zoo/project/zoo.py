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
            self.workers.append(worker)
            self._worker_capacity -= 1
            return f"{self.name} the {worker} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        if worker_name in self.workers:
            self.workers.remove(worker_name)
            self._worker_capacity += 1
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_wages = sum([worker.salary for worker in self.workers])
        if self._budget >= total_wages:
            self._budget -= total_wages
            return f"You payed your workers. They are happy. Budget left: {self._budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_amount = sum([animal.money_for_care for animal in self.animals])
        if self._budget >= total_care_amount:
            self._budget -= total_care_amount
            return f"You tended all the animals. They are happy. Budget left: {self._budget}"
        else:
            "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self._budget += amount

    def animals_status(self):
        info = f"You have {len(self.animals)} animals\n"\
               f"----- {len([lion for lion in self.animals if lion == 'lion'])} Lions:\n"\
               f"{['\n'.join([el for el in self.animals if el == 'lion'])]}"
        return info

