def check_even(number):
    result = False
    if number % 2 == 0:
        result = True

    return result, number


_ , ResultNumber = check_even(123)


if ResultNumber:
    print("number", ResultNumber, "is even.")
else:
    print("number", ResultNumber, "is odd.")
