from abc import ABC, abstractmethod
import csv

from core.transaction import Transaction


class TransactionFactory(ABC):
    @staticmethod
    def create_transaction(data: dict) -> Transaction:
        return Transaction(
            name=data['name'],
            amount=float(data['amount']),
            day=int(data['day']) if data['day'] else None,
            currency=data['currency'] if data['currency'] else 'GBP'
        )


class CSVTransactionFactory(TransactionFactory):
    def load_transactions_from_csv(self, file_path: str) -> list[Transaction]:
        """Loads transactions from a CSV file."""
        transactions = list()
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(self.create_transaction(row))
        return transactions
