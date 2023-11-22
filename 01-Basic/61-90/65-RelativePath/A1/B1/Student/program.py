# Attention we are in Student directory 
# and read Scores.txt in Backward directory

with open("../Scores.txt", "r") as reader:
    AllData = reader.read()
    print(AllData)

# Output:
    # Sina 10
    # Mina 20
    # Jina 14
    # Lina 17
    # Tina 12.5
    # Bina 16.75
    # Nina 17.05
    # Fardaad 10
    # Baran 19.75
    # Nima 13.55