from .category import Category
from value_objects import Stock


class Product:
    def __init__(
        self,
        id: str,
        name: str,
        price: int,
        description: str,
        category: Category,
        stock: int,
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.stock = Stock(stock)

    def __str__(self):
        return self.name
