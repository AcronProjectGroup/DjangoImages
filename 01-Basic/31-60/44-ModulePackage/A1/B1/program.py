def function1():
    print("This is Function 1")

def function2():
    print("This is Function 2")

class ClassProgram:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'This is {self.__class__.__name__} Class name.\nThis is {self.name} object.'