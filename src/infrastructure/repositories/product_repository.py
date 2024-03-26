from domain.entities import Product

from .repository import Repository


class ProductRepository(Repository[Product]):
    def __init__(self):
        self.products: dict[str, Product] = {}

    def get(self, id: str) -> Product:
        if id not in self.products:
            raise ValueError(f'No product with ID "{id}"')
        return self.products[id]

    def get_all(self) -> list[Product]:
        if not self.products:
            raise ValueError('No products available.')
        return list(self.products.values())

    def add(self, product: Product) -> Product:
        if any(
            product.name.lower() == existing.name.lower()
            for existing in self.products.values()
        ):
            raise ValueError(f'Product with name "{product.name}" already exists')
        self.products[product.id] = product
        return product

    def update(self, product: Product) -> None:
        NotImplementedError('Method not implemented')

    def delete(self, id: str) -> Product:
        if id not in self.products:
            raise ValueError(f'No product with ID "{id}"')
        return self.products.pop(id)
