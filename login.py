from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
def login():
    if usernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error','Field cannot be empty')
    elif usernameEntry.get()=='Hari Priya' or PasswordEntry.get()=='123':
        messagebox.showinfo('Sucess','Welcome')
        window.destroy()
        import StudentManagementSystem

    else:
        messagebox.showerror('Error', 'Please enter correct credentials')


window=Tk()

window.geometry('1280x700+0+0')
window.title('Login System Of Student Management System')

window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)

logoImage=PhotoImage(file='logo.png')

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame, image=usernameImage, text='Username',compound=LEFT,
                    font=('times new roman',20,'bold'), bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameRequired = Label(loginFrame, text="*", foreground="red", font=('times new roman', 20, 'bold'), bg='white')
usernameRequired.grid(row=1, column=1, sticky='w')

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

PasswordImage=PhotoImage(file='password.png')
PasswordLabel=Label(loginFrame,image=PasswordImage,text='Password',compound=LEFT,
                    font=('times new roman',20,'bold'),bg='white')
PasswordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordRequired = Label(loginFrame, text="*", foreground="red", font=('times new roman', 20, 'bold'), bg='white')
passwordRequired.grid(row=2, column=1, sticky='w')

PasswordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue',show='●')
PasswordEntry.grid(row=2,column=1,pady=10,padx=20)

LoginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',activebackground='cornflowerblue'
                   ,activeforeground='white',cursor='hand2',command=login)
LoginButton.grid(row=3,column=1,pady=10)


window.mainloop()