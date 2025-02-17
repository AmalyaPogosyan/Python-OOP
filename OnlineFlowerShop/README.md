Online Flower Shop Platform
Welcome to the Online Flower Shop Platform! This project simulates an online marketplace where customers can browse and purchase various flower products, and sellers can manage their inventory and orders.

Table of Contents
Features
Installation
Usage
Classes and Methods
Error Handling
Logging
Contributing
License
Features
Customer Functionality: Search for products, add items to the cart, and proceed to checkout.
Seller Functionality: Add or remove products from inventory and review orders.
Product Types: Manage different types of flower products, including bouquets and single flowers.
Validation: Ensure data integrity with attribute validation.
Logging: Track user actions such as adding products and making purchases.
Installation
Clone the Repository:

bash
Պատճենել
Խմբագրել
git clone https://github.com/yourusername/online-flower-shop.git
cd online-flower-shop
Set Up a Virtual Environment:

bash
Պատճենել
Խմբագրել
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies:

bash
Պատճենել
Խմբագրել
pip install -r requirements.txt
Usage
To run the platform, execute:

bash
Պատճենել
Խմբագրել
python main.py
This will start the simulation, allowing you to interact with the platform as a customer or seller.

Classes and Methods
FlowerProduct (Abstract Base Class)
Attributes:

name: Name of the product.
description: Description of the product.
price: Price of the product.
seller: Reference to the seller offering the product.
Methods:

purchase(customer): Abstract method to handle the purchase process.
get_details(): Abstract method to retrieve product details.
Bouquet (Subclass of FlowerProduct)
Additional Attributes:

arrangement_style: Style of the bouquet arrangement.
Methods:

purchase(customer): Deducts the price from the customer's balance and updates inventories.
get_details(): Returns detailed information about the bouquet.
SingleFlower (Subclass of FlowerProduct)
Additional Attributes:

flower_type: Type of the single flower.
Methods:

purchase(customer): Deducts the price from the customer's balance and updates inventories.
get_details(): Returns detailed information about the single flower.
Seller
Attributes:

name: Name of the seller.
email: Contact email of the seller.
inventory: List of products available for sale.
orders: List of orders received.
Methods:

add_product(flower): Adds a product to the inventory.
remove_product(flower): Removes a product from the inventory.
list_products(): Lists all products in the inventory.
review_orders(): Reviews all received orders.
Customer
Attributes:

name: Name of the customer.
email: Contact email of the customer.
cart: List of products added to the cart.
order_history: List of past purchases.
balance: Available balance for purchases.
Methods:

search_products(seller): Searches for products in a seller's inventory.
add_to_cart(flower): Adds a product to the cart.
checkout(flower): Purchases a product from the cart.
view_order_history(): Views past purchases.
Error Handling
The platform includes custom exceptions to handle various error scenarios:

InvalidProductError: Raised when an invalid product is added or removed.
OutOfStockError: Raised when attempting to purchase a product not in inventory.
SearchError: Raised when a search query returns no results.
PaymentError: Raised when there are issues during the payment process.
Logging
User actions such as adding products and making purchases are logged with timestamps. Logs are stored in log.txt in the project root directory.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Note: This project is a simulation and is intended for educational purposes only.


