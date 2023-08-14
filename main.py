'''Debt Payoff Calculator'''
import customtkinter as ctk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
from tkinter import ttk
import openpyxl

###################### Functions #############################
def switch_look():
    """Customize Appearance of App"""

    global button_on

    if button_on:
        ctk.set_appearance_mode("dark")
        app_switch.configure(text='Dark Mode')
        title.configure(text_color="#118c4f")
        button_on=False
    else:
        ctk.set_appearance_mode("light")
        app_switch.configure(text='Light Mode')
        title.configure(text_color="#5A5A5A")
        button_on=True

def clear_info():
    """Clear all User Info If Present."""

    name_content = name_box.get()
    email_content = email_box.get()
    phone_content = phone_box.get()

    if name_content:
        name_box.delete(0, ctk.END)
    if email_content:
        email_box.delete(0, ctk.END)
    if phone_content:
        phone_box.delete(0, ctk.END)

    if not name_content and not email_content and not phone_content:
        mb.showerror("Error", "No Entry Made")

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

debt_types = [
    'Credit Card',
    "Student Loan",
    "Auto",
    "Mortgage",
    "Personal Loan",
    "Medical",
    "Payday Loan",
    "Other"
]
sorted_debt = sorted(debt_types)

# main window
app = ctk.CTk()
app.title('Financial Freedom Calculator')
app.minsize(750, 550)
app.maxsize(750, 550)

# background
open_img = Image.open("images/bg.jpg")
bg_img = ctk.CTkImage(open_img, size=(1920, 960))
bg = ctk.CTkLabel(app, image=bg_img, text=None)
bg.place(x=0, y=0, relwidth=1, relheight=1)

# Title Frame & Widgets
title_frame = ctk.CTkFrame(app, width=220)
title_frame.pack(side='left', fill='y')

app_switch = ctk.CTkSwitch(title_frame, text="Light Mode", command=switch_look)
app_switch.pack(pady=10)
button_on = True

title = ctk.CTkLabel(title_frame, text='Debt Management Calculator',
                     font=ctk.CTkFont(size=30), wraplength=220)

title.pack(side='top', padx=10, pady=(20, 10))

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
                                 corner_radius=6, command=exit)
exit_button.pack(side='bottom', fill = 'x', padx=25, pady=(5, 20))
clear_user_info = ctk.CTkButton(title_frame,
                                 text='Clear/Reset Info',
                                 height=50,
                                 corner_radius=6,
                                 command=clear_info)
clear_user_info.pack(side='bottom', fill = 'x', padx=25, pady=5)
submit_user_info = ctk.CTkButton(title_frame,
                                 text='Submit Info',
                                 height=50,
                                 corner_radius=6)
submit_user_info.pack(side='bottom', fill = 'x', padx=25, pady=5)

# main process frame
app_frame = ctk.CTkFrame(app, width=500, height=550,
                        border_width=0)
app_frame.pack(fill='both', padx=10, pady=20)

# Debt Information Frame & Widgets
debt_info_frame = ctk.CTkFrame(app_frame)
debt_info_frame.pack(fill='x', padx=15, pady=10)

debt_title = ctk.CTkLabel(debt_info_frame, text="Debt Information",
                          font=ctk.CTkFont(size=20))
debt_name = ctk.CTkEntry(debt_info_frame, placeholder_text='Debt Name',
                         width=150)
debt_type_var = ctk.StringVar(value="Personal Loan")
debt_type = ctk.CTkComboBox(debt_info_frame,
                            values=sorted_debt, variable=debt_type_var)
debt_type_title = ctk.CTkLabel(debt_info_frame, text="Debt Type",
                          font=ctk.CTkFont(size=20))

balance_box = ctk.CTkEntry(debt_info_frame,
                           placeholder_text=' Current Balance Due',
                           width=150)
rate_box = ctk.CTkEntry(debt_info_frame, placeholder_text="Interest Rate",
                        width=150)
contrib_box = ctk.CTkEntry(debt_info_frame,
                           placeholder_text=
                           "Monthly Contribution",
                           width=150)

debt_title.grid(row=0, column=0, sticky='w')
debt_name.grid(row=1, column=0)
debt_type_title.grid(row=2, column=0, sticky='w')
debt_type.grid(row=2, column=1)
balance_box.grid(row=3, column=0)
rate_box.grid(row=3, column=1)
contrib_box.grid(row=3, column=2)


sep_line = ttk.Separator(app_frame)
sep_line.pack(fill='both', padx=100, pady=20)

submit_debt = ctk.CTkButton(app_frame, text='Submit Debt', height=50)
clear_debt = ctk.CTkButton(app_frame, text='Clear', height=50)

submit_debt.pack(side='left', padx=(100, 5), pady=(0, 20))
clear_debt.pack(side='right', padx=(5, 100),pady=(0, 20))

tree_frame = ctk.CTkFrame(app, height=500)
tree_frame.pack(fill='both', padx=10, pady=10)
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side='right', fill='y')

cols = ("Debt", "Type", "Current Balance", "Estimated Payoff Date")
treeview = ttk.Treeview(tree_frame, show="headings", columns=cols)
treeview.pack(fill='both')
tree_scroll.config(command=treeview.yview)


app.mainloop()
