def SayHello():
    print("Hello")

def Developer():
    SayHello()
    print("Sina")

Developer()
# Output:
    # Hello
    # Sina

def devAllFuncs(FunctionInput):
    FunctionInput()
    print("All Functions Developed")

devAllFuncs(SayHello)
# Output:
    # Hello
    # All Functions Developed

