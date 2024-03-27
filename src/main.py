import os
from typing import Any

from application.services import CategoryService, ProductService, TransactionService
from tabulate import tabulate


def main():
    category_service = CategoryService()
    product_service = ProductService()
    transaction_service = TransactionService()

    electronics = category_service.create('Electronics', 'Electronic products')
    clothing = category_service.create('Clothing', 'Clothing products')
    books = category_service.create('Books', 'Books and literature')

    laptop = product_service.create('Laptop', 1000, 'A laptop', electronics, 10)
    tshirt = product_service.create('T-Shirt', 20, 'A t-shirt', clothing, 50)
    novel = product_service.create('Novel', 15, 'A novel', books, 100)

    transaction_service.restock(laptop, 5)
    transaction_service.restock(tshirt, 10)
    transaction_service.restock(novel, 20)

    while True:
        menu_options = ['Products', 'Categories', 'Transactions', 'Exit']
        choice = get_user_choice(menu_options)

        if choice == 1:

            menu_options = ['Create', 'List', 'Exit']
            choice = get_user_choice(menu_options)

            if choice == 1:
                name = input('name: ')
                price = int(input('price: '))
                description = input('description: ')
                categories = category_service.find_many()
                category_choice = get_user_choice(categories)
                category = categories[category_choice - 1]
                stock = int(input('stock: '))
                product_service.create(name, price, description, category, stock)

            elif choice == 2:
                products = product_service.find_many()

                table_data = [
                    {
                        'Choice': index + 1,
                        'Name': product.name,
                        'Price': product.price,
                        'Description': product.description,
                        'Category': product.category.name,
                        'Stock': product.stock,
                    }
                    for index, product in enumerate(products)
                ]

                print(
                    tabulate(
                        table_data,
                        headers='keys',
                        tablefmt='simple_grid',
                    )
                )

                print(f'\n{len(products) + 1}. Exit')

                product_choice = int(input('\nEnter your choice: '))

                if product_choice == len(products) + 1:
                    os.system('cls')
                    continue

                chosen_product = products[product_choice - 1]

                product_table = [
                    {
                        'Name': chosen_product.name,
                        'Price': chosen_product.price,
                        'Description': chosen_product.description,
                        'Category': chosen_product.category.name,
                        'Stock': chosen_product.stock,
                    }
                ]

                print(
                    tabulate(
                        product_table,
                        headers='keys',
                        tablefmt='simple_grid',
                    ),
                    '\n',
                )

                menu_options = ['Restock', 'Delete', 'Exit']
                choice = get_user_choice(menu_options)

                if choice == 1:
                    stock = int(input('Quantity: '))
                    transaction_service.restock(chosen_product, stock)
                    product_service.find_many()
                elif choice == 2:
                    product_service.delete(chosen_product.id)
                elif choice == 3:
                    break

        elif choice == 2:
            menu_options = ['Create', 'List', 'Exit']
            choice = get_user_choice(menu_options)

            if choice == 1:
                name = input('name: ')
                description = input('description: ')
                category_service.create(name, description)

            elif choice == 2:
                categories = category_service.find_many()

                table_data = [
                    {
                        'Choice': index + 1,
                        'Name': category.name,
                        'Description': category.description,
                    }
                    for index, category in enumerate(categories)
                ]

                print(
                    tabulate(
                        table_data,
                        headers='keys',
                        tablefmt='simple_grid',
                    )
                )

                print(f'\n{len(categories) + 1}. Exit')

                category_choice = int(input('\nEnter your choice: '))

                if category_choice == len(categories) + 1:
                    os.system('cls')
                    continue

                chosen_category = categories[category_choice - 1]

                category_table = [
                    {
                        'Name': chosen_category.name,
                        'Description': chosen_category.description,
                    }
                ]

                print(
                    tabulate(
                        category_table,
                        headers='keys',
                        tablefmt='simple_grid',
                    ),
                    '\n',
                )

                menu_options = ['Delete', 'Exit']
                choice = get_user_choice(menu_options)

                if choice == 1:
                    category_service.delete(chosen_category.id)
                elif choice == 2:
                    break

        elif choice == 3:
            transactions = transaction_service.find_many()

            table_data = [
                {
                    'Type': transaction.type.value,
                    'Product': transaction.product.name,
                    'Quantity': transaction.quantity,
                    'Unit Price': transaction.product.price,
                    'Total Price': transaction.total_price(),
                    'Date': transaction.datetime_fmt(),
                }
                for transaction in transactions
            ]

            print(
                tabulate(
                    table_data,
                    headers='keys',
                    tablefmt='simple_grid',
                )
            )

            menu_options = ['Exit']
            product_choice = get_user_choice(menu_options)

        elif choice == 4:
            break


def get_user_choice(menu_options: list[Any]) -> int:
    while True:
        for i, option in enumerate(menu_options, 1):
            print(f'{i}. {option}')
        choice = input('\nEnter your choice: ')
        os.system('cls')
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice)
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
