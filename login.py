from tkinter import *
from tkinter import messagebox
import tkinter as tk
import mysql.connector


background = '#o6283D'
framebg= '#EDEDED'
framefg='#06283D'

def clear():
    username.delete(0, END)
    passward.delete(0,END)

def login():
    if (username=='' or username =='UserName') or (passward== ''or passward=='Enter Password' ):
        messagebox.showerror('TRY AGAIN')
    else:
        try:
            mydb= mysql.connector.connect(
                host = 'localhost', 
                user='root',
                password='78',
                database= 'oms'
                )
            mycursor= mydb.cursor()
        except:
            messagebox.showerror("error failed to login ")
            return
        sql= 'use oms'
        mycursor.execute(sql)
        sql= 'select * from login where user = %s and password =%s  '
        mycursor.execute(sql, (username.get(), passward.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('error', 'invalid username and passwors')
        else:
            messagebox.showerror('successfull login')
            win.destroy()
            import content


        

            
      
                

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

heading = Label(frame, text="Login ",bg= "yellow", font=('microsoft yahei ui light',23, 'bold' ))
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

Button(frame,width=25, pady=5, text='Login ', bg= 'light blue', fg= 'white', border=0 , command=login, ).place(x=60, y=270)
hlabel = Label(frame,text='Dont have and account',fg='black', bg='yellow')
hlabel.place(x=90,y= 300)

signin = Button(frame, width=4,text='SignIn', border=0, bg='yellow', cursor='hand2',fg='#57a1f8' )
signin.place(x=190, y=300)










win.mainloop()