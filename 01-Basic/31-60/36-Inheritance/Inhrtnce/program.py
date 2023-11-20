class Person:
    def __init__(self, FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
    def whoami(self):
        print(f'{self.FirstName.title()} {self.LastName.title()}')



class Student:
    def __init__(self, FirstName, LastName, major, university):
        self.FirstName = FirstName
        self.LastName = LastName
        self.major = major
        self.university = university

    def whoami(self):
        print(f"{self.FirstName} {self.LastName}")

class Teacher:
    def __init__(self, FirstName, LastName, department, level):
        self.FirstName = FirstName
        self.LastName = LastName
        self.department = department
        self.level = level
    def whoami(self):
        print(f"{self.FirstName} {self.LastName}. {self.department}-{self.level}")


Student1 = Student("Sina", "Lalehbakhsh", "Programming", "Berlin")
Student1.whoami()

Teacher1 = Teacher("Mina", "Jaleh", "Art", "Top Level")
