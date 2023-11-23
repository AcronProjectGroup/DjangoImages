import tkinter as tk
import subprocess

window = tk.Tk()

lblFirstName = tk.Label(
    master=window,
    text="First Name: ",
)
EntName = tk.Entry(
    master=window,
)

goResultLBL = tk.Label(
    master=window,
    text="Go Result",
)

resultLBL = tk.Label(
    master=window,
    text="Result",
)

def GetEntNameToResultLBL():
    resultLBL["text"] = EntName.get()

def RunGoProgram():
    result = subprocess.run(["go", "run", "-e", "-"], input=b'fmt.Print("Test")', capture_output=True, text=True)
    goResultLBL["text"] = result.stdout

OKButton = tk.Button(
    master=window,
    text="Click",
    command=RunGoProgram,
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
goResultLBL.grid(row=2, column=2)
resultLBL.grid(row=3,column=2)

window.mainloop()
