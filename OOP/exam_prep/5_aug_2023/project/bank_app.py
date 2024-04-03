from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan,
    }

    CLIENT_TYPE = {
        "Student": Student,
        "Adult": Adult,
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")
        loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPE:
            raise Exception("Invalid client type!")
        if self.capacity == len(self.clients):
            return "Not enough bank capacity."
        client = self.CLIENT_TYPE[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        loan = next((l for l in self.loans if l.__class__.__name__ == loan_type), None)

        if ((client.__class__.__name__ == "Student" and loan_type != "StudentLoan")
                or (client.__class__.__name__ == "Adult" and loan_type != "MortgageLoan")):
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if client is None:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_loans += 1

        return f"Successfully changed {number_of_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                counter += 1
        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        client = next((c for c in self.clients if c.loans), None)
        client_income = sum((c.income for c in self.clients))
        granted_loans = sum(len(c.loans) for c in self.clients)
        granted_amount = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        average_interest = sum((c.interest for c in self.clients)) / len(self.clients) if len(self.clients) > 0 else 0
        return (f"Active Clients: {len(self.clients)}\n"
                f"Total Income: {client_income:.2f}\n"
                f"Granted Loans: {granted_loans}, Total Sum: {granted_amount:.2f}\n"
                f"Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}\n"
                f"Average Client Interest Rate: {average_interest:.2f}")
