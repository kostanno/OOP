from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(self, name, price, description):
        super().__init__()
        self.name = name
        self.price = price
        self.description = description

    @abstractmethod
    def get_full_info(self):
        return f"{self.name}" f"{self.price}" f"{self.description}"

    def __str__(self):
        return f"{self.name} - {self.price} руб."


class MixinLog:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}, {self.name}, {self.description}, {self.price}, {self.quantity}"


class Product(MixinLog, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, product_data):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def get_full_info(self):
        return f"{self.name}" f"{self.price}" f"{self.description}" f"{self.quantity}"


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def get_full_info(self):
        return (
            f"{self.name}"
            f"{self.price}"
            f"{self.description}"
            f"{self.quantity}"
            f"{self.efficiency}"
            f"{self.model}"
            f"{self.memory}"
            f"{self.color}"
        )


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def get_full_info(self):
        return (
            f"{self.name}"
            f"{self.price}"
            f"{self.description}"
            f"{self.quantity}"
            f"{self.germination_period}"
            f"{self.country}"
            f"{self.color}"
        )


class Category:
    name: str
    description: str
    products: list
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count = 0
        Category.product_count += len(products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        for product in self.__products:
            return f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
