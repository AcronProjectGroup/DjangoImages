class Square:
    def __init__(self, SideLength): # This is Magic Method
        self.SideLength = SideLength
    
    def __str__(self):# This is Magic Method
        return f"This is Square shape with Side Length {self.SideLength}"

    

square = Square(10)
print(square)


# Before definition __str__ 
# Output
    # <__main__.Square object at 0x7f8d02cc2c90>



print(square)
# After definition __str__ 
# Output
    # This is Square shape with Side Length 10
