from tkinter import *
from tkinter import messagebox
import tkinter as tk
import mysql.connector


background = '#o6283D'
framebg= '#EDEDED'
framefg='#06283D'

def clear():
    username.delete(0, END)
    phone.delete(0,END)
    memail.delete(0,END)
    passward.delete(0,END)

def signup():
    user= username.get()
    contact= phone.get()
    email= memail.get()
    password= passward.get()
    
    #print(username, contact, memail,password)
    if (user=='' or user =='UserName') or (password== ''or password=='Enter Password' ):
        messagebox.showerror('TRY AGAIN')
    else :
        try:
            mydb= mysql.connector.connect(
                host = 'localhost', 
                user='root',
                password='78',
                database= 'oms'
                )
            mycursor= mydb.cursor()
            sql = 'insert into login(user, contact, email, password) values(%s,%s,%s,%s)'
            val = (user,contact,email,password)
            mycursor.execute(sql,val)
            
            mydb.commit()
            
            messagebox.showinfo(" data entered")
            clear()
            win.destroy()
            import login
        except mysql.connector.Error as e:
            print (e)
            messagebox.showerror("error failed to dreate ")
            
      
                

win = tk.Tk()
win.title('SinUp From')
win.geometry('900x500')
win.configure(bg= 'green')
win.resizable(False,False)


    

#adding a side image
img = PhotoImage(file='login.png')
imglabel= tk.Label(win, image=img )
imglabel.place(x=50, y=100)

frame = Frame(win, width=300,height=400, bg= 'yellow')
frame.place(x=500, y=50)

heading = Label(frame, text="sign Up",bg= "yellow", font=('microsoft yahei ui light',23, 'bold' ))
heading.place(x=100, y=5)


## for the username
def entry(e):
    username.delete(0,'end')
def leave(e):
    if username.get()== '':
       username.insert(0,'Enter a name')    
    

username= Entry(frame,width=25, fg="black", border=0, bg='yellow',font=('Microsoft Yahei UI Light',11 ))
username.place(x=60,y=70)
username.insert(0,'UserName')
username.bind("<FocusIn>",entry)
username.bind("<FocusOut>",leave)

Frame(frame,width=200, height=2, bg='black').place(x=60,y=90)

#for the email
def entry(e):
    memail.delete(0,'end')
def leave(e):
    if memail.get() == '':
        memail.insert(0,'Enter Your Email Address')    
    


memail= Entry(frame,width=25, fg="black", border=0, bg='yellow',font=('Microsoft Yahei UI Light',11 ))
memail.insert(0,'Email Address')
memail.bind("<FocusIn>",entry)
memail.bind("<FocusOut>",leave)
memail.place(x=60,y=120)

Frame(frame,width=200, height=2, bg='black').place(x=60,y=145)

#for contact
def entry(e):
    phone.delete(0,'end')
def leave(e):
    if phone.get()=='':
        phone.insert(0,'Enter your phone number')   
    
phone= Entry(frame,width=25, fg="black", border=0, bg='yellow',font=('Microsoft Yahei UI Light',11 ))
phone.place(x=60,y=170)
phone.insert(0,'Phone')
phone.bind("<FocusIn>",entry)
phone.bind("<FocusOut>",leave)

Frame(frame,width=200, height=2, bg='black').place(x=60,y=200)

#for passward
def entry(e):
    passward.delete(0,'end')
def leave(e):
    if passward.get()=='':
        passward.insert(0,'Enter Password')   
    
passward= Entry(frame,width=25, fg="black", show= '#',border=0, bg='yellow',font=('Microsoft Yahei UI Light',11 ))
passward.place(x=60,y=220)
passward.insert(0,'Password')
passward.bind("<FocusIn>",entry)
passward.bind("<FocusOut>",leave)

Frame(frame,width=200, height=2, bg='black').place(x=60,y=255)
#---------------

Button(frame,width=25, pady=5, text='Sign Up', bg= 'light blue', fg= 'white', border=0 , command=signup, ).place(x=60, y=270)
hlabel = Label(frame,text='Have and account',fg='black', bg='yellow')
hlabel.place(x=90,y= 300)

signin = Button(frame, width=4,text='SignIn', border=0, bg='yellow', cursor='hand2',fg='#57a1f8' )
signin.place(x=190, y=300)










win.mainloop()