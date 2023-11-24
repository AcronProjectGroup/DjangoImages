userInput = int(input("What's your Number: "))

isPrime = True

for i in range(2, userInput):
    if userInput % i == 0 :
        print(f"{userInput} can divide by {i}, So it's not prime.")
        isPrime = False
        break
    else:
        isPrime = True
    
if isPrime:
    print(f'Because the number {userInput} is divisible only by one and itself, it is the prime number.')
