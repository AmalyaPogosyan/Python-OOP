from abc import ABC, abstractmethod
from typing import List

# --------------------- Base Classes ---------------------
class Car:
    def __init__(self, make: str, model: str, price: float):
        if not isinstance(make, str) or not isinstance(model, str):
            raise TypeError("Make and model must be strings.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        
        self.make = make
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.make} {self.model} - ${self.price}"

# Specialized Cars
class ElectricCar(Car):
    def __init__(self, make, model, price, battery_capacity, charging_time):
        super().__init__(make, model, price)
        if battery_capacity <= 0 or charging_time <= 0:
            raise ValueError("Battery capacity and charging time must be positive numbers.")
        self.battery_capacity = battery_capacity
        self.charging_time = charging_time

class HybridCar(Car):
    def __init__(self, make, model, price, fuel_efficiency, electric_range):
        super().__init__(make, model, price)
        if fuel_efficiency <= 0 or electric_range <= 0:
            raise ValueError("Fuel efficiency and electric range must be positive numbers.")
        self.fuel_efficiency = fuel_efficiency
        self.electric_range = electric_range

# --------------------- Inventory Management ---------------------
class Inventory:
    def __init__(self):
        self.cars = []
    
    def add_car(self, car: Car):
        if not isinstance(car, Car):
            raise TypeError("Only Car objects can be added to inventory.")
        if car in self.cars:
            print(f"{car} is already in inventory.")
        else:
            self.cars.append(car)
            print(f"{car} added to inventory.")

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"{car} removed from inventory.")
        else:
            print("Car not found in inventory.")
    
    def search(self, **filters):
        results = self.cars
        for key, value in filters.items():
            results = [car for car in results if getattr(car, key, None) == value]
        return results

    def display_inventory(self):
        if not self.cars:
            print("Inventory is empty.")
        else:
            for car in self.cars:
                print(car)

# --------------------- Person Interface ---------------------
class Person:
    def __init__(self, name: str, contact_info: str):
        if not isinstance(name, str) or not isinstance(contact_info, str):
            raise TypeError("Name and contact info must be strings.")
        self.name = name
        self.contact_info = contact_info

# --------------------- Customer Class ---------------------
class Customer(Person):
    def __init__(self, name, contact_info):
        super().__init__(name, contact_info)
        self.purchased_cars = []
    
    def buy_car(self, inventory: Inventory, car: Car, salesperson):
        if car in inventory.cars:
            salesperson.initiate_sale(self, car)
            self.purchased_cars.append(car)
            inventory.remove_car(car)
            print(f"{self.name} purchased {car}.")
        else:
            print("Car is not available.")

# --------------------- Sales Operations Interface ---------------------
class SalesOperations(ABC):
    @abstractmethod
    def initiate_sale(self, customer: Customer, car: Car):
        pass
    
    @abstractmethod
    def generate_receipt(self, customer: Customer, car: Car):
        pass
    
    @abstractmethod
    def display_sales_history(self):
        pass

# --------------------- Salesperson Class ---------------------
class Salesperson(Person, SalesOperations):
    def __init__(self, name, contact_info, commission_rate: float):
        super().__init__(name, contact_info)
        if not (0 < commission_rate <= 1):
            raise ValueError("Commission rate must be between 0 and 1.")
        self.commission_rate = commission_rate
        self.sales_history = []
    
    def initiate_sale(self, customer: Customer, car: Car):
        self.sales_history.append((customer, car))
        print(f"Sale completed: {customer.name} bought {car}.")
    
    def generate_receipt(self, customer: Customer, car: Car):
        return f"Receipt:\nCustomer: {customer.name}\nCar: {car}\nPrice: ${car.price}\nSalesperson: {self.name}\nCommission: ${car.price * self.commission_rate}"
    
    def display_sales_history(self):
        if not self.sales_history:
            print("No sales yet.")
        else:
            for customer, car in self.sales_history:
                print(f"{customer.name} bought {car}.")

# --------------------- Testing the System ---------------------
if __name__ == "__main__":
    # Create inventory
    inventory = Inventory()
    
    # Add cars to inventory
    car1 = ElectricCar("Tesla", "Model S", 79999, 100, 2)
    car2 = HybridCar("Toyota", "Prius", 25000, 50, 30)
    car3 = Car("Honda", "Civic", 20000)
    
    inventory.add_car(car1)
    inventory.add_car(car2)
    inventory.add_car(car3)
    
    # Display inventory
    inventory.display_inventory()
    
    # Create salesperson
    salesperson = Salesperson("John Doe", "john@example.com", 0.05)
    
    # Create customer
    customer = Customer("Alice Smith", "alice@example.com")
    
    # Customer buys a car
    customer.buy_car(inventory, car2, salesperson)
    
    # Display updated inventory
    inventory.display_inventory()
    
    # Generate receipt
    print(salesperson.generate_receipt(customer, car2))
    
    # Show sales history
    salesperson.display_sales_history()
