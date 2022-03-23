from distutils.util import execute
import pymysql

conn, cur = None, None
# variable for name and number
data1, data2, data3, data4, data5 = "", "", "", "", ""
row = None

# connect mysql and Python

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='PhoneBookDB')
cur = conn.cursor()

# push sql code to mysql
cur.execute("SELECT * FROM userTable")

print("USER_ID  FIRST_NAME  LAST_NAME   PHONENUMBER   BIRTHINFO")
print("--------------------------------------------------------")

while(True):
    row = cur.fetchone()  # get sql row data from mysql.
    if row == None:
        break
    data1, data2, data3, data4, data5 = row  # put sql row data to data1, data2

    print("%7f %10s %10s %15d  %d" % (data1, data2, data3, data4, data5))


conn.close()  # close the connection
