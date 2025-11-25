class Coffee:
    all_orders = []  # Class variable to store all coffee orders
    def __init__(self, name):
        # Initialize the coffee with a name
        self.name = name

     #getter for the coffee name   
    @property
    def coffee_name(self):
        return self.name

    @coffee_name.setter
    def coffee_name(self, value):
        #We are checking if the value is a string
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string")
            # we check the length of characters
        if len(value) < 3:
            raise ValueError("Coffee name must be between 1 and 50 characters")
        self.name = value #stores the coffee name

    def add_order(self):
        #lets bring all the orders together
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self] #we want to go through all orders and return those that match the coffee instance
    pass