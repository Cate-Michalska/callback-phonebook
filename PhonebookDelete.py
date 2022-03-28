from distutils.util import execute
import pymysql

conn, cur = None, None
table = None
data1, data2, data3 = "", "", ""
sql = ""
table = "userTable"  # table name

# connect mysql and Python
conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='PhoneBookDB', charset='utf8')
cur = conn.cursor()

# push sql code to mysql
data1 = input("Which contact do you want to delete? ")
if data1 == "Taehoon":   # If you want to delete this name
    data3 = input("Could you type the ID of the person you want to remove?  ")
    if data3 == "1":  # you will check you want to delete person who has same name or me

        raise ValueError('you can not remove this contact')
    else:
        sql = "delete FROM userTable where ID ='"+data3+"';"  # Delete by ID
        try:
            cur.execute(sql)
            conn.commit()
            # if data is deleted successfully, then show this
            print("Record has been deleted")
        except Exception as e:
            conn.rollback()
            # if it find an error, it shows this.
            print("Exception Occured : ", e)
# write Last name
data2 = input("what is the last name of the person you want to delete?  ")

sql = "delete FROM userTable where FIRST_NAME ='" + \
    data1+"' and LAST_NAME='"+data2+"';"  # Delete by First name and Last name

try:
    cur.execute(sql)
    conn.commit()
    # if data is deleted successfully, then show this
    print("Record has been deleted")
except Exception as e:
    conn.rollback()
    print("Exception Occured : ", e)  # if it find an error, it shows this.


conn.close()  # close the connection
