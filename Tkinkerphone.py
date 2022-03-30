#initial imports that will be needed
from cgitb import text
from msilib.schema import ListBox
from struct import pack
from textwrap import fill
import tkinter as tk
from turtle import bgcolor, width


#the main window to be create
#eventually we will use classes and self._init_ for this one
master = tk.Tk()
master.title("Phone_book App")
w = tk.Canvas(master, width = 350, height=600)
w.configure(bg = 'white')


#add contact bar and search bar with button for creating new contacts
new_w = tk.Canvas(master, width= 350, height = 60 )
new_w.configure(bg = "#7ed957")
# green_label = tk.Label(new_w, text="Add Contact",background="green",foreground="white").place(x =160, y = 20)
add_button = tk.Button(new_w, text = "Add contact", activebackground="green", activeforeground="red",height=1).place(x = 160, y = 20)
enter_label = tk.Entry(new_w, width="20",background="white", foreground="blue").place(x = 30, y=20)



#Owner window that contains details about the owner, including number and birthday
Me_sect = tk.Canvas(master,width= 350, height=80)
Me_sect.configure(bg = "#DDF1D4")

Me_sect.create_text(35, 20, text= "ME", fill="green", font="Helvetica 15 bold")
Me_sect.create_line(22,35,350,35, fill="green", width=1)
Me_sect.create_text(70, 50, text = "COOL GAL", fill="green", font="Helvetica 15 bold ")
Me_sect.create_line(22,65,350,65, fill="green", width=1)


#contacts section that will have list of contacts 
contacts_sect = tk.Canvas(master,width = 350, height = 100)
contacts_sect.create_text(90, 20, text='MY CONTACTS', fill = "green", font = "Helvetica 15 bold")
contacts_sect.create_line(22,35,350,35, fill="green", width=1)



#running all the sections and windows created
# i noticed that the order in which you call the pack function matters
new_w.pack()
Me_sect.pack()
contacts_sect.pack()
w.pack()
master.mainloop()