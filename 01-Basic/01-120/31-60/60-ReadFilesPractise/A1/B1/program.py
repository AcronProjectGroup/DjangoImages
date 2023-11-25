nameFile = open("AllNames.txt", "r")
nameFile = nameFile.read()
nameFile = nameFile.split("\n")
print(nameFile)
# Output:
    # ['Sina', 'Mina', 'Lina', 'Bina', 'Jina', 'Tina']

while True:
    UserInput = input("Name? ")
    if UserInput == "fin":
        break
    nameFile.append(UserInput)

print(nameFile)
# Input:
    # Barbod
    # Barbod2
    # fin
# Output:
    # ['Sina', 'Mina', 'Lina', 'Bina', 'Jina', 'Tina', 'Barbod, 'Barbod2']


