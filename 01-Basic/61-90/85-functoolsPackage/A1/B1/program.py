from Decorators import x


@x
def Greeting():
    print("Hello cowboy!")

@x
def Add2Nums(a,b):
    return a + b
@x
def MultiThreeNums(x, y, z):
    return x * y * z

print(Greeting)
# Output:
    # <function Greeting at 0x7f3483d4ea70>
