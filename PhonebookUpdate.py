from distutils.util import execute
from sqlite3 import connect
import pymysql
import config as cf
from tkinter import messagebox

conn, cur = None, None
# variable for name and number
data1, data2, data3, data4, data5 = "", "", "", "", ""
row = None

# connect mysql and Python
conn = pymysql.connect(host=cf.host, user=cf.user,
                       password=cf.password, db=cf.database, charset='utf8')
cur = conn.cursor()


def updateData(firstname, lastname, number, birthdate):

    data1 = firstname.get()
    data2 = lastname.get()
    data3 = number.get()
    data4 = birthdate.get()
    # update_query
    update_info = "update usertable set FIRST_NAME='" + data1 + "', LAST_NAME='" + \
        data2 + "', PHONENUMBER="+data3 + ", BIRTHDATE=" + \
        data4+" where FIRST_NAME ='"+data1+"' OR LAST_NAME='"+data2+"';"

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
