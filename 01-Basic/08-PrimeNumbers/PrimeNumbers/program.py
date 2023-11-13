userInput = int(input("What's your Number: "))

isPrime = False

for i in range(2, userInput):
    if userInput % i == 0 :
        print(f"{userInput} can divide by {i}, So it's not prime.")
        break
    else:
        isPrime = True
    
if isPrime:
    print(f'Because the number {userInput} is divisible only by one and itself, it is the prime number.')
    