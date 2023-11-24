def CalcIncome(income):
    
    assert income >=0, 'Income should be positive'
    
    return income * 2


UsrInput = int(input("Income? "))


try:
    print(CalcIncome(UsrInput))
except Exception as Text:
    print("Exception", Text)

# Output:
    # Income? -100 
    # Exception Income should be positive
