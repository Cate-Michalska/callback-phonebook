from distutils.util import execute
import pymysql
import random
import datetime

MYID = "1"
MYFIRSTNAME = "#### "
MYLASTNAME = "###"
MYNUMBER = "2282222312"
MYBIRTHDAY = "12252000"

CheckME = "0"
CheckNum = False
ValidDate = True
conn, cur = None, None
data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""
sql = ""


def containsNumber(data):
    for character in data:
        if character.isdigit():
            return True
    return False


# connect mysql and Python
conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='PhoneBookDB')
cur = conn.cursor()

# create table with sql code.
sql = "CREATE TABLE IF NOT EXISTS userTable (ID float, FIRST_NAME char(10), LAST_NAME char(10), PHONENUMBER BIGINT(10), BIRTHDATE BIGINT(8))"
cur.execute(sql)
row = cur.fetchone()
CheckME = row


if (CheckME == "0"):  # check Me already exists or not.
    my_Info = "INSERT INTO userTable VALUES("+MYID + \
        ",'" + MYFIRSTNAME + "','" + MYLASTNAME + \
        "'," + MYNUMBER + "," + MYBIRTHDAY + ")"
    cur.execute(my_Info)  # add my info in the contacts}

while(True):
    data1 = str(random.randint(2, 5000))  # put in random number to ID
    data2 = input("User FIRST NAME ==>")  # input name in data1
    if data2 == "":  # if input is nothing, the loop breaks
        break
    CheckNum = containsNumber(data2)
    if(CheckNum == True):
        print("please, remove number")
        break

    data3 = input("User LAST NAME ==>")
    CheckNum = containsNumber(data3)
    if(CheckNum == True):
        print("please, remove number")
        break

    data4 = input("User PhoneNumber==>")  # input number in data2
    if(len(data4) < 9):
        print("you should write more than 10 number")
        break
    data5 = input("What is your B'day? (in DD/MM/YYYY) ")  # input birth info
    day, month, year = data5.split('/')
    try:
        datetime.datetime(int(year), int(month), int(day))
        data6 = day+month+year
    except ValueError:
        ValidDate = False
    if(ValidDate == False):
        print("your birthdate is not validate, try again")
        break
    sql = "INSERT INTO userTable VALUES("+data1 + \
        ",'"+data2+"','"+data3+"',"+data4+","+data6+")"
    cur.execute(sql)


conn.commit()
conn.close()  # close the connection
