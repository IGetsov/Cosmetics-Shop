from models.product import Product


class ShoppingCart:
    def __init__(self):
        self._products: list[Product] = []
        self._total_price = 0

    @property
    def products(self):
        return tuple([item for item in self._products])

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)
        
    def contains_product(self, product: Product):
        if product in self._products:
            return True
        return False

    def total_price(self):
        result = 0
        for prod in self._products:
            result += prod.price
        
        self._total_price = result
        return self._total_price
