import tkinter as tk
from tkinter import E, W, N, S

window = tk.Tk()

FahrenLBL = tk.Label(
    master=window,
    text="Fahrenheit:"
)
FahrEntr = tk.Entry(
    master=window,
    width=50,
)
CalcBTN = tk.Button(
    master=window,
    text="Calculate",
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



def CloseWindow():
    window.quit()
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