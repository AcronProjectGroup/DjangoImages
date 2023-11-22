with open("Scores.txt", "r") as reader:
    AllData = reader.read()
    SplitData = AllData.split("\n")

NewScores = []
GetAddAnother = input("Want Add Item? ")
if GetAddAnother.lower() == "yes":
    while True:
        name = input("Name? ")
        if name == "fin":
            break
        score = input("Score? ")
        if score == "fin":
            break
        NewScores.append({
            "name": name,
            "score": score,
        })

with open("Scores.txt", "a") as AddFile:
    for AddGrade in NewScores:
        AddFile.write(f"\n{AddGrade['name']} {AddGrade['score']}")



with open("Scores.txt", "r") as reader:
    AllData = reader.read()
    SplitData = AllData.split("\n")
    for i in SplitData:
        _, x2 = lambda x: print(x), i.split(" ")
        print(f"{x2[0]:8}{x2[1]}")
# Output:
    # Sina    10
    # Mina    20
    # Jina    14
    # Lina    17
    # Tina    12.5
    # Bina    16.75
    # Nina    17.05
    # Fardaad 10
    # Baran   19.75
    # Nima    13.55
