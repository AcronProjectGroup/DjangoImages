import random

choicesList = ['r', 'p', 's']


userScore = 0
aiScore = 0

for i in range(10): 
    aiChoice = random.choice(choicesList)
    userInput = input('Rock, Paper, Scissors? (R P S) -> ')
    if userInput in choicesList:
        print(f'Your choice is {userInput}. AI choice is {aiChoice}')
        if userInput == aiChoice:
            print('Tie')
        elif userInput == 'r' and aiChoice == 's':
            userScore += 1
            print('You won')
        elif userInput == 'p' and aiChoice == 'r':
            userScore += 1
            print('You won')
        elif userInput == 's' and aiChoice == 'p':
            userScore += 1
            print('You won')
        else:
            aiScore += 1
            print('You lost')
    else:
        print('Invalid input')


print(f'Your Score = {userScore}')
print(f'AI Score = {aiScore}')