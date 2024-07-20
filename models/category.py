from models.product import Product
from models.helper_functions import char_len_check, remove_last_line_from_str
from models.gender import Gender


class Category:
    def __init__(self, name):
        if not char_len_check(2, 15, name):
            raise ValueError("Category name must be between 2 and 15 characters!")
        self._name = name
        self._products: tuple(Product) = ()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not char_len_check(2, 15, value):
            raise ValueError("Category name must be between 2 and 15 characters!")
        self._name = value

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product: Product):
        if product not in self._products:
            self._products = self._products + (product,)
            return f'Product {product.name} added to category {self.name}!'
        else:
            raise ValueError(f'Product {product.name} is already in category {self.name}!')


    def remove_product(self, product: Product) -> str:
        if product not in self._products:
            raise ValueError(f"Product {product.name} does not exist in this category!")
        else:
            items = list(self._products)
            items.remove(product)
            self._products = tuple(items)
            return f'Product {product.name} removed from category {self.name}!'
        
    def to_string(self) -> str:
        result = [f'#Category: {self.name}']
        # if products exist
        if len(self._products) > 0:
            for prod in self._products:
                result.append(f' {prod.to_string()}')
                result.append('===')
        # remove last ===
            result = result[:-1]
        # if no products exist
        elif len(self._products) < 1:
            result.append(' #No products in this category')
        
        return ['\n'.join(item) for item in result]

