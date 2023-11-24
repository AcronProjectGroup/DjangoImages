while True:
    UserInput = input("Number? ")
    result = None

    try:
        result = int(UserInput)
    except ValueError:
        print("Can't Convert to integer")
        try:
            result = float(UserInput)
        except:
            print("Can't Convert to float!")
            print(f"{UserInput} can just convert to string, Idiot!")
        else:
            print(f"Result= {result}")    
            break
    else:
        print(f"Result= {result}")
        break



