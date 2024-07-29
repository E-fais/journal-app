import ttkbootstrap as ttkb
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('journal')
cursor = conn.cursor()

root = ttkb.Window(themename='litera')
root.title('Quick Journal')
root.iconbitmap('logo.ico')

frame = ttkb.LabelFrame(root, padding=(50, 10), width=440, height=280, bootstyle="dark")
frame.pack(padx=50, pady=40)

# Global Entry variables
user_name = ttkb.Entry(frame, width=30)
password = ttkb.Entry(frame, width=30,)

def close_login():
    frame.pack_forget()

# User login
def submit_login():
    user_name_entry = user_name.get()
    password_entry = password.get()
    cursor.execute('SELECT * FROM users WHERE user_name=? AND password=?', (user_name_entry, password_entry))
    result = cursor.fetchone()
    if result:
        messagebox.showinfo('Success', 'Login Success')
    else:
        messagebox.showerror('Error', 'Invalid credentials')
        return
    close_login()

# Change sign up to login page
def handle_login(sub_header):
    sub_header.config(text='')
    sub_header = ttkb.Label(frame, text="Login Page", font=('helvetica', 10), bootstyle='dark')
    user_name_label = ttkb.Label(frame, text='User Name:', bootstyle='dark', font=('helvetica', 14))
    password_label = ttkb.Label(frame, text='Password:', bootstyle='dark', font=('helvetica', 14))
    submit_btn = ttkb.Button(frame, text='Login', width=50, bootstyle='dark', command=submit_login)
    signup_btn = ttkb.Button(frame, text='Sign Up', bootstyle='link', command=handle_signup)
    guest_btn = ttkb.Button(frame, text='Login as guest', bootstyle='link', command=close_login)

    sub_header.grid(row=1, column=0, columnspan=2)
    user_name_label.grid(row=2, column=0, pady=10)
    user_name.grid(row=2, column=1, pady=10)
    password_label.grid(row=3, column=0, pady=10)
    password.grid(row=3, column=1, pady=10)
    submit_btn.grid(row=4, column=0, columnspan=2, pady=5)
    signup_btn.grid(row=5, column=0)
    guest_btn.grid(row=5, column=1)

def create_user():
    user_name_entry = user_name.get()
    password_entry = password.get()
    if not user_name_entry or not password_entry:
        messagebox.showerror("Error", "Both fields are required")
        return
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS users (user_name TEXT PRIMARY KEY, password TEXT NOT NULL)')
        cursor.execute('INSERT INTO users (user_name, password) VALUES (?, ?)', (user_name_entry, password_entry))
        conn.commit()
        messagebox.showinfo('Success', 'User Created Successfully')
        handle_login(sub_header)
    except Exception as err:
        messagebox.showerror('Error', str(err))

def handle_signup():
    sub_header = ttkb.Label(frame, text="Create a new user name and password", font=('helvetica', 10), bootstyle='dark')
    sub_header.grid(row=1, column=0, columnspan=2)
    save_btn = ttkb.Button(frame, text='Save User', width=50, bootstyle='dark', command=create_user)
    save_btn.grid(row=4, column=0, columnspan=2, pady=5)
    login_btn = ttkb.Button(frame, text='Login', bootstyle='link', command=lambda: handle_login(sub_header))
    login_btn.grid(row=5, column=0)

# Initial login page setup
header = ttkb.Label(frame, text="Quick Journal", font=('helvetica', 16), bootstyle='dark')
sub_header = ttkb.Label(frame, text="Login Page", font=('helvetica', 10), bootstyle='dark')
user_name_label = ttkb.Label(frame, text='User Name:', bootstyle='dark', font=('helvetica', 14))
password_label = ttkb.Label(frame, text='Password:', bootstyle='dark', font=('helvetica', 14))
submit_btn = ttkb.Button(frame, text='Login', width=50, bootstyle='dark', command=submit_login)
signup_btn = ttkb.Button(frame, text='Sign Up', bootstyle='link', command=handle_signup)
guest_btn = ttkb.Button(frame, text='Login as guest', bootstyle='link', command=close_login)

header.grid(row=0, column=0, columnspan=2)
sub_header.grid(row=1, column=0, columnspan=2)
user_name_label.grid(row=2, column=0, pady=10)
user_name.grid(row=2, column=1, pady=10)
password_label.grid(row=3, column=0, pady=10)
password.grid(row=3, column=1, pady=10)
submit_btn.grid(row=4, column=0, columnspan=2, pady=5)
signup_btn.grid(row=5, column=0)
guest_btn.grid(row=5, column=1)

root.mainloop()
