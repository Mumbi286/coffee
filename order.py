#lets import the Customer and Coffee classes from the customer and coffee modules
from customer import Customer
from coffee import Coffee
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
    
    #getter for the customer
    @property
    def order_customer(self):
        return self._customer

    #setter for the customer
    @order_customer.setter
    def order_customer(self, value):
        #we check if the value is an instance of Customer
        if not isinstance(value, Customer):
            raise ValueError("Order customer must be a Customer instance")
        self._customer = value #stores the private customer instance

    #getter for the coffee
    @property
    def order_coffee(self):
        return self._coffee #returns the private coffee instance

    #setter for the coffee
    @order_coffee.setter
    def order_coffee(self, value):
        #we check if the value is an instance of Coffee
        if not isinstance(value, Coffee):
            raise ValueError("Order coffee must be a Coffee instance")
        self._coffee = value #stores the private coffee instance

    @property
    def order_price(self):
        return self._price 
    @order_price.setter
    def order_price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Order price must be a number")
        # we check if the value is between 0 and 100
        if not (0 <= value <= 100):
            raise ValueError("Order price must be between 0 and 100")
        self._price = value  # stores the private price value

    pass