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

Greeting()
print(Add2Nums(1,2))
print(MultiThreeNums(1,2,1))

# Output:
    # Hello cowboy!
    # 3
    # 2

