choices = ['r', 'p', 's']

aiChoice = ''

userInput = input('Rock, Paper, Scissors? (R P S) -> ')

if userInput in choices:
    print(f'Your choice is {userInput}. AI choice is {aiChoice}')
    if userInput == aiChoice:
        print('Tie')
    elif userInput == 'r' and aiChoice == 's':
        print('You won')
    elif userInput == 'p' and aiChoice == 'r':
        print('You won')
    elif userInput == 's' and aiChoice == 'p':
        print('You won')
    else:
        print('You lost')
else:
    print('Invalid input')

