Complex Car Dealership System

Description

The Complex Car Dealership System is a Python-based program that simulates a comprehensive car dealership management system. It allows customers to search for cars based on various criteria, purchase vehicles, and interact with salespersons. Salespersons can manage the inventory, handle transactions, and track sales history.

Features

Car Classes:

Car: Base class with make, model, and price attributes.

ElectricCar: Inherits from Car, adds battery_capacity and charging_time.

HybridCar: Inherits from Car, adds fuel_efficiency and electric_range.

Customer Management:

Customers can search for cars by make, model, or max_price.

Customers can purchase a car through a salesperson.

Inventory Management:

Salespersons can add, remove, and display cars.

Sales Operations (Interface-based design):

initiate_sale(customer, car): Handles the sale process.

generate_receipt(customer, car): Creates a formatted receipt.

display_sales_history(): Shows all previous sales.

Encapsulation & Modularity:

Uses an interface-based approach to ensure extendability.

Supports adding new roles and car types easily.

Installation

Clone this repository:

git clone https://github.com/your-username/car-dealership.git
cd car-dealership

Ensure you have Python 3 installed:

python --version

Install any dependencies (if required):

pip install -r requirements.txt

Usage

Run the program:

python main.py

Follow the interactive prompts to:

Search for cars

Make a purchase

View inventory

Manage sales records

Extending the System

Add new car types by subclassing the Car class (e.g., SportsCar, Truck).

Implement new sales roles by creating classes that inherit from SalesOperations.

Enhance customer interactions with features like financing options or car comparisons.

License

This project is licensed under the MIT License.

Author

Developed by [Amalya Poghosyan].

