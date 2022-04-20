from tkinter import *
from random import randint
root = Tk()
lab = Label(root)
lab.pack()
count = True
button1 = 0
arr = ["1", "2", "3", "4", "5"]


def createbutton():
    global count
    button1 = Button(root, text=randint(0, 1000))
    button1.pack()
    count = False
    print("create")
    return button1


def deletebutton(a):
    a.pack_forget()
    print("delete")


def update():
    global count
    global button1
    lab['text'] = randint(0, 1000)

    for a in arr:
        if(count == True):
            button1 = Button(root, text=randint(0, 1000))
            button1.pack()
            # print(list(d.keys())[i])

            count = False

            # deletebutton(button1)
            # i += 1
        if(count == False):
            deletebutton(button1)
            button1 = createbutton()

    root.after(1000, update)  # run itself again after 1000 ms


# run first time
update()

root.mainloop()
