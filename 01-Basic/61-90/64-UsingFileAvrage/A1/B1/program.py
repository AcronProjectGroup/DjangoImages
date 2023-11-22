with open("Scores.txt", "r") as reader:
    AllData = reader.read()
    SplitData = AllData.split("\n")

SeprationDictionary = {}
for i in SplitData:
    Key, Value = i.split(" ")
    SeprationDictionary[Key] = Value

print(SeprationDictionary)

# Sina 10
# Mina 20
# Jina 14
# Lina 17
# Tina 12.5
# Bina 16.75
# Nina 17.05