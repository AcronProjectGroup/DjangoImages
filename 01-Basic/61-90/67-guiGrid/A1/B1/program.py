# for run use python3.10 program.py

import tkinter as tk

window = tk.Tk()

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

lblFirstName.grid(row=0,column=1)
EntName.grid(row=0,column=2)
OKButton.grid(row=1,column=2)
CloseBtn.grid(row=2,column=1)
resultLBL.grid(row=2,column=2)

window.mainloop()