# -*- coding:utf-8 -*-
from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("TXT and ENTRY")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(1.0, "Lines: ")

entry = Entry(root, width=30)
entry.pack()
entry.insert(0, "One line: ")

def btncmd():
    print(txt.get("1.0", END))
    print(entry.get())

    txt.delete("1.0", END)
    entry.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()