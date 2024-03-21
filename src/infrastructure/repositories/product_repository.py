from domain.entities import Product

from .repository import Repository


class ProductRepository(Repository):
    def __init__(self):
        self.products: dict[str, Product] = {}

    def get(self, product: Product) -> Product:
        if product.id not in self.products:
            raise ValueError(
                f'Failed to retrieve product: No product with ID {product.id} found.'
            )
        return self.products[product.id]

    def get_all(self) -> list[Product]:
        if not self.products:
            raise ValueError(
                'Failed to retrieve products: No products are currently available.'
            )
        return list(self.products.values())

    def add(self, product: Product) -> None:
        if product.id in self.products:
            raise ValueError(
                f'Failed to add product: A product with ID {product.id} already exists.'
            )
        self.products[product.id] = product

    def update(self, product: Product) -> None:
        if product.id not in self.products:
            raise ValueError(
                f'Failed to update product: No product with ID {product.id} found.'
            )
        self.products[product.id] = product

    def delete(self, product: Product) -> None:
        if product.id not in self.products:
            raise ValueError(
                f'Failed to delete product: No product with ID {product.id} found.'
            )
        del self.products[product.id]
