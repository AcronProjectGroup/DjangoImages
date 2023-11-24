def SayHello():
    print("Hello")

def Decoretor(FunctionIsInput):
    def developer():
        print("developed!")
        FunctionIsInput()
        print("developed!")

    return developer

a = Decoretor(SayHello)

a()
# Output:
    # developed!
    # Hello
    # developed!

