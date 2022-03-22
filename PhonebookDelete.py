from distutils.util import execute
import pymysql

conn, cur = None, None
table = None
data1 = ""
sql = ""
table = "userTable"  # table name

# connect mysql and Python
conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='PhoneBookDB', charset='utf8')
cur = conn.cursor()

# push sql code to mysql
data1 = input("Which contact do you want to delete   ")

sql = "delete FROM userTable where USERNAME ='"+data1+"';"

try:
    cur.execute(sql)
    conn.commit()
    # if data is deleted successfully, then show this
    print("Record has been deleted")
except Exception as e:
    conn.rollback()
    print("Exception Occured : ", e)  # if it find an error, it shows this.


conn.close()
