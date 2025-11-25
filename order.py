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
    pass