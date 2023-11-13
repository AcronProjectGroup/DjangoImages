# sum of the digits of a number

userInput = int(input('Enter Number:'))

result = 0

while userInput != 0:
    result += userInput % 10
    userInput = userInput // 10

print(result)