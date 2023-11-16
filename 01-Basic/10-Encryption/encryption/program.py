

userInput = 'sina'

print(f'\n{userInput} before encryption ...\n')

Encryption = []

for i in userInput:
    Encryption.append(ord(i))  

print(f'{userInput} encrypted = {Encryption}.\n')


decrypted = ''
for i in Encryption:
    decrypted += chr(i)

print(f'{Encryption} decrypted = {decrypted}.\n')
