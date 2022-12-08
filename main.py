import tkinter as tk
from tkinter import ttk

def makeTextScroll(frame):
    textBox = tk.Text(frame, width=50, height=10)
    scroll = tk.Scrollbar(frame, orient=tk.VERTICAL, command=textBox.yview)
    textBox["yscrollcommand"] = scroll.set
    scroll.pack(side=tk.RIGHT, fill="y")
    textBox.pack()


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
makeTextScroll(inputTextFrame)

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
makeTextScroll(outputTextFrame)

root.mainloop()