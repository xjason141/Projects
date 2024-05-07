from customtkinter import *
from PIL import Image, ImageTk

set_appearance_mode('dark')

root = CTk()
root.title('Guest List')
root.geometry('750x550')
root.minsize(750,550)
root.config(bg='#31464c')
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)
# root.grid_rowconfigure(2, weight=1)

def login():
    print('Login Successfull')

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

frame = CTkFrame(root, width=300, height=150, corner_radius=30, bg_color='white')
frame.place(rely=0.5, relx=0.5, anchor=CENTER)
# frame.grid(column=0, row=1)

button = CTkButton(frame, width=30, height=20, text='Login', border_spacing=5)
button.place(rely=0.5, relx=0.5, anchor=CENTER)

check_var = StringVar(value="on")
checkbox = CTkCheckBox(root, text="checking", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(pady=50, padx=50)



root.mainloop()