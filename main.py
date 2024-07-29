import ttkbootstrap as ttkb
from ttkbootstrap import *



root=ttkb.Window(themename='litera')
root.title('Quick Journal')
root.iconbitmap('logo.ico')
frame=ttkb.LabelFrame(root,padding=(50,10),width=440,height=280,bootstyle="dark")
frame.pack(padx=50,pady=40)

header=ttkb.Label(frame,text="Quick Journal ",font=('helvetica',16),bootstyle='dark')
sub_header=ttkb.Label(frame,text="Login Page ",font=('helvetica',10),bootstyle='dark')
user_name_label=ttkb.Label(frame,text='User Name : ',bootstyle='dark',font=('helvetica',14))
user_name=ttkb.Entry(frame,width=30)
password_label=ttkb.Label(frame,text='Password : ',bootstyle='dark',font=('helvetica',14))
password=ttkb.Entry(frame,width=30)
submit_btn=ttkb.Button(frame,text='Login',width=50,bootstyle='dark')
signup_btn=ttkb.Button(frame,text='Sign Up',bootstyle='link')
guest_btn=ttkb.Button(frame,text='Login as guest',bootstyle='link')



header.grid(row=0,column=0,columnspan=2)
sub_header.grid(row=1,column=0,columnspan=2)
user_name_label.grid(row=2,column=0,pady=10)
user_name.grid(row=2,column=1,pady=10)
password_label.grid(row=3,column=0,pady=10)
password.grid(row=3,column=1,pady=10)
submit_btn.grid(row=4,column=0,columnspan=2,pady=5)
signup_btn.grid(row=5,column=0)
guest_btn.grid(row=5,column=1)

root.mainloop()