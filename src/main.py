from domain.entities import Product, Category


def main():
    category = Category('1', 'Category 1', 'Description of Category 1')
    product = Product(
        '1',
        'Adidas Ultraboost',
        1500,
        'Description of product 1',
        category,
        10,
    )
    product.stock.decrease(5)
    print(product.stock)


if __name__ == '__main__':
    main()
