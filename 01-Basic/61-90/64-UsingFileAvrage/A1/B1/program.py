with open("Scores.txt", "r") as reader:
    AllData = reader.read()
    SplitData = AllData.split("\n")
    
    SeprationDictionary = {}
    for i in SplitData:
        Key, Value = i.split(" ")
        SeprationDictionary[Key] = Value

    print(SeprationDictionary)