class Shape: # This is Abstract Class
    def __init__(self, Ttype, name):
        self.Ttype = Ttype
        self.name = name

    def area(self):
        raise NotImplementedError("Should have to define area method")


class Square(Shape):
    def __init__(self, Ttype, name, SideLength):
        super().__init__(Ttype, name)
        self.SideLength = SideLength
    def area(self):
        return(self.SideLength ** 2)


class Circle(Shape):
    def __init__(self, Ttype, name, Radius):
        super().__init__(Ttype,name)
        self.Radius = Radius
    def area(self):
        return(3.14 * (self.Radius ** 2))

square1 = Square("Square", "SquareName", 1313)
# square1.area()
# Output:
    # raise NotImplementedError("Should have to define area method")
    # NotImplementedError: Should have to define area method


def ShowArea(Obj):
    print(Obj.area())

Square2 = Square("Square2", "Square2Name", 10)
Circle1 = Circle("Circle1", "CircleName", 10)
Circle2 = Circle("Circle2", "CircleName", 10)

for i in [Square2, Circle1, Circle2]:
    ShowArea(i)


