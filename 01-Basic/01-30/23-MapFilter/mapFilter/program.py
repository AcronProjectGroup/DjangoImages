ListNumbers = [1, 2, 3, 4, 5]


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


def PlusOne(number):
    return number + 1


# Map
print(list(map(PlusOne, ListNumbers)))
# Output:
# [2, 3, 4, 5, 6]


ListFullNames = [
    "SINA LALE",
    "Moriz Deutsch",
    "Frau Merkel",
    "MINA Jale",
    "REZA",
    "Meza",
    "Seza!",
]


def NameExtraction(FullName):
    return FullName.split()[0]


print(NameExtraction(ListFullNames[0]))

# Map
print(list(map(NameExtraction, ListFullNames)))
# Output:
# ['SINA', 'Moriz', 'Frau']


ListScores = [10, 3, 6, 9, 7, 12, 15, 20, 14, 15, 19, 18, 9, 2, 3, 11]


def MoreThan15(Score):
    if Score >= 15:
        return True
    else:
        return False


# Filter
print(list(filter(MoreThan15, ListScores)))
# Output:
# [15, 20, 15, 19, 18]


def GetFullNames(ListFullNames):
    return len(ListFullNames.split()) >= 2
    # for i in ListFullNames:
    #     print(i.split())
    #     print(len(i.split())>=2)
    # return len(i.split()) >= 2

# Filter
print(list(filter(GetFullNames, ListFullNames)))


def GetLenghtMoreThan5Char(ListFullNames):
    return len(ListFullNames) >= 5

# Filter
print(list(filter(GetLenghtMoreThan5Char, ListFullNames)))


