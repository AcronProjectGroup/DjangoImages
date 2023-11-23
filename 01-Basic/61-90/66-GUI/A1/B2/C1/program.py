import tkinter as tk

window = tk.Tk()

NameEntry = tk.Entry(
    master=window,
)

SubmitButton = tk.Button(
    master=window,
    text="Submit",
)

ShowLabel = tk.Label(
    master=window,
    text="test",
)

NameEntry.pack()
SubmitButton.pack()
ShowLabel.pack()

# window.mainloop()
