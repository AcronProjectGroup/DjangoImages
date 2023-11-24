def aFunc():
    def SinaPrint(name):
        return f"Print {name}"
    
    return SinaPrint("Jinna")

print(aFunc())
# Output:
    # Print Jinna


def anothFunc():
    def Add2Nums(a, b):
        return a + b
    
    return Add2Nums

GetReturn = anothFunc()
print(GetReturn(0.01, 3.14))
# Output:
    # 3.15

