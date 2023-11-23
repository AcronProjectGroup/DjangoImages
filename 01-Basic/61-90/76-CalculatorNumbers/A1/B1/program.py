import tkinter as tk
from tkinter import E, W, N, S

window = tk.Tk()

LBLCaclResult = tk.Label(
    master=window,
    text="0",
    width=30,
    height=3,
)

btn7 = tk.Button(
    master=window,
    text="7",
    command=lambda: print("7"),
)

btn8 = tk.Button(
    master=window,
    text="8",
    command=lambda: print("8"),
)

btn9 = tk.Button(
    master=window,
    text="9",
    command=lambda: print("9"),
)

btnPlus = tk.Button(
    master=window,
    text="+",
    command=lambda: print("+"),
)

LBLCaclResult.grid(row=0, column=0, columnspan=4)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btnPlus.grid(row=1, column=3)

def CloseWindow():
    """
    This function use in button.
    Its function is to close the program.
    So enjoy it ! :)
    """
    window.quit()


CloseBtn = tk.Button(
    master=window,
    text="Close",
    command=CloseWindow,
    fg="white",
    bg="#a90462",
)

CloseBtn.grid(
    row=10, 
    column=0, 
    columnspan=10, 
    sticky=(E, W),
    padx=1,
    pady=1,
)



window.mainloop()

