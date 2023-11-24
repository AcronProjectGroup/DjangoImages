import functools


def x(InputFunction):
    @functools.wraps(InputFunction)
    def Wrapper(*args, **kwargs):
        return InputFunction(*args, **kwargs)
    return Wrapper
