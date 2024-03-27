import uuid

from domain.entities import Product, Category
from infrastructure.repositories import ProductRepository


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def find(self, id: str) -> Product:
        return self.product_repository.find(id)

    def find_many(self) -> list[Product]:
        return self.product_repository.find_many()

    def create(
        self, name: str, price: int, description: str, category: Category, quantity: int
    ) -> Product:
        id = str(uuid.uuid4())
        product = Product(id, name, price, description, category, quantity)
        return self.product_repository.add(product)

    def delete(self, id: str) -> Product:
        return self.product_repository.delete(id)
