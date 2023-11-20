# Random Password Generator

# Length = 6

# Lower
# upper
# symbol
# number

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
        UsrInput = input(f'Enter pass Length: Enter-Default=8')
        if UsrInput == '':
            return default
        if UsrInput.isdigit() and int(UsrInput) > 5 :
            return int(UsrInput)
        print('Invalide input. Please write specified "Number" again.')
        

def GetSetUser(Settings):
    for option, default in Settings.items():
        if option != 'length':
            UsrChoices = GetYesOrNo(option, default)
            Settings[option] = UsrChoices
        else:
            UsrPassLength = GetUsrPassLength(option, default)

GetSetUser(Settings)
print(Settings)
    
