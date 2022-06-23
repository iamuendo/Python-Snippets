# Create a class
class Item:
    # This is a method
    def calculate_total_price(self, x, y):
        return x * y

# Create an instance of the class
item1 = Item()
# Create attributes
item1.name = "Milk"
item1.price = 15.00
item1.quantity = 5
print(f"Item 1 total: {item1.calculate_total_price(item1.price, item1.quantity)}")

'''NOTE: You can create more than one instance of a class '''

# Create an instance of the class
item2 = Item()
# Create attributes
item2.name = "Bread"
item2.price = 18.00
item2.quantity = 2
print(f"Item 2 total: {item2.calculate_total_price(item2.price, item2.quantity)}")
