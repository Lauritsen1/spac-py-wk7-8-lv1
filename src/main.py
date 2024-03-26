from infrastructure.repositories import CategoryRepository
from domain.entities import Category


def main():
    category_repository = CategoryRepository()
    try:
        category1 = Category('1', 'Shoes', 'Footwear for all occasions.')
        category2 = Category('2', 'Phones', 'Mobile phones.')
        category_repository.add(category1)
        category_repository.add(category2)
        print(category_repository.delete('1'))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
