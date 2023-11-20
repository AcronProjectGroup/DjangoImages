class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Line: a=({self.a[0]}, {self.a[1]}) b=({self.b[0]}, {self.b[1]})'
    
    def length(self):
        return ((self.b[1] - self.a[1])**1 + (self.b[0] - self.a[0])**2) ** 0.5

    def slope(self):
        return (self.b[1]-self.a[1]) / (self.b[0] - self.a[0])

line1 = Line((1,1),(3,3))
print(line1.length())

# Output:
    # 2.449489742783178

print(line1.slope())
# Output:
    # 1.0

