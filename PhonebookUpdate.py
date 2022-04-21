from distutils.util import execute
from sqlite3 import connect
import pymysql
import config as cf
from tkinter import messagebox
import datetime

conn, cur = None, None
# variable for name and number
data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""
row = None

# connect mysql and Python
conn = pymysql.connect(host=cf.host, user=cf.user,
                       password=cf.password, db=cf.database, charset='utf8')
cur = conn.cursor()


def validateBirth(BirthdayInfo):
    month, day, year = BirthdayInfo.split('/')
    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
        return isValidDate
    except ValueError:
        isValidDate = False
        return isValidDate


def updateData(firstname, lastname, number, birthdate, contacts_ID):

    data1 = firstname.get()
    data2 = lastname.get()
    data3 = number.get()
    data4 = birthdate.get()
    data6 = contacts_ID

    if(data4 == "0"):
        data5 = 0
    else:
        ValidDate = validateBirth(data4)
        if(ValidDate == True):
            month, day, year = data4.split('/')
            data5 = month+day+year
        else:
            raise Exception(
                'Error', "please enter valid birthday ")
    # update_query
    update_info = "update usertable set FIRST_NAME='" + data1 + "', LAST_NAME='" + \
        data2 + "', PHONENUMBER="+data3 + ", BIRTHDATE=" + \
        str(data5)+" where FIRST_NAME ='"+data1 + \
        "' OR LAST_NAME='"+data2+"' OR ID = "+str(data6) + ";"

    try:
        # push sql code to mysql
        cur.execute(update_info)
        conn.commit()
        print("Record Updated!")

    except Exception as e:
        print("Exception Occured : ", e)
        conn.rollback()
    else:
        messagebox.showinfo('succeded', 'Update Succeded')

    conn.close()
