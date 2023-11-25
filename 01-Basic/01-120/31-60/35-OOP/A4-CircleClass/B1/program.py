class Circle:
    PiNumber = 3.14 # Class Attribute
    
    def __init__(self, Radius):
        self.Radius = Radius
    
    def CalcDiameter(self):
        """
        Calculate Diameter:
        Diameter = Radius * Radius
        """
        print(self.Radius * 2)

    def CalcArea(self): 
        """
        Calculate Area Circle:
        Area = Pi * Radius ** 2 
        """
        print(self.PiNumber * (self.Radius ** 2))
    
    def CalcCircumference(self):
        """
        Calculate Circumference Circle
        circumference = 2 * pi * Radius
        """
        print((2 * self.PiNumber) * self.Radius)

circle1 = Circle(10)
circle1.CalcDiameter()
circle1.CalcArea()
circle1.CalcCircumference()


# Output:
    # 20
    # 314.0
    # 62.800000000000004
