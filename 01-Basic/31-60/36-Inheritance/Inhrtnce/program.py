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
Student1.whoami()
 
# Output:
    # Sina Lalehbakhsh
    # major:Programming
    # University:Berlin
