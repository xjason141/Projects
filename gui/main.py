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

frame = CTkFrame(master=root, width=300, height=150, corner_radius=30, bg_color='white')
# frame.grid(column=0, row=1)
frame.place(rely=0.5, relx=0.5, anchor=CENTER)


root.mainloop()