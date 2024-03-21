from .category import Category


class Product:
    def __init__(
        self,
        id: str,
        name: str,
        price: int,
        description: str,
        category: Category,
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.category = category

    def __str__(self):
        return self.name
