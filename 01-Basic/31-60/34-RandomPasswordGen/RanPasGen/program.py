import random
import string

Settings = {
    "lower": True,
    "upper": True,
    "symbol": True,
    "number": True,
    "space": False,
    "length": 8,
}

def GetYesOrNo(option, default):
    while True:
        UsrInput = input(f'Contain {option}? (Enter=Default={default}) y:Yes, n:No -> ')
        if UsrInput == '':
            return default
        if UsrInput in ['y', 'n']:
            return UsrInput == 'y'

        print('Invalide input. Please write again.')

def GetUsrPassLength(option, default):
    while True:
        UsrInput = input(f'Enter pass Length: Enter-Default=8 -> ')
        if UsrInput == '':
            return default
        if UsrInput.isdigit() and int(UsrInput) > 5 and int(UsrInput) <= 50  :
            return int(UsrInput)
        print('Invalide input. Please write specified "Number".(6-50)')
        

def GetSetUser(Settings):
    for option, default in Settings.items():
        if option != 'length':
            UsrChoices = GetYesOrNo(option, default)
            Settings[option] = UsrChoices
        else:
            Settings[option] = GetUsrPassLength(option, default)

def getRandomUppCase():
    return random.choice(string.ascii_uppercase)
def GetRandomLowCase():
    return random.choice(string.ascii_lowercase)
def GetRandomSynbol():
    return random.choice("""'"[<=>]{/*-+};:~_!@#$%^&()""")
def GetRandomNumber():
    return random.choice('0123456789')
def PassGenerateChar(choices):
    choice = random.choice(choices)
    if choice == 'upper':
        return getRandomUppCase()
    if choice == 'lower':
        return GetRandomLowCase()
    if choice == 'symbol':
        return GetRandomSynbol()
    if choice == 'number':
        return GetRandomNumber()
    if choice == 'space':
        return ' '    

def PassGen(Settings):
    passLengt = Settings['length']
    FinalPass = ''

    choices = list(filter(lambda x: Settings[x], ['lower','upper','symbol','number','space']))
    # print(choices)
    # choices = []
    # for option, value in Settings.items():
    #     if value == True: # Here I wrote value Exactly should be TRUE 
    #                       # If is not, don't go in 'if condition'
    #         choices.append(option)

    for i in range(passLengt):
        FinalPass += PassGenerateChar(choices)
    
    return FinalPass




GetSetUser(Settings)
    
print(PassGen(Settings))
