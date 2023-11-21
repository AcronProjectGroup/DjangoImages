class NegetiveIncomeError(Exception):
    def __init__(self, message, Income):
        self.message = message
        self.income = Income
    

def CheckIncome(Income):
    if Income < 0:
        raise NegetiveIncomeError(f"{Income} is negetive. Income should be positive whore!", Income)
    return Income

UserInput = int(input("Income? "))

try:
    CheckIncome(UserInput)
except NegetiveIncomeError as TextErr:
    print(TextErr.message)
