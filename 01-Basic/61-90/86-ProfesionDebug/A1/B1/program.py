class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        NewX = self.x + other.x
        NewY = self.y + other.y
        return Dot(NewX, NewY)
    def __str__(self):
        return f"({self.x}, {self.y})"

def Sum2Nums(a, b):
    result = a + b
    return result

p, q = 4, -1

a = Dot(Sum2Nums(p, q), 2)
b = Dot(10, 3)

