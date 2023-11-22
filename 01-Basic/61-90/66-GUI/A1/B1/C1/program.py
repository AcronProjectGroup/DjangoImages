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
UserInput.pack()
text.pack()

text1 = tk.Label(
    master=window,
    text="SINA LALEHBAKHSH",
)

text1.pack()
window.mainloop()
