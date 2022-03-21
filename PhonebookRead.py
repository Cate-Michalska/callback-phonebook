from distutils.util import execute
import pymysql

conn, cur = None, None
data1, data2, data3 = "", "", ""  # variable for name and number
row = None

# connect mysql and Python

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='PhoneBookDB')
cur = conn.cursor()

# push sql code to mysql
cur.execute("SELECT * FROM userTable")

print("USER NAME   PHONENUMBER   BIRTHINFO")
print("------------------------")

while(True):
    row = cur.fetchone()  # get sql row data from mysql.
    if row == None:
        break
    data1, data2, data3 = row  # put sql row data to data1, data2

    print("%15s  %d  %d" % (data1, data2, data3))


conn.close()  # close the connection
