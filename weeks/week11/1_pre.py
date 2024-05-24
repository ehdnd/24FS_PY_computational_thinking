# #1. 윈도우 창 만들기
# from tkinter import *

# root = Tk()
# root.geometry("640x480+2500+100")
# root.resizable(False, False)
# root.title("윈도우 창 만들기")

# root.mainloop()

#2. 배치관리자
from tkinter import *

root = Tk()
root.geometry("640x480")
root.title("winodws button")

btn1 = Button(root, text="button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="button2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="button3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="button4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="button5")
btn5.pack()

def btncmd():
    print("hi")

btn6 = Button(root, text="print hi", command=btncmd)
btn6.pack()


label1 = Label(root, text="label1")
label1.pack()

label2 = Label(root, text="label2")
label2.pack()

label3 = Label(root, text="just showing text", font="Times 20 bold italic", fg="white", bg="black")
label3.pack()


def change():
    label3.config(text="text has been changed")

btn = Button(root, text="change text", command=change)
btn.pack()

root.mainloop()