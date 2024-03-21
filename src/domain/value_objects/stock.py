class Stock:
    def __init__(self, quantity: int):
        self.quantity = quantity

    def increase(self, quantity: int):
        return Stock(self.quantity + quantity)

    def decrease(self, quantity: int):
        if quantity > self.quantity:
            raise ValueError('Cannot decrease stock below zero')
        return Stock(self.quantity - quantity)

    def __str__(self):
        return str(self.quantity)
