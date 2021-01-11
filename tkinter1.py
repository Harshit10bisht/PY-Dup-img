import sys
import os
import Tkinter
import tkMessageBox
top=Tkinter.Tk()

def helloCallBack():
    os.system('tkinterdemo.py')

B=Tkinter.Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()
