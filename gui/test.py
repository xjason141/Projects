from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
import hashlib

root = Tk()
root.title('test app')
root.minsize(1000,650)
root.configure(bg='#581845')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


def main():

    bgframe1 = Frame(root, bg='blue')
    bgframe1.grid(row=0, column=0, sticky=NSEW)

    #mainWin
    mainWin = Frame(bgframe1, bg='blue', width=500, height=500)
    mainWin.place(relx=0.5, rely=0.5, anchor=CENTER)

    #mainWin label
    mainLabel = Label(mainWin, text='This is mainWin', bg='red', fg='white')
    mainLabel.grid(column=1, row=0)

    #mainBtn
    chgBtn = Button(mainWin, text='Change to second window', command=secondWin)
    chgBtn.grid(column=1, row=1)


def secondWin():

    bgframe2 = Frame(root, bg='magenta')
    bgframe2.grid(row=0, column=0, sticky=NSEW)
    
    #secWin
    secWin = Frame(root, bg='magenta', width=500, height=500)
    secWin.place(relx=0.5, rely=0.5, anchor=CENTER)

    #secWin label
    secLabel = Label(secWin, text='This is secWin', bg='yellow', fg='black')
    secLabel.grid(column=1, row=0)

    #secBtn
    secBtn = Button(secWin, text='Change to first window window', command=main)
    secBtn.grid(column=1, row=1)

    # secWin.tkraise()

main()

if __name__ == '__main__':
    root.mainloop()