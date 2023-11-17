

userInput = 'sina'

print(f'\n{userInput} before encryption ...\n')

Encryption = []

for i in userInput:
    Encryption.append((ord(i)+10)-5)  

print(f'{userInput} encrypted = {Encryption}.\n')

decrypted = []

for i in Encryption:
    first = (i-10)+5
    decrypted.append(first)


print(f'{Encryption} decrypted = {decrypted}.\n')
