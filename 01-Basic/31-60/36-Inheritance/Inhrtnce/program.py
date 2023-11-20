class Person:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
    def whoami(self):
        print(f'{self.FirstName.title()} {self.LastName.title()}')



class Student(Person):
    def __init__(self, FirstName, LastName, major):
        super().__init__(FirstName, LastName)
        self.major = major
    def whoami(self):
        print(f"{self.FirstName} {self.LastName} {self.major}")

class Teacher:
    pass


Student1 = Student("Sina", "Lalehbakhsh", "Programming")
Student1.whoami()
 
# Output:
    # Sina Lalehbakhsh Programming
