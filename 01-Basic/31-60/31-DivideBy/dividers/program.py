def DividersBy(number):
    DividerNumbers = 1
    listDividers = []
    for i in range(1, number):
        if number % i == 0:
            DividerNumbers += 1
            listDividers.append(i)
    listDividers.append(number)
    return number, DividerNumbers, listDividers
    

number, numbers, LIst = DividersBy(8) 
print('Number=', number)
print('Numbers=', numbers)
print('List dividers=', LIst)