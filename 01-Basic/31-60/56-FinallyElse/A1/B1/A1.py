

UsrInput = int(input("Income? "))


try:
    print( 10 / UsrInput)
except ZeroDivisionError as TextErr:
    print("Zero!?", TextErr)
except ModuleNotFoundError as TextErr:
    print("Not Import!?", TextErr)
else: 
    # If there is no Error = Code don't have any error
    print("I don't have an any error")
finally:
    # By all means, do this part
    print("By all means, do this part. -> FINALLY <-")



