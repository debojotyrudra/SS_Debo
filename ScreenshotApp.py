import tkinter
import pyautogui
from tkinter import *

def takess():
    add=entry.get()
    path=add+"\\test18.png"
    print(path)
    ss=pyautogui.screenshot()
    ss.save(path)

win=tkinter.Tk()
win.title("Sample Screenshot Application by Debo")
win.geometry("500x500")
win.config(bg="crimson")
win.resizable(False,False)

entry=Entry(win,font=('Times New Roman',30))
entry.place(x=10,y=30,height=50,width=300)

button=Button(win,text="Done",font=('Times New Roman',20),command=takess)
button.place(x=50,y=200,height=50,width=100)
win.mainloop()
