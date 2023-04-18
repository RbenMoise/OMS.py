import tkinter as tk
from tkinter import  ttk
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk




#functions
def search():
    firstname = fnameentry.get()
    lastname = lnameentry.get()
    idc = id.get()
    age= agespinbox.get()
    dobc= dob.get()
    gf= pfnameentry.get()
    gl= plnameentry.get()
    titleg = ptitle.get()
    age =pagespinbox.get() 
    countryg = pcounty.get()
    allergiesm = allergies.get()
    clinicm=clinic.get()
    aillementsm = ments.get()
    effectsm = sideeffects.get()
    medsm = meds.get()
    treatmentm=treatment.get()
    
    mydb= mysql.connector.connect(
                host = 'localhost', 
                user='root',
                password='78',
                database= 'childinfo'
                )
    mycursor= mydb.cursor()
    
    try:
        mycursor.execute("SELECT * FROM details where unique_id = '" + idc + "'")
        myresult = mycursor.fetchall()
 
        for x in myresult:
            print(x)
       # firstname.delete(0, END)
        #firstname.insert(END, x[2])
        #lastname.delete(0, END)
        lnameentry.insert( x[3])
    except Exception as e:
       print(e)
       mydb.rollback()
       mydb.close()


#def clear():
def enter():
    firstname = fnameentry.get()
    lastname = lnameentry.get()
    idc = id.get()
    age= agespinbox.get()
    dobc= dob.get()
    gf= pfnameentry.get()
    gl= plnameentry.get()
    titleg = ptitle.get()
    age =pagespinbox.get() 
    countryg = pcounty.get()
    allergiesm = allergies.get()
    clinicm=clinic.get()
    aillementsm = ments.get()
    effectsm = sideeffects.get()
    medsm = meds.get()
    treatmentm=treatment.get()
    
    if (firstname=='' or lastname =='' or id== ''or age=='' or dob == ''):
        messagebox.showerror('TRY AGAIN')
    else :
        try:
            mydb= mysql.connector.connect(
                host = 'localhost', 
                user='root',
                password='78',
                database= 'childinfo'
                )
            mycursor= mydb.cursor()
            sql = 'insert into details(child_First_name, child_last_name,unique_id,child_age,DOB,Guardian_Fname,Guardian_Lname,title,age,country,allergies,clinic,aillements,effects,medical_files,treatments) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            val = (firstname, lastname,idc,age,dobc,gf,gl,titleg,age,countryg,allergiesm,clinicm,aillementsm,effectsm,medsm,treatmentm)
            mycursor.execute(sql,val)
            
            mydb.commit()
            
            messagebox.showinfo(" data entered")
           # clear()
            win.destroy()
            import login
        except mysql.connector.Error as e:
            print (e)
            messagebox.showerror("error failed to dreate ")
    
win = tk.Tk()
win.title('SinUp From')
win.geometry('900x1000')
win.configure(bg= 'yellow')
win.resizable(False,False)


frame = tk.Frame(win, width= 2000)
frame.place(x=20, y= 10)
sframe = tk.Frame(win, width=200, height=70)
sframe.place(x =700, y = 20)

#user info frame
userFrame = tk.LabelFrame(frame, text= 'User Information')
userFrame.grid(row=0,column=0,  padx=20, pady=20)
#userFrame.configure(bg='blue')

global filename, img 
def myupload():
    ftype = [('All files','*.*'),('JPG','*.jpg'),('PNG','*.png')]
    filename=filedialog.askopenfilename(filetypes=ftype)
    img= Image.open(filename)
    img =img.resize((100,100))
    img = ImageTk.PhotoImage(img)
    e1 = tk.Label(userFrame, image = img )
    e1.grid(row=10, column=0)
    e1.image = img
   # b3=tk.Button(userFrame, image=img)
    #b3.grid(column=0, row=6 , )
    #ilable.configure(image=img)
    #ilable.image = img
    
pb = tk.Button(userFrame, text= 'Upload a photo', command=lambda:myupload())
e1 = tk.Label(userFrame)
#e1.grid(column=0,row=7)



            
    
    

#for the search
slable = tk.Label(sframe,text='search').grid(column=0,row=0)
sentry = tk.Entry(sframe,).grid(column=0,row=2)
search = tk.Button(sframe, text='search',command = search ).grid(column=0, row=1)


