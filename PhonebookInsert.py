from distutils.util import execute
import pymysql

conn, cur = None, None
Me, MyNumber, data1, data2 = "", "", "", ""
sql = ""

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='PhoneBookDB')
cur = conn.cursor()
sql = "CREATE TABLE IF NOT EXISTS userTable (USERNAME char(15), PHONENUMBER int)"
cur.execute(sql)
# if Me == "":
#     Me = input("Inser my name ==> ")
#     MyNumber = input("My phone number ==> ")
#     cur.execute("INSERT INTO userTable VALUES('"+Me +
#                 "',"+MyNumber+")")
# else:
while(True):
    data1 = input("User NAME ==>")
    if data1 == "":
        break
    data2 = input("User PhoneNumber==>")
    sql = "INSERT INTO userTable VALUES('"+data1 + \
        "',"+data2+")"
    cur.execute(sql)


conn.commit()
conn.close()
