from customtkinter import *
from PIL import Image, ImageTk

set_appearance_mode('dark')

root = CTk()
root.title('Guest List')
root.geometry('1000x650')
root.minsize(1000,650)
root.maxsize(1000,650)
root.config(bg='#31464c')
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

def login():
    print('Login Successfull')

# def checkbox_event():
#     print("checkbox toggled, current value:", check_var.get())

frame = CTkFrame(root, width=450, height=250, corner_radius=30, fg_color='transparent', bg_color='#ABB0B8')
frame.place(rely=0.5, relx=0.5, anchor=CENTER)
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)

# label_frame = CTkFrame(frame, width=35, height=15, fg_color='blue', bg_color='#ABB0B8', text=)
# label_frame.place(y=10, x=10)

label = CTkLabel(frame, width=40, height=40, fg_color='transparent', bg_color='#ABB0B8', text_color='black', text='Welcome', font=('sans', 20))
label.place(relx=0.5, y=30, anchor=CENTER)


# button = CTkButton(frame, width=30, height=20, text='Login', border_spacing=5)
# button.place(rely=0.5, relx=0.5, anchor=CENTER)

# check_var = StringVar(value="on")
# checkbox = CTkCheckBox(root, text="checking", command=checkbox_event,
#                                      variable=check_var, onvalue="on", offvalue="off")
# checkbox.pack(pady=50, padx=50)



root.mainloop()