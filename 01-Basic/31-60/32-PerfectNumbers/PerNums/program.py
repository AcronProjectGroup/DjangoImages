def DividersBy(number):
    DividerNumbers = 1
    listDividers = []
    PerfectNumber = False

    for i in range(1, number):
        if number % i == 0:
            DividerNumbers += 1
            listDividers.append(i)
    if sum(listDividers) == number:
        PerfectNumber = True

    listDividers.append(number)
    return number, DividerNumbers, listDividers, PerfectNumber


number, numbers, LIst, perfectnumber = DividersBy(28)
print("Number =", number)
print("Numbers =", numbers)
print("List dividers =", LIst)
print("Perfect number =", perfectnumber)
