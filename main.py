from distutils.cmd import Command
import PhonebookInsert as Inserting
import PhonebookDelete as Delete
import PhonebookRead as Read
import PhonebookUpdate as Update
import PhonebookSearch as Search
from tkinter import *
from distutils.util import execute

# initial imports that will be needed
from cgitb import text
from fileinput import close
from msilib.schema import ListBox


from struct import pack
from textwrap import fill
import tkinter as tk
from tkinter.ttk import Entry
from turtle import bgcolor, color, width
from venv import create


class CallbackPhonebookMain:

    def __init__(self, *args, **kwargs):
        # the main window to be create

        self.w = tk.Canvas(master, width=350, height=200)
        self.w.configure(bg='white')
        self.entry = tk.StringVar()
        self.init = True
        self.new_name = ""

        # add contact bar and search bar with button for creating new contacts

        # new update for git push
        self.new_w = tk.Canvas(master, width=350, height=60)
        self.new_w.configure(bg="#7ed957")
        # green_label = tk.Label(new_w, text="Add Contact",background="green",foreground="white").place(x =160, y = 20)
        add_button = tk.Button(self.new_w, text="Add contact", activebackground="green",
                               activeforeground="red", height=1, command=self.contact)
        add_button.place(x=210, y=20)
        enter_label = tk.Entry(self.new_w, width="20", background="white",
                               foreground="blue", textvariable=self.entry)
        enter_label.place(x=30, y=20)
        search_button = tk.Button(self.new_w, text="Search", activebackground="green",
                                  activeforeground="red", height=1, command=lambda: [phonebook.search()]).place(x=160, y=20)

        # Owner window that contains details about the owner, including number and birthday
        self.Me_sect = tk.Canvas(master, width=350, height=80)
        self.Me_sect.configure(bg="#DDF1D4")


        me_firstName = []
        me_LastName = []
        me_Phone = []
        me_Birthinfo = []


        me_firstName, me_LastName, me_Phone, me_Birthinfo = Read.ReadData()

        self.Me_sect.create_text(
            35, 20, text="ME", fill="green", font="Helvetica 15 bold")
        self.Me_sect.create_line(22, 35, 350, 35, fill="green", width=1)
        # Me_button = tk.Button(self.Me_sect ,text = me_firstName[0], activebackground="green", fg="green",bg = "#DDF1D4",
        #                              activeforeground="red", height=1,borderwidth=0, font="Helvetica 15 bold").place(x = 20, y = 30)
        self.Me_sect.create_text(85, 50, text=me_firstName[0], fill="green",
                                 font="Helvetica 15 bold ")
        self.Me_sect.create_line(22, 65, 350, 65, fill="green", width=1)

        # contacts section that will have list of contacts
        self.contacts_sect = tk.Canvas(master, width=350, height=500)
        self.contacts_sect.create_text(90, 20, text='MY CONTACTS',
                                       fill="green", font="Helvetica 15 bold")
        # contacts section that will add list of contacts
        self.contacts_sect.create_line(22, 35, 350, 35, fill="green", width=1)

        # create buttons

        self.makeNameList()

        self.new_w.pack()
        self.Me_sect.pack()
        self.contacts_sect.pack()
        self.w.pack()

    def contact(self):
        new = tk.Toplevel(self.w)
        new.geometry("350x450")

        new.title("Add Contact")

        newContact_sect = tk.Canvas(
            new, width="350", background="#7ED957", height=120)
        newContact_sect.create_text(
            175, 60, text="ADD CONTACT", fill="white", font="Helvetica 22 bold")

        # FIRST NAME AND LAST NAME SECTION
        newContact_sect2 = tk.Canvas(
            new, width="350", background="white", height=320)

        newContact_sect2.create_text(
            65, 40, text="First Name", fill="grey", font="Helvetica 15 bold")
        firstName_entry = tk.Entry(new, width="20", background="white", foreground="black",
                                   highlightbackground="grey", highlightcolor='grey', highlightthickness=4)
        firstName_entry.place(x=14, y=180)

        newContact_sect2.create_text(
            260, 40, text='Last Name', fill="grey", font="Helvetica 15 bold")
        lastName_entry = tk.Entry(new, width='20', background='white', foreground="black",
                                  highlightcolor="grey", highlightbackground='grey', highlightthickness=4)
        lastName_entry.place(x=200, y=180)

        newContact_sect2.create_text(
            90, 110, text="Phone Number", fill='grey', font='Helvetica 15 bold')
        phoneNumber_entry = tk.Entry(new, background='white', foreground="black", highlightcolor="grey",
                                     highlightbackground='grey', highlightthickness=4)
        phoneNumber_entry.place(x=14, y=250, width=300)

        newContact_sect2.create_text(
            80, 180, text="BIRTHDAY", fill="grey", font="Helvetica 15 bold")
        birthday_entry = tk.Entry(new, background='white', foreground="black", highlightcolor="grey",
                                  highlightbackground='grey', highlightthickness=4)
        birthday_entry.place(x=14, y=320, width=300)
        if len(birthday_entry.get()) == 0:
            birthday_entry.insert(0, 0)
        # button run insert function and convey each entry data
        Submit_button = tk.Button(
            new, width='20', text="Enter", bg='#008037', height=2, command=lambda: [Inserting.insertData(firstName_entry, lastName_entry, phoneNumber_entry, birthday_entry), phonebook.refresh(), new.destroy()])
        Submit_button.place(x=14, y=355)
        newContact_sect.pack()
        newContact_sect2.pack()

    def displayContact(self, Contact, Phone_num, birthdate, contacts_ID):
        """Displays contacts"""
        new2 = tk.Toplevel(self.w)
        new2.geometry = ("350x450")
        display_sect = tk.Canvas(
            new2, width="350", background="#7ED957", height=120)
        display_sect.create_text(
            175, 60, text=(Contact), fill="white", font="Helvetica 22 bold")

        display_sect2 = tk.Canvas(
            new2, width="350", background="white", height=320)

        display_sect2.create_text(
            90, 40, text="PHONE NUMBER", fill='grey', font="Helvetica 15 bold")
        phoneNumber_entry = tk.Entry(display_sect2, text=Contact, background='white', foreground="black", highlightcolor="grey",
                                     highlightbackground='grey', highlightthickness=4, textvariable="contacts_Phone")
        phoneNumber_entry.place(x=40, y=70, width=200)
        phoneNumber_entry.delete(0, END)
        phoneNumber_entry.insert(0, Phone_num)
        phoneNumber_entry.config(state='readonly')

        display_sect2.create_text(70, 120, text="BIRTHDAY",
                                  fill="grey", font="Helvetica 15 bold")
        birthday_entry = tk.Entry(display_sect2, background="white",
                                  highlightbackground="grey", highlightthickness=4, foreground="black")
        birthday_entry.place(x=40, y=150, width=200)
        birthday_entry.insert(0, birthdate)
        birthday_entry.config(state='readonly')

        edit_contact = tk.Button(new2, text="EDIT CONTACT", fg="white", activebackground="green",
                                 bg='#008037', activeforeground="red", height=1, command=lambda Contact=Contact, Phone_num=Phone_num, birthdate=birthdate: [phonebook.editContact(Contact, Phone_num, birthdate, contacts_ID),  new2.destroy()])
        edit_contact.place(x=40, y=350)
        delete_contact = tk.Button(new2, text="DELETE CONTACT", fg="red", activebackground='green',
                                   bg='#008037', command=lambda Contact=Contact, Phone_num=Phone_num: [Delete.DeleteData(Contact, Phone_num), phonebook.refresh(), new2.destroy()], activeforeground='red', height=1)
        delete_contact.place(x=200, y=350)

        display_sect.pack()
        display_sect2.pack()

    def search(self):
        Search.ENTRYNAME = str(self.entry.get())
        if(self.entry.get() == ""):
            Search.SEARCHSTATUS = False
            phonebook.refresh()
        else:
            phonebook.Search_refresh()
            res = Search.searchData()

            """store the all information from Search"""
            Contact = res[0]
            phonenumber = res[1]  # get a phone number
            birthday = res[2]  # get a birthday number
            contacts_ID = res[3]
            display_button = tk.Button(self.contacts_sect, text=Contact, fg='green', activebackground='green', activeforeground='red',
                                       height=1, command=lambda Contact=Contact, phonenumber=phonenumber, birthday=birthday, contacts_ID=contacts_ID: self.displayContact(Contact, phonenumber, birthday, contacts_ID), borderwidth=0, font="Helvetica 15 bold").place(x=20, y=40)

    def editContact(self, Contact, Phonenum, birthdate, contacts_ID):
        new = tk.Toplevel(self.w)
        new.geometry("350x450")

        new.title("Edit Contact")

        newContact_sect = tk.Canvas(
            new, width="350", background="#7ED957", height=120)
        newContact_sect.create_text(
            175, 60, text="EDIT CONTACT", fill="white", font="Helvetica 22 bold")

        # FIRST NAME AND LAST NAME SECTION
        newContact_sect2 = tk.Canvas(
            new, width="350", background="white", height=320)

        newContact_sect2.create_text(
            65, 40, text="First Name", fill="grey", font="Helvetica 15 bold")

        a = Contact.split()

        firstName_entry = tk.Entry(new, width="20", background="white", foreground="black",
                                   highlightbackground="grey", highlightcolor='grey', highlightthickness=4)
        firstName_entry.insert(0, a[0])

        firstName_entry.place(x=14, y=180)

        newContact_sect2.create_text(
            260, 40, text='Last Name', fill="grey", font="Helvetica 15 bold")
        lastName_entry = tk.Entry(new, width='20', background='white', foreground="black",
                                  highlightcolor="grey", highlightbackground='grey', highlightthickness=4)
        lastName_entry.insert(0, a[1])
        lastName_entry.place(x=200, y=180)

        newContact_sect2.create_text(
            90, 110, text="Phone Number", fill='grey', font='Helvetica 15 bold')
        phoneNumber_entry = tk.Entry(new, background='white', foreground="black", highlightcolor="grey",
                                     highlightbackground='grey', highlightthickness=4)
        phoneNumber_entry.insert(0, Phonenum)
        phoneNumber_entry.place(x=14, y=250, width=300)

        newContact_sect2.create_text(
            80, 180, text="BIRTHDAY", fill="grey", font="Helvetica 15 bold")
        birthday_entry = tk.Entry(new, background='white', foreground="black", highlightcolor="grey",
                                  highlightbackground='grey', highlightthickness=4)
        birthday_entry.insert(0, birthdate)
        birthday_entry.place(x=14, y=320, width=300)
        if len(birthday_entry.get()) == 0:
            birthday_entry.insert(0, 0)
        # button run insert function and convey each entry data
        Submit_button = tk.Button(
            new, width='20', text="Enter", bg='#008037', height=2, command=lambda: [Update.updateData(firstName_entry, lastName_entry, phoneNumber_entry, birthday_entry, contacts_ID), phonebook.refresh(), new.destroy()])
        Submit_button.place(x=14, y=355)
        newContact_sect.pack()
        newContact_sect2.pack()

    def createContacts(self, contacts_Name, names, Phone_num, Contacts, Birthdate, index, i, contacts_ID):
        contacts_Name[index] = tk.Button(self.contacts_sect, text=names, activebackground="green", fg="green",
                                         activeforeground="red", height=1, command=lambda Phone_num=Phone_num, Contacts=Contacts, Birthdate=Birthdate, contacts_ID=contacts_ID: [self.displayContact(Contacts, Phone_num, Birthdate, contacts_ID)], borderwidth=0, font="Helvetica 15 bold")
        contacts_Name[index].place(x=20, y=40+i)
        return contacts_Name[index]

    def makeNameList(self):
        print("update")
        print(Search.SEARCHSTATUS)
        contacts_Name = []
        contacts_Phone = []
        contacts_Birhinfo = []
        contacts_ID = []
        i = 0
        index = 0
        contacts_Name, contacts_Phone, contacts_Birhinfo, contacts_ID = Read.ReadData()
        if(Search.SEARCHSTATUS == False):
            for names in contacts_Name:
                Phone_num = str(contacts_Phone[index])
                Contacts = contacts_Name[index]
                Birthdate = contacts_Birhinfo[index]
                ID = contacts_ID[index]
                self.createContacts(contacts_Name, names, Phone_num,
                                    Contacts, Birthdate, index, i, ID)
                i += 40
                index += 1

    def refresh(self):
        self.w.destroy()
        self.new_w.destroy()
        self.Me_sect.destroy()
        self.contacts_sect.destroy()
        phonebook.__init__()

    def Search_refresh(self):
        self.w.destroy()
        self.new_w.destroy()
        self.Me_sect.destroy()
        self.contacts_sect.destroy()
        Search.SEARCHSTATUS = True
        phonebook.__init__()


# running all the sections and windows created
# i noticed that the order in which you call the pack function matters


master = tk.Tk()
master.title("Callback? The Phonebook")
phonebook = CallbackPhonebookMain(master)
master.mainloop()