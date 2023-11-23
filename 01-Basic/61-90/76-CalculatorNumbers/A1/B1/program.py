import tkinter as tk
from tkinter import E, W, N, S

window = tk.Tk()

LBLCaclResult = tk.Label(
    master=window,
    text="0",
    width=30,
    height=3,
)
LBLCaclResult.grid(row=0, column=0, columnspan=4)

def InsertNumberInLabal(btnText):
    LBLCaclResult["text"] = btnText

Keys = [
    {
        "text": "7",
        "command": lambda: InsertNumberInLabal("7"),
    },
    {
        "text": "8",
        "command": lambda: InsertNumberInLabal("8"),
    },
    {
        "text": "9",
        "command": lambda: InsertNumberInLabal("9"),
    },
    {
        "text": "+",
        "command": lambda: InsertNumberInLabal("+"),
    },
    {
        "text": "4",
        "command": lambda: InsertNumberInLabal("4"),
    },
    {
        "text": "5",
        "command": lambda: InsertNumberInLabal("5"),
    },
    {
        "text": "6",
        "command": lambda: InsertNumberInLabal("6"),
    },
    {
        "text": "-",
        "command": lambda: InsertNumberInLabal("-"),
    },
    {
        "text": "1",
        "command": lambda: InsertNumberInLabal("1"),
    },
    {
        "text": "2",
        "command": lambda: InsertNumberInLabal("2"),
    },
    {
        "text": "3",
        "command": lambda: InsertNumberInLabal("3"),
    },
    {
        "text": "*",
        "command": lambda: InsertNumberInLabal("*"),
    },
    {
        "text": ".",
        "command": lambda: InsertNumberInLabal("."),
    },
    {
        "text": "0",
        "command": lambda: InsertNumberInLabal("0"),
    },
    {
        "text": "CR",
        "command": lambda: InsertNumberInLabal("CR"),
    },
    {
        "text": "=",
        "command": lambda: InsertNumberInLabal("="),
    },
]


KeysObjects = []

for data in Keys:
    btn = tk.Button(
        master=window,
        text=data["text"],
        command=data["command"],
    )
    KeysObjects.append(btn)

for i, Object in enumerate(KeysObjects):
    Object.grid(row=(i//4)+1, column=(i%4), sticky=(N, E, W, S))


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
