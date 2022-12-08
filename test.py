import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("scrollbar")

textFrame = tk.Frame()
textFrame.pack()

textBox = tk.Text(textFrame, width=50, height=10)

scroll = tk.Scrollbar(textFrame, orient=tk.VERTICAL, command=textBox.yview)
scroll.pack(side=tk.RIGHT, fill="y")

textBox["yscrollcommand"] = scroll.set

textBox.pack()

root.mainloop()