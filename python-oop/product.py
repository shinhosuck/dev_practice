import csv

class Product:
    count_products = 0
    products = []

    
    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity

        Product.count_products += 1
        Product.products.append(self)

    # user can't change name attribute
    @property
    def name(self):
        return self.__name
        
    @name.setter 
    def name(self, value):
        self.__name = value
        return self.__name

    @classmethod
    def instantiate_from_csv(cls):
        product_name = cls.__name__.lower()
        with open(f'/home/aiai/Desktop/products/{product_name}s.csv') as f:
            reader = csv.DictReader(f)
            item_list = list(reader)
            for item in item_list:
                Product(
                    name = item.get('name'),
                    price = item.get('price'),
                    quantity= item.get('quantity')
                )
    def __repr__(self):
        items = f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'
        return items

    # def sample_dict(self, name, price, quantity):
    #     dict = {
    #         'name': self.name,
    #         'price': self.price,
    #         'quantity': self.quantity
    #     }
    #     return dict