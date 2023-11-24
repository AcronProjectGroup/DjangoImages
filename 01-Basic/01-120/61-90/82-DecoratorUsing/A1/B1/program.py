def DecoratorRepeater(FuncInput):
    def Wrapper():
        for i in range(3):
            FuncInput()
    return Wrapper

@DecoratorRepeater
def Hello():
    print("Hello")

Hello()
# Output:
    # Hello
    # Hello
    # Hello
