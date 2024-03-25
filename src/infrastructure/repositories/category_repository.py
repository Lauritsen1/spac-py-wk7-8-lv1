from domain.entities import Category

from .repository import Repository


class CategoryRepository(Repository):
    def __init__(self):
        self.categories: dict[str, Category] = {}

    def get(self, category: Category) -> Category:
        if category.id not in self.categories:
            raise ValueError(
                f'Failed to retrieve category: No category with ID {category.id} found.'
            )
        return self.categories[category.id]

    def get_all(self) -> list[Category]:
        if not self.categories:
            raise ValueError(
                'Failed to retrieve categories: No categories are currently available.'
            )
        return list(self.categories.values())

    def add(self, category: Category) -> None:
        if category.id in self.categories:
            raise ValueError(
                f'Failed to add category: A category with ID {category.id} already exists.'
            )
        self.categories[category.id] = category

    def update(self, category: Category) -> None:
        if category.id not in self.categories:
            raise ValueError(
                f'Failed to update category: No category with ID {category.id} found.'
            )
        self.categories[category.id] = category

    def delete(self, category: Category) -> None:
        if category.id not in self.categories:
            raise ValueError(
                f'Failed to delete category: No category with ID {category.id} found.'
            )
        del self.categories[category.id]
