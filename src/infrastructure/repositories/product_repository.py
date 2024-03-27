from domain.entities import Product

from .repository import Repository


class ProductRepository(Repository[Product]):
    def __init__(self):
        self.products: dict[str, Product] = {}

    def find(self, id: str) -> Product:
        return self.products[id]

    def find_many(self) -> list[Product]:
        return list(self.products.values())

    def add(self, product: Product) -> Product:
        self.products[product.id] = product
        return self.products[product.id]

    def update(self, product: Product) -> None:
        NotImplementedError('Method not implemented')

    def delete(self, id: str) -> Product:
        return self.products.pop(id)
