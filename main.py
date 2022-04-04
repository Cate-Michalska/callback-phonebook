import PhonebookInsert as Insert
import PhonebookDelete as Delete
import PhonebookRead as Read
from tkinter import *
from distutils.util import execute


def main():
    window = Tk()
    edtFrame = Frame(window)
    edtFrame.pack()

    btnInsert = Button(edtFrame, text="insert", width=25,
                       height=5, command=lambda: Insert.insertData())
    btnInsert.pack(side=LEFT)
    btnInsert = Button(edtFrame, text="select", width=25,
                       height=5, command=lambda: Read.ReadData())
    btnInsert.pack(side=LEFT)
    btnInsert = Button(edtFrame, text="Delete", width=25,
                       height=5, command=lambda: Delete.DeleteData())
    btnInsert.pack(side=LEFT)
    btnInsert.pack()
    window.mainloop()


if __name__ == "__main__":
    main()
