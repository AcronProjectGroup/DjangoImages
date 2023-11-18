
ListNumbers = [1,2,3,4,5]

def power(number):
    return number**2

for number in ListNumbers:
    print(power(number))
    # map:
    # print(map(power, ListNumbers))
    # Output:
        # 1
        # <map object at 0x7f130e0c2e30>
        # 4
        # <map object at 0x7f130e0c2e60>
        # 9
        # <map object at 0x7f130e0c2e90>
        # 16
        # <map object at 0x7f130e0c2ec0>
        # 25
        # <map object at 0x7f130e0c2ef0>

# map:
for item in map(power, ListNumbers):
    print(item)
# Output:
    # 1
    # 4
    # 9
    # 16
    # 25
    # 1
    # 4
    # 9
    # 16
    # 25


print(list(map(power, ListNumbers)))
# Output:
    # [1, 4, 9, 16, 25]


    