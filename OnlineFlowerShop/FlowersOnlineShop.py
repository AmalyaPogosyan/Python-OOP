from abc import ABC, abstractmethod
from datetime import datetime
import re
import functools

# Custom Exceptions
class InvalidProductError(Exception): pass
class OutOfStockError(Exception): pass
class SearchError(Exception): pass
class PaymentError(Exception): pass

# Utility Functions
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

# Descriptor for Attribute Validation
class Validator:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Invalid type for '{self.name}', expected {self.expected_type}.")
        
        if isinstance(value, str) and not value.strip():
            raise ValueError(f"'{self.name}' cannot be an empty string.")
        
        if isinstance(value, (int, float)) and value < 0:
            raise ValueError(f"'{self.name}' must be a positive number.")
        
        if self.name == "email" and not is_valid_email(value):
            raise ValueError("Invalid Email format.")
        
        instance.__dict__[self.name] = value

# Logging Decorator
def log_action(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        with open("log.txt", "a") as log_file:
            log_file.write(f"[{datetime.now()}] '{fn.__name__}' called with {', '.join(repr(arg) for arg in args[1:])}\n")
        return result
    return wrapper

# Abstract Base Class for Flower Products
class FlowerProduct(ABC):
    name = Validator(str)
    price = Validator((int, float))
    description = Validator(str)

    def __init__(self, name, description, price, seller):
        if not isinstance(seller, Seller):
            raise TypeError("Seller must be an instance of Seller class.")
        self.name = name
        self.description = description
        self.price = price
        self.seller = seller

    @abstractmethod
    def purchase(self, customer):
        pass

    @abstractmethod
    def get_details(self):
        pass

    def __repr__(self):
        return f"{self.name} (${self.price})"

# Concrete Classes for Flower Products
class Bouquet(FlowerProduct):
    def __init__(self, name, description, price, seller, arrangement_style):
        super().__init__(name, description, price, seller)
        self.arrangement_style = arrangement_style

    def purchase(self, customer):
        if customer.balance < self.price:
            raise PaymentError("Insufficient balance.")
        customer.balance -= self.price
        self.seller.inventory.remove(self)
        customer.order_history.append(self)

    def get_details(self):
        return f"Bouquet | {self.name} | {self.description} | ${self.price} | Arrangement: {self.arrangement_style} | Seller: {self.seller}"

class SingleFlower(FlowerProduct):
    def __init__(self, name, description, price, seller, flower_type):
        super().__init__(name, description, price, seller)
        self.flower_type = flower_type

    def purchase(self, customer):
        if customer.balance < self.price:
            raise PaymentError("Insufficient balance.")
        customer.balance -= self.price
        self.seller.inventory.remove(self)
        customer.order_history.append(self)

    def get_details(self):
        return f"Single Flower | {self.name} | {self.description} | ${self.price} | Type: {self.flower_type} | Seller: {self.seller}"

# Seller Class
class Seller:
    name = Validator(str)
    email = Validator(str)

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []
        self.inventory = []

    @log_action
    def add_product(self, flower):
        if not isinstance(flower, FlowerProduct):
            raise InvalidProductError("Invalid product.")
        self.inventory.append(flower)

    @log_action
    def remove_product(self, flower):
        if flower not in self.inventory:
            raise OutOfStockError("Product not found in inventory.")
        self.inventory.remove(flower)

    def list_products(self):
        return ", ".join(repr(flower) for flower in self.inventory) if self.inventory else "No products available."

    def review_orders(self):
        return ", ".join(repr(order) for order in self.orders) if self.orders else "No orders yet."

    def __repr__(self):
        return self.name

# Customer Class
class Customer:
    name = Validator(str)
    email = Validator(str)

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []
        self.order_history = []
        self.balance = 0

    def add_funds(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount

    def search_product(self, seller):
        if not isinstance(seller, Seller):
            raise TypeError("Invalid type; must be a Seller.")
        return seller.list_products()

    @log_action
    def add_to_cart(self, flower):
        if not isinstance(flower, FlowerProduct):
            raise InvalidProductError("Invalid product.")
        self.cart.append(flower)

    @log_action
    def checkout(self):
        total_cost = sum(flower.price for flower in self.cart)
        if self.balance < total_cost:
            raise PaymentError("Not enough balance.")
        
        for flower in self.cart:
            flower.purchase(self)
        
        self.cart.clear()

    def view_order_history(self):
        return ", ".join(repr(flower) for flower in self.order_history) if self.order_history else "No past orders."

    def __repr__(self):
        return self.name
