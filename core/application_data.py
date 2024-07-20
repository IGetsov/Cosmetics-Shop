from models.category import Category
from models.product import Product
from models.shopping_cart import ShoppingCart


class ApplicationData:
    def __init__(self):
        self._products: tuple(Product) = ()
        self._categories: tuple(Category) = ()
        self._shopping_cart: ShoppingCart = ShoppingCart()

    @property
    def products(self):
        return self._products

    @property
    def categories(self):
        return self._categories

    @property
    def shopping_cart(self) -> ShoppingCart:
        return self._shopping_cart

    def find_product_by_name(self, name: str) -> Product:
        for prod in self._products:
            if prod.name == name:
                return prod
        else:
            raise ValueError("No such product exists!")

    def find_category_by_name(self, name) -> Category:
        for prod in self._categories:
            if prod.name == name:
                return prod
        else:
            raise ValueError("No such category exists!")

    def create_category(self, name) -> None:
        category = Category(name=name)
        if category not in self._categories:
            self._categories = self._categories + (category,)

    def create_product(self, name, brand, price, gender) -> None:
        product = Product(name=name, brand=brand, price=price, gender=gender)
        if product not in self._products:
            self._products = self._products + (product,)

    def category_exists(self, name) -> bool:
        for category in self._categories:
            if category.name == name:
                return True
        return False

    def product_exists(self, name) -> bool:
        for product in self._products:
            if product.name == name:
                return True
        return False


#####
#prod1 = Product("Shampoo", "Nivea", 10.99, Gender.WOMEN)
#prod2 = Product("Cream", "Nivea", 8.99, Gender.WOMEN)
#prod3 = Product("Deodorant", "FA", 11.00, Gender.UNISEX)

# cat1 = Category("Nivea")
# cat2 = Category("FA")

# shpgcrt = ShoppingCart()
# print('Adding products in categories')
# cat1.add_product(prod1)
# cat1.add_product(prod2)
# cat2.add_product(prod3)

# print('Adding products to cart_______')
# shpgcrt.add_product(prod1)
# shpgcrt.add_product(prod2)
# shpgcrt.add_product(prod3)
# print('Check for product_______')
# print(shpgcrt.contains_product(prod2))
# print(shpgcrt.contains_product(prod3))
# print('Check for total price_______')
# print(shpgcrt.total_price())
# print('Removing of product_______')
# shpgcrt.remove_product(prod2)
# print('Check for total price after prod2 is removed_______')
# print(shpgcrt.total_price())

