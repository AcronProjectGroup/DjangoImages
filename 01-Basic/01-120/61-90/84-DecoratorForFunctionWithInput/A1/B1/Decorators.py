
def x(InputFunction):
    def Wrapper(*args, **kwargs):
        return InputFunction(*args, **kwargs)
    return Wrapper
