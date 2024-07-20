from models.helper_functions import char_len_check
from models.gender import Gender


class Product:
    def __init__(self, name: str, brand: str, price: float, gender: Gender):
        if not char_len_check(3, 10, name):
            raise ValueError("Product name has to be between 3 and 10 characters long!")
        if not char_len_check(2, 10, brand):
            raise ValueError("Brand has to be between 2 and 10 characters long!")
        if price < 0:
            raise ValueError("Price cannot be negative value!")
        self._name = name
        self._brand = brand
        self._price = price
        self._gender: Gender = gender

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not char_len_check(3, 10, value):
            raise ValueError("Product name has to be between 3 and 10 characters long!")
        self._name = value
            
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not char_len_check(2, 10, value):
            raise ValueError("Brand has to be between 2 and 10 characters long!")
        self._brand = value
            
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @property
    def gender(self):
        return self._gender

    def to_string(self):
        str_list = [f' #{self.name} {self.brand}', f'\n #Price: ${self.price:.2f}', f'\n #Gender: {self._gender}']
        result = ''
        for i in range(len(str_list)):
            result += str_list[i]
        return result
    
