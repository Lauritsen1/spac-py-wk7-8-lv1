from domain.entities import Product, Category
from infrastructure.repositories import ProductRepository, CategoryRepository

import uuid


def main():
    category_repository = CategoryRepository()
    product_repository = ProductRepository()

    category_id = str(uuid.uuid4())
    category_name = 'Shoes'
    category_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

    category = Category(category_id, category_name, category_description)
    category_repository.add(category)

    product_id = str(uuid.uuid4())
    product_name = 'Adidas Ultraboost'
    product_price = 1500
    product_description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    product_category = category
    product_initial_stock = 10

    product = Product(
        product_id,
        product_name,
        product_price,
        product_description,
        product_category,
        product_initial_stock,
    )
    product_repository.add(product)
    print(category_repository.get(category).id)


if __name__ == '__main__':
    main()
