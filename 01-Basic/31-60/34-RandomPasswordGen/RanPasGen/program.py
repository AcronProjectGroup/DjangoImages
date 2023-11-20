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

def GetSetUser(Settings):
    for option, default in Settings.items():
        if option != 'length':
            while True:
                UsrInput = input(f'Contain {option}? (Default={default}) y:Yes, n:No -> ')
                if UsrInput == 'y' or UsrInput == 'n' or UsrInput == '':
                    if UsrInput == 'y':
                        Settings[option] = True
                    elif UsrInput == '':
                        Settings[option] = Settings[option]
                    else:
                        Settings[option] = False    
                    break
                else:
                    print('Invalide input. Please write again.')

GetSetUser(Settings)

print(Settings)
    
