import tkinter as tk
from tkinter import ttk

def makeTextScroll(frame):
    textBox = tk.Text(frame, width=50, height=10)
    scroll = tk.Scrollbar(frame, orient=tk.VERTICAL, command=textBox.yview)
    textBox["yscrollcommand"] = scroll.set
    scroll.pack(side=tk.RIGHT, fill="y")
    textBox.pack()

    return textBox

def getInputTextOutput(event):
    outputBox.insert("1.0", inputBox.get("1.0", tk.END))

# initialize
# window set
root = tk.Tk()
root.title("hi im title")

# Label
headerFrame = ttk.Frame(root, padding=10)
headerFrame.pack(fill=tk.X)
tk.Label(headerFrame, text="Readable").pack(side=tk.LEFT)

# inputTextFrame
inputTextFrame = ttk.Frame(root, padding=10)
inputTextFrame.pack()
inputBox = makeTextScroll(inputTextFrame)

# executeButton
executeButton = ttk.Button(root, text="Execute")
executeButton.pack()

# bodyFrame
bodyFrame = ttk.Frame(root, padding=10)
bodyFrame.pack()

# textFrame1 in bodyFrame
textFrame1 = ttk.Frame(bodyFrame, padding=10)
textFrame1.pack(side=tk.LEFT)
makeTextScroll(textFrame1)

# textFrame2 in bodyFrame
textFrame2 = ttk.Frame(bodyFrame, padding=10)
textFrame2.pack(side=tk.RIGHT)
makeTextScroll(textFrame2)

# nextButton 
nextButton = ttk.Button(root, text="Next")
nextButton.pack()

# outputBox
outputTextFrame = ttk.Frame(root, padding=10)
outputTextFrame.pack()
outputBox = makeTextScroll(outputTextFrame)

# Execute Button
executeButton2 = ttk.Button(root, text="Execute")
executeButton2.pack()
executeButton2.bind("<Button-1>", getInputTextOutput)

root.mainloop()

