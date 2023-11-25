def check_even(number):
    return number % 2 == 0 #, number

# _ , ResultNumber = check_even(123)


# if ResultNumber:
#     print("number", ResultNumber, "is even.")
# else:
#     print("number", ResultNumber, "is odd.")


def CountEvensInList(ListNumbers):
    count = 0
    for number in ListNumbers:
        if check_even(number) == True:
            count += 1
    return count

listNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Count Even Numbers in list:\n', listNumbers, '\nnumber of Even Numbers:', CountEvensInList(listNumbers))