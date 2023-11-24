a = 2

def Function(number):
    global a
    a = a + number
    print(a)

print(a)
Function(100)
print(a)

# Output:
    # 2
    # 102
    # 102
