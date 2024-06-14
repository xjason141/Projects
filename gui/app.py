#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
import hashlib
import datetime

#main app
root = Tk()
root.title('test app')
root.minsize(1000,650)
root.configure(bg='#581845')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


#mainWindow Frame
def mainWindow():

    #login function
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
            guestWindow()
        else:
            messagebox.showerror(title='Failed', message='Invalid Username or Password')


    #mainWin to store all widgets
    mainWin = Frame(root, bg='#581845')
    mainWin.grid(column=0, row=0, sticky=NSEW)

    #put login widgets in here
    loginFrame = Frame(mainWin, bg='#581845')
    loginFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    #username and entry box
    userLabel = Label(loginFrame, text='Username', padx=10, bg='#581845', fg='#FFFFFF', font=('arial', 11))
    username = StringVar()
    userEntry = Entry(loginFrame, textvariable=username)
    userLabel.grid(column=0, row=1)
    userEntry.grid(column=1, row=1, pady=5)

    #password and entry box
    passLabel = Label(loginFrame, text='Password', pady=10, bg='#581845', fg='#FFFFFF', font=('arial', 11))
    password = StringVar()
    passEntry = Entry(loginFrame, textvariable=password, show='*')
    passLabel.grid(column=0, row=2)
    passEntry.grid(column=1, row=2, pady=5)

    #welcome text
    welcome_text = Label(loginFrame, text='Welcome', bg='#581845', fg='#ff6eeb', font=('arial', 20))
    welcome_text.grid(column=0, row=0, columnspan=2, pady=15)

    #login button
    log_btn = Button(loginFrame, text='Login', bg='#581845', fg='#ff6eeb', font=('arial', 11), command=login)
    log_btn.grid(column=0, row=3, columnspan=2, pady=12)

    mainWin.tkraise()


#guest info window
def guestWindow():

    curr_time = datetime.datetime.now().strftime('%H:%M')
    curr_date = datetime.datetime.now().strftime('%d-%b-%Y')

    #place all widgets in here
    guestWin = Frame(root, bg='#e8c5ff')
    guestWin.grid(column=0, row=0, sticky=NSEW)

    #guest info Frame
    guestFrame = Frame(guestWin, bg='#e8c5ff')
    guestFrame.place(relx=0.5, rely=0.5, anchor='center')

    #guests info below
    ### date ###
    date = Label(guestFrame, text='Date', font=('arial', 11), bg='#e8c5ff')
    date.grid(column=0, row=0, padx=15)
    dateEntry = Entry(guestFrame, textvariable=curr_date)
    dateEntry.grid(column=1, row=0, pady=5)


    ### id ###
    id = Label(guestFrame, text='ID', font=('arial', 11), bg='#e8c5ff')
    id.grid(column=0, row=1, padx=15)
    idEntry = Entry(guestFrame, textvariable=StringVar())
    idEntry.grid(column=1, row=1, pady=5)


    ### time ###
    time = Label(guestFrame, text='Time', font=('arial', 11), bg='#e8c5ff')
    time.grid(column=2, row=0, padx=(120,15))
    timeEntry = Entry(guestFrame, textvariable=curr_time)
    timeEntry.grid(column=3, row=0, pady=5)


    ### name ###
    name = Label(guestFrame, text='Name', font=('arial', 11), bg='#e8c5ff')
    name.grid(column=0, row=2, padx=15)
    nameEntry = Entry(guestFrame, textvariable=StringVar())
    nameEntry.grid(column=1, row=2, pady=5)


    ### address ###
    address = Label(guestFrame, text='Address', font=('arial', 11), bg='#e8c5ff')
    address.grid(column=0, row=3, padx=15)
    addressEntry = Entry(guestFrame, textvariable=StringVar())
    addressEntry.grid(column=1, row=3, pady=5)


    ### plate number ###
    plate = Label(guestFrame, text='Plate Number', font=('arial', 11), bg='#e8c5ff')
    plate.grid(column=2, row=1, padx=(120,15))
    plateEntry = Entry(guestFrame, textvariable=StringVar())
    plateEntry.grid(column=3, row=1, pady=5)


    ### reason ###
    reason = Label(guestFrame, text='Reason', font=('arial', 11), bg='#e8c5ff')
    reason.grid(column=2, row=2, padx=(120,15))
    reasonEntry = Entry(guestFrame, textvariable=StringVar())
    reasonEntry.grid(column=3, row=2, pady=5)




    #logout button
    # logoutBtn = Button(guestFrame, text='Logout', command=mainWindow)
    # logoutBtn.grid(column=0, row=3, columnspan=2, pady=12)

    guestWin.tkraise()


# mainWindow()
guestWindow()

if __name__ == '__main__':
    root.mainloop()