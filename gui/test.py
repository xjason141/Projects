#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
import hashlib

root = Tk()
root.title('test app')
root.minsize(1000,650)
root.configure(bg='#581845')
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0, weight=1)



def mainF():
    mainFrame = Frame(root, bg='red')
    mainFrame.grid(column=0, row=0, sticky=NSEW)

    logFrame = Frame(mainFrame)
    logFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    logBtn = Button(logFrame, text='Login', fg='black', command=secF)
    logBtn.grid(column=1, row=1)

    mainFrame.tkraise()

def secF():
    secFrame = Frame(root, bg='blue')
    secFrame.grid(column=0, row=0, sticky=NSEW)

    guestFrame = Frame(secFrame)
    guestFrame.place(rely=0.5, relx=0.5, anchor=CENTER)

    exitBtn = Button(guestFrame, text='Log Out', fg='black', command=mainF)
    exitBtn.grid(column=1, row=1)




    secFrame.tkraise()






mainF()

if __name__ == '__main__':
    root.mainloop()