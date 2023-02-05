import csv 
from product import Product

class Phone(Product):

    def __init__(self, name, price, quantity, broken=0):
        super().__init__(name, price, quantity)

        self.broken = broken


