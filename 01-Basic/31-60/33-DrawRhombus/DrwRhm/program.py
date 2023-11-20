def SpaceStars(numberStar, TotalStars):
    NumberSpaces = (TotalStars-numberStar) // 2
    print(f"{' ' * NumberSpaces}{'*' * numberStar}{' ' * NumberSpaces}")
     


def DrawRhombus(number):
    if number % 2 == 0:
        number += 1
    
    print()
    for i in range(number):
        if i < number / 2:
            SpaceStars((i*2 + 1), number)
        else:
            SpaceStars(((number-i)*2 - 1), number)
    print()
    

DrawRhombus(50)

     

