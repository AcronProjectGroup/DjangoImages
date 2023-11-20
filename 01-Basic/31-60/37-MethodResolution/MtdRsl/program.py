class Person:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
    def whoami(self):
        print(f'{self.FirstName.title()} {self.LastName.title()}')



class Student(Person):
    def __init__(self, FirstName, LastName, major, university):
        super().__init__(FirstName, LastName)
        self.major = major
        self.university = university
    def whoami(self):
        print(f"{self.FirstName} {self.LastName}\nmajor:{self.major}\nUniversity:{self.university}")

class Teacher:
    pass


Student1 = Student("Sina", "Lalehbakhsh", "Programming", "Berlin")


# Result:
    # Is like Scope Resolution on Function before hase explained


# "Method resolution order" is here: 
help(Student)
# Output:
    # Help on class Student in module __main__:
    # class Student(Person)
    #  |  Student(FirstName, LastName, major, university)
    #  |
    #  |  Method resolution order:
    #  |      Student
    #  |      Person
    #  |      builtins.object
    #  |
    #  |  Methods defined here:
    #  |
    #  |  __init__(self, FirstName, LastName, major, university)
    #  |      Initialize self.  See help(type(self)) for accurate signature.
    #  |
    #  |  whoami(self)
    #  |
    #  |  ----------------------------------------------------------------------
    #  |  Data descriptors inherited from Person:
    #  |
    #  |  __dict__
    #  |      dictionary for instance variables (if defined)
    #  |
    #  |  __weakref__
    #  |      list of weak references to the object (if defined)


