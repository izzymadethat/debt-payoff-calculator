'''Debt Payoff Calculator'''
import customtkinter as ctk
from tkinter import messagebox as mb
from PIL import ImageTk, Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# main window
app = ctk.CTk()
app.title('Financial Freedom Calculator')
app.geometry('750x550')

# background
bg_img = ImageTk.PhotoImage(Image.open("images/bg.jpg"))
bg = ctk.CTkLabel(app, image=bg_img, text=None)
bg.place(x=0, y=0, relwidth=1, relheight=1)

# Title Frame & Widgets
title_frame = ctk.CTkFrame(app, width=220)
title_frame.pack(side='left', fill='y')

title = ctk.CTkLabel(title_frame, text='Debt Management Calculator',
                     font=ctk.CTkFont(size=30), wraplength=220)

title.pack(side='top', padx=10, pady=(50, 10))

name_box = ctk.CTkEntry(title_frame,
                        width=200,
                        placeholder_text='Enter Your First Name')
email_box = ctk.CTkEntry(title_frame,
                        width=200,
                        placeholder_text='Enter Your Email')

phone_box = ctk.CTkEntry(title_frame,
                        width=200,
                        placeholder_text='Enter Your Phone Number')

name_box.pack(padx=20, pady=(20, 10))
email_box.pack(padx=20, pady=10)
phone_box.pack(padx=20, pady=(10, 5))

exit_button = ctk.CTkButton(title_frame,
                                 text='Exit App',
                                 height=50,
                                 corner_radius=6)
exit_button.pack(side='bottom', fill = 'x', padx=50, pady=(5, 20))
clear_user_info = ctk.CTkButton(title_frame,
                                 text='Clear/Reset Info',
                                 height=50,
                                 corner_radius=6)
clear_user_info.pack(side='bottom', fill = 'x', padx=50, pady=5)
submit_user_info = ctk.CTkButton(title_frame,
                                 text='Submit Info',
                                 height=50,
                                 corner_radius=6)
submit_user_info.pack(side='bottom', fill = 'x', padx=50, pady=5)


app.mainloop()
