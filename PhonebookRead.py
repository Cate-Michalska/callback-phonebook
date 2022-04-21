from distutils.util import execute
import pymysql
import config as cf


def ReadData():
    contacts_Name = []
    contacts_Phone = []
    contacts_Birhinfo = []
    contacts_ID = []
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

        # print("%10s %10s" % (data2, data3))
        contacts_Name.append(data2+" "+data3)
        contacts_Phone.append(data4)
        """prevent from the case first 0 is left out"""
        if(len(data5) < 8):
            data5 = "0"+data5
            """makes month / day / year form"""
            data5 = data5[:2]+"/"+data5[2:]
            data5 = data5[:5]+"/"+data5[5:]
            contacts_Birhinfo.append(data5)
        else:
            data5 = data5[:2]+"/"+data5[2:]
            data5 = data5[:5]+"/"+data5[5:]
            contacts_Birhinfo.append(data5)
        contacts_ID.append(data1)
    return contacts_Name, contacts_Phone, contacts_Birhinfo, contacts_ID
    conn.close()  # close the connection
