def CalcIncome(income):
    if income < 0:
        raise Exception("Income shold positive")
    return income * 2


UsrInput = int(input("Income? "))

print(CalcIncome(UsrInput))
# Input:
    # -100
# Output:
    # Exception: Income shold positive



try:
    print(CalcIncome(UsrInput))
except Exception:
    print(Exception)
# Output:
# <class 'Exception'>