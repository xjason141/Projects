from customtkinter import *


set_appearance_mode('dark')
set_default_color_theme('dark-blue')

root = CTk()
root.geometry('500x350')

def login():
    print('hello')

frame = CTkFrame(master=root)
frame.pack(pady=20, padx=30, fill='both', expand=True)

button = CTkButton(master=frame, corner_radius=34, fg_color='transparent')
button.pack(padx=50, pady=50, expand=True)

root.mainloop()