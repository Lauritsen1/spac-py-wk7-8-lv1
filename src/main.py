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

    try:
        product.stock.remove(11)
        print(product.stock)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
