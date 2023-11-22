
with open("AllNames.txt", "r") as reader:
# It is equivalent to the bottom line
# nameFile = open("AllNames.txt", "r")
    nameFile = reader
    # after this line file is closed force.
    AllNameVar = nameFile.read()


AllNameVar = AllNameVar.split("\n")

while True:
    UserInput = input("Name? ")
    if UserInput == "fin":
        break
    AllNameVar.append(UserInput)

print(AllNameVar)

