import tkinter as tk

window = tk.Tk()

textVar = tk.StringVar()

# Label
text = tk.Label(
    master=window,
    # text="Django Web Application",
    textvariable=textVar,
)
UserInput = tk.Entry(
    master=window,
    textvariable=textVar,
)
text1 = tk.Label(
    master=window,
    text="First Name",
)
text1.pack(side=tk.LEFT)
UserInput.pack(side=tk.LEFT)

text.pack(side=tk.LEFT)


window.mainloop()
