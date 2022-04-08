from distutils.util import execute
import pymysql
import config as cf
contacts_Name = []
contacts_Phone = []
contacts_Birhinfo = []


def ReadData():
    conn, cur = None, None
    # variable for name and number
    data1, data2, data3, data4, data5 = "", "", "", "", ""
    row = None

    # connect mysql and Python

    conn = pymysql.connect(host=cf.host, user=cf.user,
                           password=cf.password, db=cf.database)
    cur = conn.cursor()

    # push sql code to mysql
    cur.execute("SELECT * FROM userTable")

    # print("USER_ID  FIRST_NAME  LAST_NAME   PHONENUMBER   BIRTHINFO")
    # print("--------------------------------------------------------")

    while(True):
        row = cur.fetchone()  # get sql row data from mysql.
        if row == None:
            break
        data1, data2, data3, data4, data5 = row  # put sql row data to data1, data2

        print("%10s %10s" % (data2, data3))
        contacts_Name.append(data2+" "+data3)
        contacts_Phone.append(data4)
        contacts_Birhinfo.append(data5)
    return contacts_Name, contacts_Phone, contacts_Birhinfo
    conn.close()  # close the connection
