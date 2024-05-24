#!/usr/bin/env python3
from customtkinter import *

set_appearance_mode('dark')

root = CTk()
root.title('Guest List')
root.geometry('1000x650')
root.minsize(1000,650)
root.maxsize(1000,650)
root.config(bg='#31464c')
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)


def login():
    print('Login Successfull')


#welcome frame
frame = CTkFrame(root, width=500, height=300, corner_radius=30, fg_color='transparent', bg_color='#ABB0B8')
frame.grid(column=1, row=1, sticky=NSEW)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)


#welcome label
label = CTkLabel(frame, bg_color='#ABB0B8', text_color='black', text='Welcome', font=('sans', 20))
label.grid(column=1, row=0, sticky=N, pady=(20,0))




# def checkbox_event():
#     print("checkbox toggled, current value:", check_var.get())


#login info
# user_label = CTkLabel(frame, width=40, height=40, fg_color='transparent')
# user_label.grid(row=1, column=0)


# button = CTkButton(frame, width=30, height=20, text='Login', border_spacing=5)
# button.place(rely=0.5, relx=0.5, anchor=CENTER)

# check_var = StringVar(value="on")
# checkbox = CTkCheckBox(root, text="checking", command=checkbox_event,
#                                      variable=check_var, onvalue="on", offvalue="off")
# checkbox.pack(pady=50, padx=50)



root.mainloop()