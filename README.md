# Callback? Phonebook

Jim, here is your phonebook. It saves your contacts in a MySQL database, but luckily you just need to interact with the user interface created from Python's Tkinter. All the functions you need are there, including:
* Entering contacts (Including their first name, last name, phone number, and birthday)
* Retrieving contacts
* Editing contacts
* Searching contacts
* Deleting contacts

Are you ready to try it? 

## Setup 

You'll need some tools before you can run the code:
1. [MySQL Workbench 8.0E](https://www.mysql.com/products/workbench/)
2. [Python 3.9](https://www.python.org/downloads/)
3. [PyMySQL 1.0.2](https://pypi.org/project/PyMySQL/)
  
Before we begin, you must install MySQL Workbench. We found [this tutorial](https://www.guru99.com/introduction-to-mysql-workbench.html) to be helpful. 
  
Once you have workbench installed, navigate to your SQL connection. 
![Workbench SQL Connections](documentation_screenshots\workbench_home_screen.png?raw=true "Workbench Home Screen")
  
Next, we'll create the Phonebook database that we'll call `phonebookdb`. To create the database, first create a SQL query by clicking the button to do so in the top left corner. 
![Add SQL Query](documentation_screenshots\add_sql_button.png?raw=true "Add SQL Query")
  
Type the SQL below and run it. 
```sql
CREATE DATABASE phonebookdb; 
```
![Add Database](documentation_screenshots\create_database.png?raw=true "Create Databse")

Refresh the schemas and you'll see the database there. Click on it. 
![Refresh Schemas]

Now, we'll create the table that will store all the contact information.
After clicking on the `phonebookdb`, open another SQL query, then type and run the following command:
```sql
CREATE TABLE IF NOT EXISTS `usertable` (ID float, FIRST_NAME char(10), LAST_NAME char(10), PHONENUMBER BIGINT(10), BIRTHDATE char(11));
``` 
Once you successfully run the code and refresh the schemes, you'll see a table with the appropriate columns.
![Usertable](documentation_screenshots\usertable.png?raw=true "Usertable")

As our last step of setting up the database, you'll need to add your own contact. Open a new SQL query and run the following, filling in the first, last, birthdate, and phonenumber with your information. 
```sql
INSERT INTO usertable(ID, FIRST_NAME, LAST_NAME, PHONENUMBER, BIRTHDATE) VALUES(0, "First", "Last", 1234567890, 12122000);
```

We have one last setup step before finally seeing the application. Assuming you have downloaded the code from this project, create a `config.py` file in the same directory as `main.py`. Fill in the config file with the following information, replacing the empty strings with your specific information. 
```python
# config.py

host="localhost"
user="root" # Replace if your user is different
password=""
database="phonebookdb"

MYID = "0"
MYFIRSTNAME =""
MYLASTNAME = ""
MYNUMBER = ""
MYBIRTHDAY = ""
```

Phew! That was a lot, but now you're set to run the program! In your command terminal, type:
```bash
python main.py
```
A window will pop up. Add your first contact by clicking the button in the top right. As contacts are added, you can click on the names to view their information or make changes. 
![ViewContacts](documentation_screenshots\temporary_viewcontacts_window.png?raw=true "View contacts")

## Team Members
**Project Manager** [Catherine Lukner](https://github.com/Cate-Lukner)
**Full-Stack Developer** [Taehoon Yun](https://github.com/taehoonyun)
**Front-End Developer** [David Emenike](https://github.com/Davidemenike)
**Full-Stack Developer** [Cainan Black](https://github.com/cainanBlack)
**Tester** [Allen Lowery](https://github.com/alowery23)
**Tester** [Raymond Rios](https://github.com/rayriosjr42)