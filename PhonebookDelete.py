from distutils.util import execute
import pymysql
import config as cf
from tkinter import messagebox
# connect mysql and Python


def DeleteData(name, number):
    conn, cur = None, None
    table = None
    data1, data2, data3 = "", "", ""
    sql = ""
    table = "userTable"  # table name

    # connect mysql and Python
    conn = pymysql.connect(host=cf.host, user=cf.user,
                           password=cf.password, db=cf.database, charset='utf8')
    cur = conn.cursor()

    # push sql code to mysql
    data1, data2 = name.split()

    if (data1 == "Taehoon" and data2 == "Yun"):   # If you want to delete this name
        raise Exception(
            'Error', "can't delete your number")
    else:
        data3 = number
        sql = "delete FROM userTable where FIRST_NAME ='"+data1+"' and LAST_NAME = '" + \
            data2+"' and PHONENUMBER =" + data3+";"  # Delete by name and number
        try:
            cur.execute(sql)
            conn.commit()
            # if data is deleted successfully, then show this
            print("Record has been deleted")
        except Exception as e:
            conn.rollback()
            # if it find an error, it shows this.
            print("Exception Occured : ", e)
        else:
            messagebox.showinfo('succeded', 'Delete Succeded')

    conn.close()  # close the connection
