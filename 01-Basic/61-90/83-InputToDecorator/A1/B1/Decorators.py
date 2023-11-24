
def OutLayerDecorator(n):
    def SendRepeatTimes(FuncInput):
        def Wrapper():
            for i in range(n):
                FuncInput()
        return Wrapper
    return SendRepeatTimes

