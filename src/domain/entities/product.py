from .category import Category


class Stock:
    def __init__(self, quantity: int):
        self.quantity = quantity

    def add(self, quantity: int):
        self.quantity += quantity

    def remove(self, quantity: int):
        if quantity > self.quantity:
            raise ValueError(
                f'Failed to remove {quantity}. Only {self.quantity} in stock.'
            )
        self.quantity -= quantity

    def __str__(self):
        return str(self.quantity)


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
