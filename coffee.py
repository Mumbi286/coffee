class Coffee:
    def __init__(self, name):
        self.name = name
    @property
    def coffee_name(self):
        return self.name

    @coffee_name.setter
    def coffee_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Coffee name must be a string")
        if len(value) < 3:
            raise ValueError("Coffee name must be between 1 and 50 characters")
        self.name = value
    pass