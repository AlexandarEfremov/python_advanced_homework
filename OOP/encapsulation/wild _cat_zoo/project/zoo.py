from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity != 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity != 0 and self.__budget <= price:
            return "Not enough budget"
        else:
            return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__worker_capacity != 0:
            self.workers.append(worker)
            self.__worker_capacity -= 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_wages = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_wages:
            self.__budget -= total_wages
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_amount = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_care_amount:
            self.__budget -= total_care_amount
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        info = f"You have {len(self.animals)} animals\n"
        total_lions = [lion for lion in self.animals if lion.__class__.__name__ == "Lion"]
        amount_of_lions = sum(total_lions)
        info += f"----- {amount_of_lions} Lions:"
        for lion in total_lions:
            info += f"{lion}\n"


