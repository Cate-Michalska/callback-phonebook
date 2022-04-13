import pymysql
import config as cf
# connect mysql and Python
conn = pymysql.connect(host=cf.host, user=cf.user,
                       password=cf.password, db=cf.database, charset='utf8')
cur = conn.cursor()

# main function
# if data syntax is correct but there is no matching value, no result will be displayed


def search(find):
    '''
    Takes User Input in the var 'find'; 
    Prints either an error, no result, or the desired result; 
    A search function that delivers the row of the desired contact
    '''
    # if find is a digit, it is sorted into BITHDAY or PHONENUMBER statements
    if find.isdigit():
        if len(find) == 8:
            # if BITHDAY is an ilogical value or incorrect lenght, an error message prints
            if (int(find[-4:-1]+find[-1])) > 2022 or int(find[0:2]) > 12 or int(find[2:4]) > 31:
                print(
                    "**ERROR: Please enter a valid Phone Number, Birthday, or First and/or Last Name.")
            else:
                cur.execute(
                    "SELECT * FROM usertable WHERE BIRTHDATE = '"+find+"'")
        # if PHONENUMBER is an incorrect lenght, an error message prints
        elif len(find) == 10:
            cur.execute(
                "SELECT * FROM usertable WHERE PHONENUMBER = '"+find+"'")
        else:
            print(
                "**ERROR: Please enter a valid Phone Number, Birthday, or First and/or Last Name.")

    # if var find is not a digit, it is sorted into FIRST_NAME or LAST_NAME statement
    else:
        cur.execute("SELECT * FROM usertable WHERE FIRST_NAME = '"+find +
                    "'") or cur.execute("SELECT * FROM usertable WHERE LAST_NAME = '"+find+"'")
    # if there is a value given from the execute, the data is fetched from the table
    # if there is not a value given from the execute, the data prints as null and there is an error message
    try:
        fd = cur.fetchall()
        for i in fd:
            print("CONTACT "+str(i[1])+": "+str(i))
    except Exception as e:
        print("**ERROR: Fetch All Failed,", e)


# find var declaration and main function call
find = input("Enter First Name or Last Name, Phone Number, or Birthdate. ")
search(find)
