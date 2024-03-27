from datetime import datetime
from enum import Enum

from ..entities import Product


class TransactionType(Enum):
    RESTOCK = 'restock'
    SALE = 'sale'


class Transaction:
    def __init__(self, id: str, type: TransactionType, product: Product, quantity: int):
        self.id = id
        self.type = type
        self.product = product
        self.quantity = quantity
        self.datetime = datetime.now()

    def total_price(self) -> int:
        return self.product.price * self.quantity

    def datetime_fmt(self) -> str:
        return self.datetime.strftime('%d/%m/%Y')
