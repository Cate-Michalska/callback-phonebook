from distutils.util import execute
import pymysql

conn, cur = None, None
data1, data2 = "", ""
row = None

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='PhoneBookDB')
cur = conn.cursor()
cur.execute("SELECT * FROM userTable")

print("USER NAME   PHONENUMBER")
print("------------------------")

while(True):
    row = cur.fetchone()
    if row == None:
        break
    data1, data2 = row

    print("%15s  %d" % (data1, data2))


conn.close()
