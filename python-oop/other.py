from product import Product


class Other(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
