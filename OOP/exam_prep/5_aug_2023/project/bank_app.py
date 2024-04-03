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
        loan = next((l for l in self.loans if c.__class__.__name__ == loan_type), None)

        if ((client.__class__.__name__ == "Student" and loan_type != "StudentLoan")
                or (client.__class__.__name__ == "Adult" and loan_type != "MortgageLoan")):
            raise Exception("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."


