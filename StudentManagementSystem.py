from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog, simpledialog
import pymysql
import pandas
from PIL._tkinter_finder import tk



#functionality part

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Sucess','Data is saved sucessfully')

def toplevel_data(title,button_text,command):
    global idEntry,nameEntry,phoneEntry,emailEntry,addressEntry,genderCombobox,dobEntry,courseEntry,yearEntry,percentageEntry, screen
    screen = Toplevel()
    screen.title(title)
    screen.resizable(False, False)
    screen.grab_set()
    idLabel = Label(screen, text='Id', font=('times new roman', 18, 'bold'),foreground='darkblue')
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text='Name', font=('times new roman', 18, 'bold'),foreground='darkblue')
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(screen, text='Phone', font=('times new roman', 18, 'bold'),foreground='darkblue')
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(screen, text='Email', font=('times new roman', 18, 'bold'),foreground='darkblue')
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(screen, text='Address', font=('times new roman', 18, 'bold'),foreground='darkblue')
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(screen, text='Gender', font=('times new roman', 18, 'bold'),foreground='darkblue')
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)

    genderCombobox = ttk.Combobox(screen, font=('roman', 15, 'bold'), width=22, state='readonly')
    genderCombobox['values'] = ('Male', 'Female', 'Other')
    genderCombobox.grid(row=5, column=1, pady=15, padx=10)
    #gender = StringVar()
    #maleRadio = Radiobutton(screen, text="Male", variable=gender, value="Male", font=('times new roman', 18, 'bold'),bg='white')
    #maleRadio.grid(row=5, column=1, pady=15, padx=(10, 100), sticky='w')

    #femaleRadio = Radiobutton(screen, text="Female", variable=gender, value="Female",font=('times new roman', 18, 'bold'), bg='white')
    #femaleRadio.grid(row=5, column=1, pady=15, padx=(100, 10), sticky='w')
    #genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    #genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(screen, text='D.O.B', font=('times new roman', 18, 'bold'),foreground='darkblue')
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=7, columnspan=2, pady=15)

    #task
    courseLabel = Label(screen, text='Course', font=('times new roman', 18, 'bold'), foreground='darkblue')
    courseLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    courseEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    courseEntry.grid(row=7, column=1, pady=15, padx=10)

    yearLabel = Label(screen, text='Year of Passing', font=('times new roman', 18, 'bold'), foreground='darkblue')
    yearLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    yearEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    yearEntry.grid(row=8, column=1, pady=15, padx=10)

    percentageLabel = Label(screen, text='Percentage', font=('times new roman', 18, 'bold'), foreground='darkblue')
    percentageLabel.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    percentageEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    percentageEntry.grid(row=9, column=1, pady=15, padx=10)
#task
    if title=='Update Student':
        indexing = studentTable.focus()
        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        phoneEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderCombobox.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])
        # task
        courseEntry.insert(0, listdata[6])
        yearEntry.insert(0, listdata[7])
        percentageEntry.insert(0, listdata[8])
        # Fetch Education Details
        query = 'select course, year_of_passing, percentage from education where student_id=%s'
        mycursor.execute(query, (listdata[0],))
        education_data = mycursor.fetchone()
        if education_data:
            course, year_of_passing, percentage = education_data
            courseEntry.insert(0, course)
            yearEntry.insert(0, year_of_passing)
            percentageEntry.insert(0, percentage)
#task

def update_data():
    query = 'update student set name=%s,email=%s,mobile=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query, (nameEntry.get(), emailEntry.get(), phoneEntry.get(),
                             addressEntry.get(), genderCombobox.get(),dobEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    #task
    #query = 'update education set course=%s, year_of_passing=%s, percentage=%s where student_id=%s'
    #mycursor.execute(query, (courseEntry.get(), yearEntry.get(), percentageEntry.get(), idEntry.get()))
    #con.commit()
    query = 'UPDATE student_education se JOIN student s ON se.id = s.id JOIN education e ON se.id = e.student_id SET se.name = %s, se.email = %s, se.mobile = %s, se.address = %s, se.gender = %s, se.dob = %s, se.date = %s, se.time = %s, se.course = %s, se.year_of_passing = %s, se.percentage = %s WHERE se.id = %s'
    mycursor.execute(query, (nameEntry.get(), emailEntry.get(), phoneEntry.get(),
                             addressEntry.get(), genderCombobox.get(), dobEntry.get(), date, currenttime,
                             courseEntry.get(), yearEntry.get(), percentageEntry.get(), idEntry.get()))
    con.commit()
#task
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_student()

def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    #task
    query = 'select s.id, s.name, s.mobile, s.email, s.address, s.gender, s.dob, s.date, s.time,e.course, e.year_of_passing, e.percentage from student s left join education e on s.id = e.student_id'
    mycursor.execute(query)
