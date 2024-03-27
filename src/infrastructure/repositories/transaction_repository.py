from domain.aggregates import Transaction

from .repository import Repository


class TransactionRepository(Repository[Transaction]):
    def __init__(self):
        self.transactions: dict[str, Transaction] = {}

    def find(self, id: str) -> Transaction:
        return self.transactions[id]

    def find_many(self) -> list[Transaction]:
        return list(self.transactions.values())

    def add(self, transaction: Transaction) -> Transaction:
        self.transactions[transaction.id] = transaction
        return self.transactions[transaction.id]

    def update(self, transaction: Transaction) -> None:
        NotImplementedError('Method not implemented')

    def delete(self, id: str) -> Transaction:
        return self.transactions.pop(id)
