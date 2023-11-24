try:
    print(2 / 0)
        # Output -> ZeroDivisionError: division by zero
    ListNumbers = [0,1,2]
    print(ListNumbers[100])
        # Output -> IndexError: list index out of range
    import PoisonousModule
        # Output: -> ModuleNotFoundError: No module named 'PoisonousModule'
except:
    print("No error detection is badly !!!")
        # Output -> No error detection is badly !!!

