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

