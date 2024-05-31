#!/usr/bin/evn python3
from tkinter import *

root = Tk()
root.title('test app')
root.minsize(1000,650)
# root.configure(bg='#f2a9e8')
# root.maxsize(1000,650)



#login background
# loginBg = Frame(root, width=700, height=350)
# loginBg.place(relx=0.5, rely=0.5, anchor='center')

#login frame
# loginFrame = Frame(root, width=100, height=100, bg='red')
# loginFrame.pack(side='')

#welcome text
welcome_text = Label(root, text='Welcome')
welcome_text.grid(column=0, row=0, columnspan=2)


#username and entry box
userLabel = Label(root, text='Username', padx=10)
username = StringVar()
userEntry = Entry(root, textvariable=username)
userLabel.grid(column=0, row=1)
userEntry.grid(column=1, row=1)

# #password and entry box
passLabel = Label(root, text='Password', pady=10)
password = StringVar()
passEntry = Entry(root, textvariable=password, show='*')
passLabel.grid(column=0, row=2)
passEntry.grid(column=1, row=2)

#login button
log_btn = Button(root, text='Login')
log_btn.grid(column=0, row=3, columnspan=2)

if __name__ == '__main__':
    root.mainloop()