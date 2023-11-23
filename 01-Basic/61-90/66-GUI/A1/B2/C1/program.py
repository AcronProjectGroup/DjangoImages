# for run use python3.10 program.py

import tkinter as tk

window = tk.Tk()

def ButtonClicked():
    ShowLabel["text"] = NameEntry.get()

NameEntry = tk.Entry(
    master=window,
)

SubmitButton = tk.Button(
    master=window,
    text="Submit",
    command=ButtonClicked,
)

ShowLabel = tk.Label(
    master=window,
    text="test",
)

NameEntry.pack()
SubmitButton.pack()
ShowLabel.pack()

window.mainloop()
