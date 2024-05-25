#!/usr/bin/evn python3
from tkinter import *

root = Tk()
root.title('test app')
root.minsize(1000,650)
# root.maxsize(1000,650)

# welcome_text = Label(text='welcome',fg='grey', pady=100, font=('arial', 20)) #to change font size, must include font type
# welcome_text.pack()

#login background
loginBg = Frame(root, width=700, height=350, bg='grey')
loginBg.place(relx=0.5, rely=0.5, anchor='center')

#login frame
loginFrame = Frame(loginBg, width=100, height=100)
loginFrame.pack(side='bottom')


#username and entry box
userLabel = Label(loginFrame, text='Username', padx= 10)
username = StringVar()
userEntry = Entry(loginFrame, textvariable=username)
userLabel.grid(column=0, row=1)
userEntry.grid(column=1, row=1)

# #password and entry box
passLabel = Label(loginFrame, text='password', pady=10)
password = StringVar()
passEntry = Entry(loginFrame, textvariable=password, show='*')
passLabel.grid(column=0, row=5)
passEntry.grid(column=1, row=5)


root.mainloop()