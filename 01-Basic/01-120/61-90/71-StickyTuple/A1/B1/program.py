# for run use python3.10 program.py

import tkinter as tk
from tkinter import E, W
window = tk.Tk()

TitlLBL = tk.Label(
    master=window,
    text="Enter Your Data",
)

lblFirstName = tk.Label(
    master=window,
    text="First Name: ",
)
EntName = tk.Entry(
    master=window,
)

resultLBL = tk.Label(
    master=window,
    text="Result",
)


def GetEntNameToResultLBL():
    resultLBL["text"] = EntName.get()


OKButton = tk.Button(
    master=window,
    text="Click",
    command=GetEntNameToResultLBL,
    fg="white",
    bg="#094260",
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

TitlLBL.grid(row=0, column=0, columnspan=2)
lblFirstName.grid(row=1, column=0)
EntName.grid(row=1, column=1)
CloseBtn.grid(row=2, column=0)
OKButton.grid(row=2, column=1, sticky=(E, W))
resultLBL.grid(row=4, column=1)

window.mainloop()
