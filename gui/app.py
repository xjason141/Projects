#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
import sqlite3 as sq
import hashlib
import datetime as dt
import main as mn

#main app
root = Tk()
root.title('test app')
root.minsize(1000,650)
root.configure(bg='#581845')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#login function
def login(u, p):
        #for practice purpose, user='didi123', password=didipassword
        #using sqlite3 to store login info in database
        conn = sq.connect('gui/info.db')
        cur = conn.cursor()

        theUser = u.get()
        thePassword = p.get()
        hashed = hashlib.sha256(thePassword.encode()).hexdigest()

        cur.execute('SELECT user FROM loginInfo WHERE user=? AND password=?', (theUser, hashed))
        check = cur.fetchone()

        if check:
            selector()
        else:
            messagebox.showerror(title='Failed', message='Invalid Username or Password')

#main window Frame
def mainWindow():

    #main window to store login frame and widgets
    mainWin = Frame(root, bg='#581845')
    mainWin.grid(column=0, row=0, sticky=NSEW)

    #login widgets in here
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
    log_btn = Button(loginFrame, text='Login', bg='#581845', fg='#ff6eeb', font=('arial', 11), command=lambda u=userEntry, p=passEntry: login(u, p))
    log_btn.grid(column=0, row=3, columnspan=2, pady=12)
    root.bind('<Return>', lambda event, u=userEntry, p=passEntry: login(u, p))

    # root.bind('g', login)
    mainWin.tkraise()


#select either to register guest or search for guest
def selector():

    #logout confirmation function
    def confirm():
        answer = askyesno(title='confirmation',
                          message='Are you sure you want to log out?')
        
        if answer:
            mainWindow()

    #window
    selectWIndow = Frame(root, bg='grey')
    selectWIndow.grid(column=0, row=0, sticky=NSEW)

    selectorFrame = Frame(selectWIndow, bg='grey')
    selectorFrame.place(relx=0.5, rely=0.5, anchor='center')

    #update guest list
    toUpdate = Button(selectorFrame, text='Register Guest',command=guestWindow)
    toUpdate.grid(column=0, row=0, padx=(0,30), pady=(5,0))

    #search for guest
    toSearch = Button(selectorFrame, text='Search for Guest', command=search)
    toSearch.grid(column=1, row=0, padx=(30,0), pady=(5,0))

    #logout button
    logoutBtn = Button(selectorFrame, text='Log Out', font=('arial', 11), command=confirm)
    logoutBtn.grid(column=0, row=1, columnspan=2, pady=(70,0))

    selectWIndow.tkraise()


#register guest
def guestWindow():
    curr_date = dt.datetime.now().strftime('%d-%b-%Y')
    curr_time = dt.datetime.now().strftime('%H:%M')

    #place all widgets in here
    guestWin = Frame(root, bg='#e8c5ff')
    guestWin.grid(column=0, row=0, sticky=NSEW)

    #back button
    backBtn = Button(guestWin, text='Back', command=selector, bg='#e8c5ff')
    backBtn.grid(column=0, row=0, padx=30, pady=(30,0))

    #guest info Frame
    guestFrame = Frame(guestWin, bg='#e8c5ff')
    guestFrame.place(relx=0.5, rely=0.5, anchor='center')

    #guests info below
    ### date ###
    date = Label(guestFrame, text='Date', font=('arial', 11), bg='#e8c5ff')
    date.grid(column=0, row=0, padx=15)
    dateEntry = Entry(guestFrame)
    dateEntry.insert(0, curr_date)
    dateEntry.grid(column=1, row=0, pady=5)

    ### id ###
    id = Label(guestFrame, text='ID', font=('arial', 11), bg='#e8c5ff')
    id.grid(column=0, row=1, padx=15)
    idEntry = Entry(guestFrame, textvariable=StringVar())
    idEntry.grid(column=1, row=1, pady=5)

    ### time ###
    time = Label(guestFrame, text='Time', font=('arial', 11), bg='#e8c5ff')
    time.grid(column=2, row=0, padx=(120,15))
    timeEntry = Entry(guestFrame)
    timeEntry.insert(0, curr_time)
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

    guestWin.tkraise()


#to search guest in guest list via ID
def search():

    #searcWindow
    searchWIn = Frame(root, bg='#8f009b')
    searchWIn.grid(column=0, row=0, sticky=NSEW)

    #back button
    backBtn = Button(searchWIn, text='Back', command=selector, bg='#8f009b')
    backBtn.grid(column=0, row=0, padx=30, pady=(30,0))

    #searchFrame
    searchFrame = Frame(searchWIn, bg='#8f009b')
    searchFrame.place(rely=0.5, relx=0.5, anchor='center')

    #search guest entries
    searchLabel = Label(searchFrame, text='ID', font=('arial', 11), bg='#8f009b', fg='#FFFFFF')
    searchLabel.grid(column=0, row=0, padx=10)
    searchEntry = Entry(searchFrame, textvariable=StringVar())
    searchEntry.grid(column=1, row=0, padx=10)
    searchBtn = Button(searchFrame, text='Search', font=('arial', 11))
    searchBtn.grid(column=0, row=1, columnspan=2, pady=20)

    searchWIn.tkraise()

#run mainWindow() for full gui
mainWindow()

if __name__ == '__main__':
    root.mainloop()