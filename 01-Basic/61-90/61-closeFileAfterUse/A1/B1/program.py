nameFile = open("AllNames.txt", "r")

AllNameVar = nameFile.read()

# After storing file to the AllNameVar variable, close it.
nameFile.close()

AllNameVar = AllNameVar.split("\n")

while True:
    UserInput = input("Name? ")
    if UserInput == "fin":
        break
    AllNameVar.append(UserInput)

print(AllNameVar)

# Input:
    # sina
    # fin
# Output:
#     Name? sina
#     Name? fin
#     ['Sina', 'Mina', 'Lina', 'Bina', 'Jina', 'Tina', 'sina']
