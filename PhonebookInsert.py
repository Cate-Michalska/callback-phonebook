from distutils.util import execute
import pymysql
import random
import datetime
from tkinter import *
from tkinter import messagebox
import config as cf

MYID = "1"
MYFIRSTNAME = "Taehoon "
MYLASTNAME = "Yun"
MYNUMBER = "2282222312"
MYBIRTHDAY = "12252000"

CheckME = "0"
CheckNum = False
ValidNum = False
ValidDate = False
conn, cur = None, None
data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""
sql = ""


def containsNumber(data):
    for Name in data:
        if Name.isdigit():
            return True
    return False


def validateNum(phonenum):
    if(len(phonenum) < 9):
        return True
    else:
        return False


def validateBirth(BirthdayInfo):
    month, day, year = BirthdayInfo.split('/')

    isValidDate = True
    try:
        # datetime.datetime(int(year), int(month), int(day))
        datetime.datetime(int(year), int(day), int(month))
        # datetime.datetime(int(year), int(month), int(day))
        return isValidDate
    except ValueError:
        isValidDate = False
        return isValidDate


def insertData(firstName_entry, lastName_entry, phoneNumber_entry, birthday_entry):
    conn = pymysql.connect(host=cf.host, user=cf.user,
                           password=cf.password, db=cf.database)
    cur = conn.cursor()

    # create table with sql code.
    sql = "CREATE TABLE IF NOT EXISTS userTable (ID int, FIRST_NAME char(10), LAST_NAME char(10), PHONENUMBER BIGINT(10), BIRTHDATE char(11))"
    cur.execute(sql)
    cur.execute("SELECT * FROM userTable")
    row = cur.fetchone()
    CheckME = row[0]

    # check Me already exists or not. if Me exists, then, ignore this.
    if (CheckME != 1):
        my_Info = "INSERT INTO userTable VALUES("+MYID + \
            ",'" + MYFIRSTNAME + "','" + MYLASTNAME + \
            "'," + MYNUMBER + "," + MYBIRTHDAY + ")"
        cur.execute(my_Info)  # add my info in the contacts}

    try:
        data1 = str(random.randint(2, 5000))  # put in random number to ID
        # get a data from main function. it gets first name value
        data2 = firstName_entry.get()
        CheckNum = containsNumber(data2)
        if(CheckNum == True):
            raise Exception(
                'Error', "please remove number ")  # if user add number in name entry show Error box.
            # get a data from main function. it gets last name value
            data2 = lastName_entry.get()
        data3 = lastName_entry.get()
        CheckNum = containsNumber(data3)
        if(CheckNum == True):
            raise Exception(
                'Error', "please remove number ")

        # get a data from main function. it gets phone number
        data4 = phoneNumber_entry.get()
        ValidNum = validateNum(data4)
        if(ValidNum == True):
            raise Exception(
                'Error', "please enter valid phone number ")
            data4 = phoneNumber_entry.get()
            ValidNum = validateNum(data4)

        # input birth info
        data5 = birthday_entry.get()
        print(type(data5))
        if(data5 == "0"):
            data6 = 0
        else:
            ValidDate = validateBirth(data5)
            if(ValidDate == True):
                month, day, year = data5.split('/')
                data6 = month+day+year
            else:
                raise Exception(
                    'Error', "please enter valid phone number ")
        sql = "INSERT INTO userTable VALUES("+data1 + \
            ",'"+data2+"','"+data3+"',"+data4+","+str(data6)+")"
        cur.execute(sql)
    except:
        messagebox.showerror(
            'Error', 'Please remove a number in the name or check if it is a vaid number or birthdate')
    else:
        messagebox.showinfo('succeded', 'Insert Succeded')
    conn.commit()
    conn.close()  # close the connection
