from domain.entities import Category

from .repository import Repository


class CategoryRepository(Repository[Category]):
    def __init__(self):
        self.categories: dict[str, Category] = {}

    def find(self, id: str) -> Category:
        return self.categories[id]

    def find_many(self) -> list[Category]:
        return list(self.categories.values())

    def add(self, category: Category) -> Category:
        self.categories[category.id] = category
        return self.categories[category.id]

    def update(self, category: Category) -> None:
        NotImplementedError('Method not implemented')

    def delete(self, id: str) -> Category:
        return self.categories.pop(id)
