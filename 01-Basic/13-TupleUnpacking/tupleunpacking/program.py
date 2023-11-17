marks = [("sina", 30), ("mina", 20), ("jina", 40), ("bina", 15)]

for name, mark in marks:
    print(name, ":", mark)


def Calculator(number1, number2):
    sumNumber = number1 + number2
    SubtractionNumber = number1 - number2
    return (sumNumber, SubtractionNumber)


print(Calculator(10, 4))

# Tuple unpacking:
(a, b) = Calculator(10, 4)
print(a)
print(b)


def CalcMinMax(ListNumbers):
    return min(ListNumbers), max(ListNumbers)


print(CalcMinMax([1, 13, 123, -12, -2, 153, -23]))

# Tuple unpacking
(Min, Max) = CalcMinMax([1, 13, 123, -12, -2, 153, -23])
print("Min=", Min)
print("Max=", Max)


def LongestStringInList(ListStrings):
    finalResult = ""
    for String in ListStrings:
        if len(String) >= len(finalResult):
            finalResult = String
    return finalResult, len(finalResult)


ListStringsss = [
    "Sina",
    "Laleh",
    "Bakhsh",
    "4",
    "5",
    "6",
    "Program",
    "Sina 4 Laleh 5 Bakhsh 6",
    "Sina LalehBakhsh = 4, 5, 6 ",
]

print(LongestStringInList(ListStringsss))

# Tuple unpacking
Name, LengthName = LongestStringInList(ListStringsss)
print('Name =',Name)
print('LengthName =',LengthName)
