import random

WordsList = [
    "Deutsch",
    "Germany",
    "Berlin",
    "deutsch",
    "germany",
    "berlin",
    "Hamburg",
    "hamburg",
    "Munich",
    "munich",
    "Cologne",
    "cologne",
    "Leipzig",
    "leipzig",
    "Essen",
    "essen",
    "Frankfurt",
    "frankfurt",
    "Dortmund",
    "dortmund",
    "Stuttgart",
    "stuttgart",
    "Dusseldorf",
    "dusseldorf",
    "Bremen",
    "bremen",
    "Dresden",
    "dresden",
    "Hanover",
    "hanover",
    "Nuremberg",
    "nuremberg",
    "Duisburg",
    "duisburg",
]

def GetUserInput():
    while True:
        userInput = input('Enter your guess: ')
        if userInput.isalpha():
            print('User input is correct')
            return userInput
        else:
            print('Please enter just letters contain a-z,A-Z')

def Intro():
    print('-'*20)
    print("Hi")
    print("Welcome")
    print('All words:')
    counter = 0
    for i in WordsList:
        counter += 1
        print(f'{i:13}', end='')
        if counter == 4:
            print()
            counter = 0
    print()
    print('='*30)


def RunGame():
    Intro()
    print('number of guesses: 5')
    AIChoice = random.choice(WordsList)

    for i in range(5):
        userInput = GetUserInput()
        if userInput == AIChoice:
            print('YOU WON')
            break
        else:
            print('You guessed wrong!')
            print(f'Rounds left: {4-i}')
    
    print(f'Correct answer by AI was {AIChoice}')



RunGame()

# Output:
    # --------------------
    # Hi
    # Welcome
    # All words:
    # Deutsch      Germany      Berlin       deutsch      
    # germany      berlin       Hamburg      hamburg      
    # Munich       munich       Cologne      cologne      
    # Leipzig      leipzig      Essen        essen        
    # Frankfurt    frankfurt    Dortmund     dortmund     
    # Stuttgart    stuttgart    Dusseldorf   dusseldorf   
    # Bremen       bremen       Dresden      dresden      
    # Hanover      hanover      Nuremberg    nuremberg    
    # Duisburg     duisburg     
    # ==============================
    # number of guesses: 5
    # Enter your guess: Deutsch
    # User input is correct
    # You guessed wrong!
    # Rounds left: 4
    # Enter your guess: Germany
    # User input is correct
    # You guessed wrong!
    # Rounds left: 3
    # Enter your guess: Berlin
    # User input is correct
    # You guessed wrong!
    # Rounds left: 2
    # Enter your guess: deutsch
    # User input is correct
    # You guessed wrong!
    # Rounds left: 1
    # Enter your guess: germany
    # User input is correct
    # You guessed wrong!
    # Rounds left: 0
    # Correct answer by AI was Cologne

    