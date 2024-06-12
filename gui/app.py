#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
import hashlib

root = Tk()
root.title('test app')
root.minsize(1000,650)
root.configure(bg='#581845')

#main frame
mainFrame = Frame(root, bg='#581845')
mainFrame.place(relx=0.5, rely=0.5, anchor=CENTER)


#login func
def login():
    #for practice purpose, user='didi123', password=didipassword
    #using sqlite3 to store login info in database
    conn = sq.connect('gui/info.db')
    cur = conn.cursor()

    user = userEntry.get()
    password = passEntry.get()
    hashed = hashlib.sha256(password.encode()).hexdigest()

    cur.execute('SELECT user FROM loginInfo WHERE user=? AND password=?', (user, hashed))
    check = cur.fetchone()

    if check:
        messagebox.showinfo(title='success', message='User exists')
    else:
        messagebox.showerror(title='Failed', message='Invalid Username or Password')


#welcome text
welcome_text = Label(mainFrame, text='Welcome', bg='#581845', fg='#ff6eeb', font=('arial', 20))
welcome_text.grid(column=0, row=0, columnspan=2, pady=15)


#username and entry box
userLabel = Label(mainFrame, text='Username', padx=10, bg='#581845', fg='#FFFFFF', font=('arial', 11))
username = StringVar()
userEntry = Entry(mainFrame, textvariable=username)
userLabel.grid(column=0, row=1)
userEntry.grid(column=1, row=1, pady=5)


# #password and entry box
passLabel = Label(mainFrame, text='Password', pady=10, bg='#581845', fg='#FFFFFF', font=('arial', 11))
password = StringVar()
passEntry = Entry(mainFrame, textvariable=password, show='*')
passLabel.grid(column=0, row=2)
passEntry.grid(column=1, row=2, pady=5)


#login button
log_btn = Button(mainFrame, text='Login', bg='#581845', fg='#ff6eeb', font=('arial', 11), command=login)
log_btn.grid(column=0, row=3, columnspan=2, pady=12)


if __name__ == '__main__':
    root.mainloop()