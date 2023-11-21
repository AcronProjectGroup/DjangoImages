while True:
    UserTextAdding = input("write in Sina.txt: ")
    if UserTextAdding == "fin":
        break
    file = open("Sina.txt", "w") # w: write  --- r: read
    # and Delete past data
    file.write(UserTextAdding)


