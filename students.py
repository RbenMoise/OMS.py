import tkinter as tk
import tkinter as tk


background= "#06283D"
framebg = "#EDEDED"
framefg= "#06283D"

win =tk.Tk()
win.title('student registration')
win.geometry('900x700')
win.config(bg=background)

#top frame
tLable =tk.Label (win, text=' student@gmail.com', height=3, bg = 'green', anchor= 'w')
tLable.pack(side='top', fill='x')
jLable =tk.Label (win, text = 'STUDENT REGISTRATION', width= 20, height = 1, bg= "#c36464", fg = '#fff', font= 'arial 20 bold')
jLable.pack(side= 'top', fill= 'x')





win.mainloop()