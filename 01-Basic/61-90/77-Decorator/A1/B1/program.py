def SinPrint():
    print("Sina Print")

def SinaRunFunction(a):
    a()

SinaRunFunction(SinPrint)
# Output:
    # Sina Print


def Run2Funcs(aFunc, arg1, arg2):
    return aFunc(arg1, arg2)

def Add2Numbers(a, b):
    return a + b

print(Run2Funcs(Add2Numbers, 2, 4))
# Output:
    # 6

