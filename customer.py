class Customer:
    def __init__(self, name):
        self.name = name
    @property
    def customer_name(self):
        return self.name

    @customer_name.setter
    def customer_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Customer name must be a string")
        if not (1 <= len(value) <= 50):
            raise ValueError("Customer name must be between 1 and 15 characters")
        self.name = value

    pass