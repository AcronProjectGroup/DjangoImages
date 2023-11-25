def CalcIncome(income):
    if income < 0:
        print("Invalid")
        return

    return income * 2

UsrInput = int(input("Income? "))

print(CalcIncome(UsrInput))


