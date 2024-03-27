import uuid

from domain.entities import Category
from infrastructure.repositories import CategoryRepository


class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()

    def find(self, id: str) -> Category:
        return self.category_repository.find(id)

    def find_many(self) -> list[Category]:
        return self.category_repository.find_many()

    def create(self, name: str, description: str) -> Category:
        id = str(uuid.uuid4())
        category = Category(id, name, description)
        return self.category_repository.add(category)

    def delete(self, id: str) -> Category:
        return self.category_repository.delete(id)
