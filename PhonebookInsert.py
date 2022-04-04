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
ValidNum = False
ValidDate = False
conn, cur = None, None
data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""
sql = ""


def containsNumber(data):
    for Name in data:
        if Name.isdigit():
            return True
    return False


def validateNum(phonenum):
    if(len(phonenum) < 9):
        return True
    else:
        return False


def validateBirth(BirthdayInfo):
    month, day, year = BirthdayInfo.split('/')
    try:
        datetime.datetime(int(year), int(month), int(day))
        ValidDate = False
        return ValidDate
    except ValueError:
        print("please type vaild birthday")
        ValidDate = True
        return ValidDate

    # connect mysql and Python


def insertData():
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
        data2 = input("User FIRST NAME ==> ")  # input name in data1
        if data2 == "":  # if input is nothing, the loop breaks
            break
        CheckNum = containsNumber(data2)
        if(CheckNum == True):
            while(CheckNum):
                print("please, remove number")
                data2 = input("User FIRST NAME ==> ")
                CheckNum = containsNumber(data2)

        data3 = input("User LAST NAME ==> ")
        CheckNum = containsNumber(data3)
        if(CheckNum == True):
            while(CheckNum):
                print("please, remove number")
                data3 = input("User LAST NAME ==> ")
                CheckNum = containsNumber(data3)

        data4 = input("User PhoneNumber==>")  # input number in data2
        ValidNum = validateNum(data4)
        if(ValidNum == True):
            while(ValidNum):
                print("please enter valid phone number ")
                data4 = input("User PhoneNumber==> ")
                ValidNum = validateNum(data4)

        # input birth info
        data5 = input(
            "What is your B'day? (in MM/DD/YYYY) if you want to skip, press enter ==> ")
        if(data5 == ""):
            data6 = "0"
            continue
        ValidDate = validateBirth(data5)
        if(ValidDate == True):
            while(ValidDate):
                data5 = input("What is your B'day? (in MM/DD/YYYY) ")
                month, day, year = data5.split('/')
                data6 = month+day+year
                ValidDate = validateBirth(data5)
        else:
            month, day, year = data5.split('/')
            data6 = month+day+year

        sql = "INSERT INTO userTable VALUES("+data1 + \
            ",'"+data2+"','"+data3+"',"+data4+","+data6+")"
        cur.execute(sql)

    conn.commit()
    conn.close()  # close the connection
