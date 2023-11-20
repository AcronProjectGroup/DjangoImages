class Car:
    def __init__(self, color, model): # This is constructor 
        self.color = color # This is an "instance attribute"
        self.model = model

car1 = Car("Blue", "Mercedes G class") # Create a instance object
print(car1.color)
print(car1.model)


car2 = Car("Red", "Unimog U 5000")
print(car2.color)
print(car2.model)

# Output:
    # Blue
    # Mercedes G class
    # Red
    # Unimog U 5000
