class Customer:
    def __init__(self, name):
        #initialize the customer with a name
        #This uses the property decorator to create a getter and setter for the customer name
        self.name = name
    @property
    def customer_name(self):
        return self.name

    #setter for the customer name
    @customer_name.setter
    def customer_name(self, value):
        #validate the customer name and raise an error if it is not valid
        if not isinstance(value, str):
            raise ValueError("Customer name must be a string")
            #check if the length of characters
        if not (1 <= len(value) <= 50):
            raise ValueError("Customer name must be between 1 and 15 characters")
        self.name = value #stores the customer name
    def orders(self):
        #lets bring all the orders together
        from order import Order
        return [order for order in Order.all_orders if order.customer == self] #we want to go through all orders and return those that match the customer instance

    def coffees(self):
        #return a list of coffees that the customer has ordered
        return list(set(order.coffee for order in self.orders())) #used set to avoid duplicate coffees
