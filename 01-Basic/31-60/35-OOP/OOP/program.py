class Car:
    def __init__(self, color, model): # This is constructor 
        self.color = color # This is an "instance attribute"
        self.model = model

car1 = Car("Blue") # Create a instance object
print(car1.color)


car2 = Car("Red")
print(car2.color)

# Output:
    # Blue
    # Red
