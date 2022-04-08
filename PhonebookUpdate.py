from distutils.util import execute
from sqlite3 import connect
import pymysql

conn, cur = None, None
# variable for name and number
data1, data2, data3, data4, data5 = "", "", "", "", ""
row = None

# connect mysql and Python
conn = pymysql.connect(host='127.0.0.1', user='root',
                       password='@MNmn0065', db='PhoneBookDB')
cur = conn.cursor()

while(True):
    data1 = input(
        "Which information do you want to change ==> \n 1. First Name \n 2. Last Name \n 3. Number \n 4. Birthday \n :  ")
    if data1 == "":  # if input is nothing, the loop breaks
        break
    if data1 == "1":
        data2 = input("User FIRST NAME ==> ")  # i1nput name in data1
        # update_query
        data3 = input("write the name  ")
        update_info = "update usertable set FIRST_NAME='" + \
            data3 + "' " + "where FIRST_NAME ='"+data2+"'"
    if data1 == "2":
        data2 = input("User FIRST NAME ==>")  # input name in data1
        # update_query
        data3 = input("User LAST NAME ==>")
        update_info = "update usertable set LAST_NAME='" + \
            data3 + "' " + "where FIRST_NAME ='"+data2+"'"
    if data1 == "3":
        data2 = input("wUser FIRST NAME ==> ")  # input name in data1
        # update_query
        data3 = input("User NUMBER ==>")
        update_info = "update usertable set PHONENUMBER='" + \
            data3 + "' " + "where FIRST_NAME ='"+data2+"'"
    if data1 == "4":
        data2 = input("User FIRST NAME ==> ")  # input name in data1
        # update_query
        data3 = input("User BIRTHDAY INFO ==>")
        update_info = "update usertable set BIRTHDAY='" + \
            data3 + "' " + "where FIRST_NAME ='"+data2+"'"

    try:
        # push sql code to mysql
        cur.execute(update_info)
        conn.commit()
        print("Record Updated!")

    except Exception as e:
        print("Exception Occured : ", e)
        conn.rollback()

conn.close()
