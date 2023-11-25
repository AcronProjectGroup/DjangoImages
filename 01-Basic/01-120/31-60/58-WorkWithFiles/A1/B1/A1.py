file = open("Sina.txt", "w") # w: write  --- r: read

while True:
    UserTextAdding = input("write in Sina.txt: ")
    if UserTextAdding == "fin":
        break
    # and Delete past data
    file.write(f"{UserTextAdding}\n")


