class Car:
    def __init__(self, color, model): # This is constructor 
        self.color = color # This is an "instance attribute"
        self.model = model
    def PrintDetails(self): # This is Method Creation
        """This is Method Creation
        and shows Detail of Object created by Car"""
        print(f'Color: {self.color} Model: {self.model}')

car1 = Car("Blue", "Mercedes G class") # Create a instance object
car1.PrintDetails()

# Output:
    # Color: Blue Model: Mercedes G class
