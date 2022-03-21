from distutils.util import execute
import pymysql

conn, cur = None, None
data1, data2, data3 = "", "", ""
sql = ""

# connect mysql and Python
conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='PhoneBookDB')
cur = conn.cursor()

# create table with sql code.
sql = "CREATE TABLE IF NOT EXISTS userTable (USERNAME char(15), PHONENUMBER int, BIRTHDATE int)"
cur.execute(sql)

while(True):
    data1 = input("User NAME ==>")  # input name in data1
    if data1 == "":  # if input is nothing, the loop breaks
        break
    data2 = input("User PhoneNumber==>")  # input number in data2
    data3 = input("User Birthday info==>")  # input birth info
    sql = "INSERT INTO userTable VALUES('"+data1 + \
        "',"+data2+","+data3+")"
    cur.execute(sql)


conn.commit()
conn.close()
