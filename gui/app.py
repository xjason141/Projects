#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('test app')
root.minsize(1000,650)
root.configure(bg='#581845')
# root.maxsize(1000,650)

#main frame
mainFrame = Frame(bg='#581845')
mainFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

#login func
def login():
    #for real life use, should use a database to store username and password login info. code below is hardcoded and only for learning purposes
    username = 'didi'
    password = '12345'
    if userEntry.get()==username and passEntry.get()==password:
        messagebox.showinfo(title='Successful Login', message='Successful Login')
    else:
        messagebox.showerror(title='Invalid Login', message='Invalid username or password')

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