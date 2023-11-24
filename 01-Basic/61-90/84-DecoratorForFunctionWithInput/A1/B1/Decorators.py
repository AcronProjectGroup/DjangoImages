
def x(InputFunction):
    def Wrapper():
        InputFunction()
    return Wrapper
