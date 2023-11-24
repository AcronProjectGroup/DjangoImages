# Recursive Functions
def AddRecursive(number):
    if number < 4:
        return AddRecursive(number+1)
    return number

print(AddRecursive(1))
# Output:
    # 4



# Recursive Functions
def FactorialRecursive(number):
    if number == 1 :
        return 1
    return number * FactorialRecursive(number-1)
print(FactorialRecursive(5))
# Output:
    # 120