#task
    mycursor.execute(query)
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query = 'delete from student where id=%s'
    mycursor.execute(query, content_id)
    #task
    query = 'delete from education where id=%s'
    mycursor.execute(query, content_id) #
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    #task
    query = 'select * from education'
    mycursor.execute(query) #
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)
    # task

def search_data():
    query = 'select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderCombobox.get(),dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def add_data():
    if (idEntry.get()=='' or nameEntry.get()=='' or emailEntry.get()=='' or phoneEntry.get()=='' or addressEntry.get()=='' or dobEntry.get()==''or genderCombobox.get() == ''
            or courseEntry.get()==''or percentageEntry.get()==''or yearEntry.get()==''):
        messagebox.showerror('Error','All fields are required',parent=screen)
    else:
        try:
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(), nameEntry.get(), phoneEntry.get(), emailEntry.get(), addressEntry.get()
                          , genderCombobox.get(), dobEntry.get(), date, currenttime))
            #task
            query = 'insert into education values(%s, %s, %s, %s)'
            mycursor.execute(query, (idEntry.get(), courseEntry.get(), yearEntry.get(), percentageEntry.get()))
            query = 'select s.id, s.name, s.mobile, s.email, s.address, s.gender, s.dob, s.date, s.time,e.course, e.year_of_passing, e.percentage from student s left join education e on s.id = e.student_id'
            mycursor.execute(query) #
            con.commit()
            result = messagebox.askyesno('Confirm', 'Data and Education details added successfully. Do you want to clean the form?',
                                     parent=screen)
            if result:
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                phoneEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderCombobox.delete(0, END)
                dobEntry.delete(0, END)
                courseEntry.delete(0, END)
                yearEntry.delete(0, END)
                percentageEntry.delete(0, END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return
        #task
        #try:
            # Get Education Details
            #course = simpledialog.askstring("Course", "Enter the course name:")
            #year_of_passing = simpledialog.askinteger("Year of Passing", "Enter the year of passing:")
            #percentage = simpledialog.askfloat("Percentage", "Enter the percentage:")

            #Insert into Education Table
            #query = 'insert into education values(%s, %s, %s, %s)'
            #mycursor.execute(query, (int(idEntry.get()), courseEntry.get(), yearEntry.get(), percentageEntry.get()))
            #con.commit()
            #result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?',parent=screen)
            #messagebox.showinfo('Success', 'Education details added successfully.')

            #task
            #if result:
                #idEntry.delete(0, END)
                #courseEntry.delete(0, END)
                #yearEntry.delete(0, END)
                #percentageEntry.delete(0, END)
            #task
            #else:
                #pass
        #except Exception as e:
            #messagebox.showerror('Error', f"Unable to add education details: {e}", parent=screen)
        #return
#task
        query = 'select * from student'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values=data)


def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),
                                password=passwordEntry.get())
            mycursor=con.cursor()
            messagebox.showinfo('Success','Database connection is successful',parent=connectWindow)
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),Mobile varchar(10),email varchar(30),address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50)) '
            mycursor.execute(query)
            query = 'Create table education(student_id INT NOT NULL,course VARCHAR(50),year_of_passing INT,percentage FLOAT,FOREIGN KEY (student_id) REFERENCES student(id)) '
            mycursor.execute(query)
            query = 'CREATE TABLE student_education AS select s.id, s.name, s.mobile, s.email, s.address, s.gender, s.dob, s.date, s.time,e.course, e.year_of_passing, e.percentage from student s left join education e on s.id = e.student_id'
            mycursor.execute(query)
            results = mycursor.fetchall()
            for row in results:
                print(row)
            # Task modified code
# task
        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
        #Task

#Task
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportdataButton.config(state=NORMAL)

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',18,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 18, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 18, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2,show='●')
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)
def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}',foreground='darkblue')
    datetimeLabel.after(1000,clock)
#GUI part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Student Management System') #s[count] is S when count is 0

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30,foreground='darkblue')
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student (1).png')
logo_label=Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=lambda :toplevel_data('Add Student','Add Student',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=lambda :toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=lambda :toplevel_data('Update Student','Update Student',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportdataButton=ttk.Button(leftFrame,text='Export Data',width=25,state=DISABLED,command=export_data)
exportdataButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address','Gender',
                                 'D.O.B','Added Date','Added Time')
                          ,xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile No')
studentTable.heading('Email',text='Email Address')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Email',width=400,anchor=CENTER)
studentTable.column('Mobile',width=200,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Added Date',width=200,anchor=CENTER)
studentTable.column('Added Time',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),background='white',fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='darkblue')

studentTable.config(show='headings')


root.mainloop()