from distutils.util import execute
import pymysql

conn, cur = None, None
table = None
data1, data2 = "", ""
sql = ""
table = "userTable"

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='PhoneBookDB', charset='utf8')
cur = conn.cursor()
data1 = input("Which contact do you want to delete   ")
print(type(data1))
sql = "delete FROM userTable where USERNAME ='"+data1+"';"
try:
    cur.execute(sql)
    conn.commit()
    print("Record has been deleted")
except Exception as e:
    conn.rollback()
    print("Exception Occured : ", e)


conn.close()
