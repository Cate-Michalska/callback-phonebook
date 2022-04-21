import pymysql
import config as cf

# main function
# if data syntax is correct but there is no matching value, no result will be displayed

SEARCHSTATUS = False
ENTRYNAME = ""


def searchData(search_info):
    print(ENTRYNAME)
    print("")
    '''
    Takes User Input in the var 'search_info'; 
    Prints either an error, no result, or the desired result; 
    A search function that delivers the row of the desired contact
    '''
    # connect mysql and Python
    conn = pymysql.connect(host=cf.host, user=cf.user,
                           password=cf.password, db=cf.database)
    cur = conn.cursor()

    contacts = []

    # var that is used to search_info info
    #search_info = input("Enter First Name or Last Name, Phone Number, or Birthdate. ")

    # if search_info is a digit, it is sorted into BITHDAY or PHONENUMBER statements
    if search_info.isdigit():
        if len(search_info) == 8:
            # if BITHDAY is an ilogical value or incorrect lenght, an error message prints
            if (int(search_info[-4:-1]+search_info[-1])) > 2022 or int(search_info[0:2]) > 12 or int(search_info[2:4]) > 31:
                print(
                    "**ERROR: Please enter a valid Phone Number, Birthday, or First and/or Last Name.")
            else:
                cur.execute(
                    "SELECT FIRST_NAME, LAST_NAME, PHONENUMBER, BIRTHDATE, ID FROM usertable WHERE BIRTHDATE = '"+search_info+"'")
        # if PHONENUMBER is an incorrect lenght, an error message prints
        elif len(search_info) == 10:
            cur.execute(
                "SELECT FIRST_NAME, LAST_NAME, PHONENUMBER, BIRTHDATE, ID FROM usertable WHERE PHONENUMBER = '"+search_info+"'")
        else:
            print(
                "**ERROR: Please enter a valid Phone Number, Birthday, or First and/or Last Name.")

    # statment to return all if search is blank
    elif search_info == "" or search_info == " ":
        cur.execute(
            "SELECT FIRST_NAME, LAST_NAME, PHONENUMBER, BIRTHDATE, ID FROM usertable")

    # if var search_info is not a digit, it is sorted into FIRST_NAME or LAST_NAME statement
    else:
        cur.execute("SELECT FIRST_NAME, LAST_NAME, PHONENUMBER, BIRTHDATE,ID FROM usertable WHERE FIRST_NAME = '"+search_info +
                    "'") or cur.execute("SELECT FIRST_NAME, LAST_NAME, PHONENUMBER, BIRTHDATE, ID FROM usertable WHERE LAST_NAME = '"+search_info+"'")
    # if there is a value given from the execute, the data is fetched from the table
    # if there is not a value given from the execute, the data prints as null and there is an error message
    try:
        fd = cur.fetchall()
        for i in fd:
            contacts.append(i[0]+" "+i[1])
            """to get a phonenumber"""
            contacts.append(i[2])
            """to get a birthday info"""
            contacts.append(i[3])
            contacts.append(i[4])

    except Exception as e:
        print("**ERROR: Fetch All Failed,", e)

    if contacts == []:
        print("ERROR: Contact not found. Try a different search.")
    else:
        """now it will return ('Taehoon Yun', 2282222312, '12252000') array"""
        return contacts
    conn.close()  # close the connection
