# Create a class
class Item:
    # Create methods
    # Create a constructor method (Magic Method) for instances
    # Specify the data types
    def __init__(self, name: str, price: float, quantity):

        # Run validations to the received arguments
        ''' Using assert keyword lets you test if a condition in your code returns True, 
        if not, the program will raise an AssertionError.'''
        assert price >=0, f"{price} is not greater than or equal to zero!"
        assert quantity >=0, f"{quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    # Method to perform calculations
    def calculate_total_price(self):
        return self.price * self.quantity

# Create an object and assign values for each attribute
item1 = Item("Milk", 15.00, 5)
item2 = Item("Bread", 18.00, 2)

# Display total price
print(item1.calculate_total_price())
print(item2.calculate_total_price())

