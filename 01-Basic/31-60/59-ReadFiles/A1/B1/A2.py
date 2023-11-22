FileNames = open("Names.txt", "r")

ListNames = FileNames.read().split("\n")

print(ListNames)

# Output:
    # ['Sina', 'Mina', 'Lina', 'Bina', 'Jina', 'Shina']
