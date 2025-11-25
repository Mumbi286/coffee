class Coffee:
    def __init__(self, name):
        # Initialize the coffee with a name
        self.name = name
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
    pass