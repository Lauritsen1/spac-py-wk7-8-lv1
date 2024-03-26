from domain.entities import Category

from .repository import Repository


class CategoryRepository(Repository[Category]):
    def __init__(self):
        self.categories: dict[str, Category] = {}

    def get(self, id: str) -> Category:
        if id not in self.categories:
            raise ValueError(f'No category with ID "{id}"')
        return self.categories[id]

    def get_all(self) -> list[Category]:
        if not self.categories:
            raise ValueError('No categories available.')
        return list(self.categories.values())

    def add(self, category: Category) -> Category:
        if any(
            category.name.lower() == existing.name.lower()
            for existing in self.categories.values()
        ):
            raise ValueError(f'Category with name "{category.name}" already exists.')
        self.categories[category.id] = category
        return category

    def update(self, category: Category) -> None:
        NotImplementedError('Method not implemented')

    def delete(self, id: str) -> Category:
        if id not in self.categories:
            raise ValueError(f'No category with ID "{id}"')
        return self.categories.pop(id)
