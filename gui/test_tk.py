#!/usr/bin/evn python3
from tkinter import *

root = Tk()
root.title('test app')
root.minsize(1000,650)
root.configure(bg='#c2c2c2')
# root.maxsize(1000,650)

#welcome text
welcome_text = Label(root, text='Welcome', bg='#c2c2c2', font=('arial', 13))
welcome_text.grid(column=0, row=0, columnspan=2, pady=15)


#username and entry box
userLabel = Label(root, text='Username', padx=10, bg='#c2c2c2', font=('Reddit Mono', 11))
username = StringVar()
userEntry = Entry(root, textvariable=username)
userLabel.grid(column=0, row=1)
userEntry.grid(column=1, row=1)


# #password and entry box
passLabel = Label(root, text='Password', pady=10, bg='#c2c2c2', font=('Reddit Mono', 11))
password = StringVar()
passEntry = Entry(root, textvariable=password, show='*')
passLabel.grid(column=0, row=2)
passEntry.grid(column=1, row=2)


#login button
log_btn = Button(root, text='Login', bg='#c2c2c2', font=('fangsong', 11))
log_btn.grid(column=0, row=3, columnspan=2, pady=12)


if __name__ == '__main__':
    root.mainloop()