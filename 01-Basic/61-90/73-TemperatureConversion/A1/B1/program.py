import tkinter as tk
from tkinter import E, W, N, S

window = tk.Tk()

FahrenheitValue = tk.StringVar()    

def ConverFunction():
    """
    This function convert the User Input to Celsius number 
    and will write it to label in below.
    """
    UserInput = FahrenheitValue.get()
    try:
        UserInput = float(UserInput)
        # Converting is in this part
        ResultLBL["text"] =  (UserInput-32)*5 /9
    except ValueError:
        if UserInput != "":
            ResultLBL["text"] = "Just enter number"
        else:
            ResultLBL["text"] = "Can't be empty, whore!"



def CloseWindow():
    """
    This function use in button.
    Its function is to close the program.
    So enjoy it ! :)
    """
    window.quit()


FahrenLBL = tk.Label(
    master=window,
    text="Fahrenheit:"
)
FahrEntr = tk.Entry(
    master=window,
    width=50,
    textvariable=FahrenheitValue,
)
CalcBTN = tk.Button(
    master=window,
    text="Calculate",
    command=ConverFunction,
    fg="white",
    bg="#094260",
)

CelsLBL = tk.Label(
    master=window,
    text="Celsius: ",
)
    

ResultLBL = tk.Label(
    master=window,
    text="Result shows here ..."
)


CloseBtn = tk.Button(
    master=window,
    text="Close",
    command=CloseWindow,
    fg="white",
    bg="#a90462",
)


FahrenLBL.grid(row=0, column=0, padx=5, pady=10)
FahrEntr.grid(row=0, column=1, padx=5)
CalcBTN.grid(row=0, column=2, padx=3)
CelsLBL.grid(row=1, column=0)
ResultLBL.grid(row=1, column=1)



CloseBtn.grid(
    row=10, 
    column=0, 
    columnspan=10, 
    sticky=(E, W),
    padx=1,
    pady=1,
)


window.title("Temperature conversion")
window.mainloop()