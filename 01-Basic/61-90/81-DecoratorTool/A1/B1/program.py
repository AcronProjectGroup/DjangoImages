
def Decoretor(FunctionIsInput):
    def developer():
        print("developed!")
        FunctionIsInput()
        print("developed!")

    return developer

@Decoretor
def SayHello():
    print("Hello")

SayHello()
# Output:
    # developed!
    # Hello
    # developed!
