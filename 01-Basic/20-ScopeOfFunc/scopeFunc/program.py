a = 123

def PrintA():
    a = 3
    print(a)

# print(a)
# PrintA()
# print(a)

# Output
    # 123
    # 3
    # 123

def PrintAResolution():
    def Print():
        print('a')
    
    Print()

PrintAResolution()
# Output:
    # a