class Person:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
    def whoami(self):
        print(f'{self.FirstName.title()} {self.LastName.title()}')



class Student(Person):
    pass

class Teacher:
    pass


Student1 = Student("Sina", "Lalehbakhsh")
Student1.whoami()

# Output:
    # Sina Lalehbakhsh
