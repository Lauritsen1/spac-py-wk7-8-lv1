import uuid

from domain.aggregates import Transaction, TransactionType
from domain.entities import Product
from infrastructure.repositories import TransactionRepository


class TransactionService:
    def __init__(self):
        self.transaction_repository = TransactionRepository()

    def find(self, id: str) -> Transaction:
        return self.transaction_repository.find(id)

    def find_many(self) -> list[Transaction]:
        return self.transaction_repository.find_many()

    def restock(self, product: Product, quantity: int) -> Transaction:
        product.stock.add(quantity)
        id = str(uuid.uuid4())
        transaction = Transaction(id, TransactionType.RESTOCK, product, quantity)
        return self.transaction_repository.add(transaction)

    def sell(self, product: Product, quantity: int) -> Transaction:
        product.stock.remove(quantity)
        id = str(uuid.uuid4())
        transaction = Transaction(
            id, TransactionType.SALE, product, product.stock.quantity - quantity
        )
        return self.transaction_repository.add(transaction)