fnamelable = tk.Label(userFrame,text='Frist Name')
fnamelable.grid(row=0,column=0)
fnameentry = tk.Entry(userFrame)
fnameentry.grid(row=2,column=0)

lnamelable = tk.Label(userFrame,text='Last Name')
lnamelable.grid(row=0,column=4)
lnameentry = tk.Entry(userFrame,)
lnameentry.grid(row=2,column=4)


id= tk.Label(userFrame, text='unique ID').grid(row=0,column=8)
id= ttk.Entry(userFrame)
id.grid(column=8,row=2)

agelable= tk.Label(userFrame,text='age')
agelable.grid(row=4,column=0)
agespinbox= tk.Spinbox(userFrame,from_=18 ,to= 100)
agespinbox.grid(row=5,column=0)

dob = tk.Label(userFrame, text='Date of Birth').grid(row=4,column=8)
dob= ttk.Entry(userFrame)
dob.grid(column=8,row=5)

for widget in userFrame.winfo_children():
    widget.grid_configure(pady=3,padx=10)
    
#parent's details
pFrame = tk.LabelFrame(frame, text= 'Parent\'s Information')
pFrame.grid(row=1,column=0,  padx=20, pady=20)
#userFrame.configure(bg='blue')

pfnamelable = tk.Label(pFrame,text='Frist Name')
pfnamelable.grid(row=0,column=0)
pfnameentry = tk.Entry(pFrame,)
pfnameentry.grid(row=2,column=0)

plnamelable = tk.Label(pFrame,text='Last Name')
plnamelable.grid(row=0,column=4)
plnameentry = tk.Entry(pFrame,)
plnameentry.grid(row=2,column=4)


ptitle = tk.Label(pFrame, text='Title').grid(row=0,column=8)
ptitle= ttk.Combobox(pFrame,values=['','Mr','Dr','sir'])
ptitle.grid(column=8,row=2)

pagelable= tk.Label(pFrame,text='age')
pagelable.grid(row=4,column=0)
pagespinbox= tk.Spinbox(pFrame,from_=18 ,to= 100)
pagespinbox.grid(row=5,column=0)

pcounty = tk.Label(pFrame, text='County').grid(row=4,column=8)
pcounty= ttk.Combobox(pFrame,values=['Nyeri','Kisumu','Nairobi','Migori'])
pcounty.grid(column=8,row=5)

for widget in pFrame.winfo_children():
    widget.grid_configure(pady=3,padx=10)    


#Medical recodrds
mFrame = tk.LabelFrame(frame, text= 'Medical Records')
mFrame.grid(row=2 ,column=0, pady=3,padx=10)
#userFrame.configure(bg='blue')

allergies = tk.Label(mFrame,text='Allergies')
allergies.grid(row=0,column=0)
allergies = tk.Entry(mFrame,)
allergies.grid(row=2,column=0)

clinic = tk.Label(mFrame,text='Clinic Attended')
clinic.grid(row=0,column=4)
clinic = tk.Entry(mFrame,)
clinic.grid(row=2,column=4)

meds = tk.Label(mFrame,text='Medical files')
meds.grid(row=4,column=4)
meds = tk.Entry(mFrame,)
meds.grid(row=5,column=4)


ments = tk.Label(mFrame, text='Aillements').grid(row=0,column=8)
ments= ttk.Combobox(mFrame,values=['cholera','hepatitis','malaria','asthma'])
ments.grid(column=8,row=2)

sideeffects= tk.Label(mFrame,text='Side Effects')
sideeffects.grid(row=4,column=0)
sideeffects= tk.Entry(mFrame)
sideeffects.grid(row=5,column=0)

treatment = tk.Label(mFrame, text='Treatments').grid(row=4,column=8)
treatment= tk.Entry(mFrame)
treatment.grid(column=8,row=5)

for widget in mFrame.winfo_children():
    widget.grid_configure(pady=3,padx=10)
    
    
#for the registration
regfram= tk.LabelFrame(frame, text='Confirm and Enter the Details')
regfram.grid(row=3 ,column=0)

reglable= tk.Label(regfram,text='Alreagr registered?')
#regcheckbox=tk.Checkbutton(regfram, text=' if the kid is already registered')
#egcheckbox.grid(row=1,column=0 )

regbutton = tk.Button(regfram,command = enter ,text='Enter')
regbutton.grid(row=0,column=0)




win.mainloop()