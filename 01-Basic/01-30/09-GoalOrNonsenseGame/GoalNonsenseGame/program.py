# Goal Or None Sense Game

import random



cups = int(input("How many cups?"))
chances = int(input("How many chances?"))

ai_goal = random.randint(1, cups)

print("-" * 10)


for i in range(chances):
    print(f'{chances - i} chances left.')
    user_guess = int(input(f'Guess [1-{cups}]: '))

    if user_guess == ai_goal:
        print('You guesses right.')
        break
    else:
        print('\U0001F976 \U0001FAE8 \U0001F976 \U0001FAE8 ')
        print('\U0001F976 \U0001FAE5 \U0001F976 \U0001FAE8 \U0001FAE8')
        print("-" * 10)


if user_guess == ai_goal:
    print('='*15)
    print('\U0001F493 \U0001F60D \U0001F493 \U0001F60D \U0001F493 \U0001F60D \U0001F493 \U0001F60D\U0001F917\U0001F917 \U0001F917')
    
else:
    print(f'The right answer is {ai_goal}.')
    print('You lost. Sorry!')

