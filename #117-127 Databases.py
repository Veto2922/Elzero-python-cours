# ------------------------
# -- Databases => Intro --
# ------------------------
# - Database Is A Place Where We Can Store Data
# - Database Organized Into Tables (Users, Categories)
# - Tables Has Columns (ID, Username, Password)
# - There's Many Types Of Databases (MongoDB, MySQL, SQLite)
# - SQL Stand For Structured Query Language
# - SQLite => Can Run in Memory or in A Single File
# - You Can Browse File With https://sqlitebrowser.org/
# - Data Inside Database Has Types (Text, Integer, Date)
# ------------------------------------------------------


# درس 118# - قواعد البيانات - إنشاء قواعد البيانات والإتصال بها
# --------------------------------------------------------
# -- Databases => SQLite => Create Database And Connect --
# --------------------------------------------------------
# - Connect
# - Execute
# - Close
# --------------------------------------------------

# # # Import SQLite Module

# # import sqlite3

# # # Create Database And Connect
# # db = sqlite3.connect("app.db")


# # # Create The Tables and Fields
# # db.execute(
# #     "create table if not exists skills (name text, progress integer, user_id integer)")

# # # Close Database
# # db.close()


# # درس 119# - قواعد البيانات - إدخال البيانات في قاعدة البيانات
# # ------------------------------------------------------
# # -- Databases => SQLite => Insert Data Into Database --
# # ------------------------------------------------------
# # - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# # - commit => Save All Changes
# # ------------------------------------------------------

# # Import SQLite Module
# import sqlite3
# # Create Database And Connect
# db = sqlite3.connect("app.db")

# # Setting Up The Cursor
# cr = db.cursor()

# # Create The Tables and Fields
# cr.execute("create table if not exists users (user_id integer , name text)")
# cr.execute(
#     "create table if not exists skills (name text, progress integer, user_id integer)")


# # Inserting Data

# # cr.execute("insert into users(user_id , name) values(1, 'Ahmed')")
# # cr.execute("insert into users(user_id , name) values(2, 'Sayed')")
# # cr.execute("insert into users(user_id , name) values(3, 'Osama')")


# my_list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ibrahim", "Enas"]

# for key, user in enumerate(my_list):

#     cr.execute(
#         f"insert into users(user_id , name) values({key + 1}, '{user}')")

# # Save (commit)  changes

# db.commit()


# # Close Database
# db.close()


# درس 120# - قواعد البيانات SQLite - جلب البيانات من قاعدة البيانات
# --------------------------------------------------------
# -- Databases => SQLite => Retrieve Data From Database --
# --------------------------------------------------------
# - fetchone => returns a single record or None if no more rows are available.
# - fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch.
# - fetchmany(size) =>
# ------------------------------------------------------


# # Import SQLite Module
# import sqlite3
# # Create Database And Connect
# db = sqlite3.connect("app.db")

# # Setting Up The Cursor
# cr = db.cursor()

# # Create The Tables and Fields
# cr.execute("create table if not exists users (user_id integer , name text)")
# cr.execute(
#     "create table if not exists skills (name text, progress integer, user_id integer)")


# # Inserting Data

# # cr.execute("insert into users(user_id , name) values(1, 'Ahmed')")
# # cr.execute("insert into users(user_id , name) values(2, 'Sayed')")
# # cr.execute("insert into users(user_id , name) values(3, 'Osama')")


# # Fetch Data

# cr.execute("select * from users")

# # print(cr.fetchone())
# # print(cr.fetchone())
# # print(cr.fetchone())
# # print(cr.fetchone())


# # print(cr.fetchall())

# print(cr.fetchmany(2))
# # Save (commit)  changes

# db.commit()


# # Close Database
# db.close()


# درس 121# - قواعد البيانات SQLite - تدريبات على كل ما سبق
# ---------------------------------------------------
# -- Databases => SQLite => Training On Everything --
# ---------------------------------------------------

# import sqlite3


# def get_all_data():

#     try:
#         # connect to Database
#         db = sqlite3.connect("app.db")

#         print("Connected to database successfuly")

#         # setting up The cursor
#         cr = db.cursor()

#         # Fetch Data from database
#         cr.execute("select * from users")

#         # assign data to variable

#         result = cr.fetchall()

#         # print number of rows
#         print(f"The number of rows is {len(result)}")

#         # printing massage

#         print("Showing Data:")

#         # Loop On Results
#         for row in result:

#             print(f"UserID => {row[0]},", end=" ")

#             print(f"Username => {row[1]}")

#     except sqlite3.Error as er:

#         print("error reading data {er}")

#     finally:

#         if (db):

#             db.close()

#             print("connection to database is closed")


# get_all_data()


# ----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# ----------------------------------------------

# # Import SQLite Module
# import sqlite3

# # Create Database And Connect
# db = sqlite3.connect("app.db")

# # Setting Up The Cursor
# cr = db.cursor()

# # Update Data
# cr.execute("update users set name = 'Mahmoud' where user_id = 1")
# cr.execute("update users set name = 'Sayed' where user_id = 2")
# cr.execute("update users set name = 'Ameer' where user_id = 3")

# # # Delete Data
# cr.execute("delete from users where user_id = 3")

# # Fetch Data
# cr.execute("select * from users")

# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())

# # Save (Commit) Changes
# db.commit()

# # Close Database
# db.close()


# درس 123# - قواعد البيانات - SQLite إنشاء تطبيق للمهارات الجزء الأول
# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 1 --
# ----------------------------------------------------

# Import SQLite Module
from cgi import print_environ
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

# My user Id
uid = 1


def commit_and_close():
    ''' Commit changes and close connection to database    '''

    # Save (Commit) Changes
    db.commit()

    # Close Database
    db.close()
    print("Connection to database is colse")

# input Big massage


input_message = """

What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

# input Option choose
user_input = input(input_message).strip().lower()


# command list

commands_list = ["s", "a", "d", "u", "q"]


# define the method

def show_skills():

    cr.execute(f"select * from skills where user_id = '{uid}'")

    results = cr.fetchall()

    print(f"you have {len(results)} skills")

    if len(results) > 0:
        print("Showing skills with progress:")

    for row in results:

        print(f"Skill => {row[0]} , ", end="")

        print(f"progress => {row[1]} %")

        print(f"user id is {row[2]}")

    commit_and_close()


def add_skills():

    sk = input("Write skill name: ").strip().capitalize()

    cr.execute(
        f"select name from skills where name = '{sk}' and user_id = '{uid}' ")

    results = cr.fetchone()

    if results == None:

        prog = input("Write skill progress: ").strip()

        cr.execute(
            f"insert into skills(name , progress , user_id) values('{sk}' , '{prog}' , '{uid}')")

    else:

        user_des = input(
            "Skill is Exists , Do you like to update it? yes or no :").strip()

        if user_des == "yes" or user_des == "y":

            prog = input("Write new skill progress: ").strip()

            cr.execute(
                f"update skills set progress = '{prog}' where name ='{sk}' and user_id = '{uid}'")

        elif user_des == "no" or user_des == "n":
            # commit_and_close()
            pass

        else:
            print("Ok")

    print("Done")
    commit_and_close()


def delete_skills():
    sk = input("Write skill name: ").strip().capitalize()

    cr.execute(
        f"delete from skills where name ='{sk}' and user_id = '{uid}'")

    print("Done")
    commit_and_close()


def update_skills():

    sk = input("Write skill name: ").strip().capitalize()

    prog = input("Write new skill progress: ").strip()

    cr.execute(
        f"update skills set progress = '{prog}' where name ='{sk}' and user_id = '{uid}'")

    print("Done")
    commit_and_close()


# check if commend is exists

if user_input in commands_list:

    # print(f"Commands Found {user_input}")

    if user_input == "s":

        show_skills()

    elif user_input == "a":

        add_skills()

    elif user_input == "d":

        delete_skills()

    elif user_input == "u":

        update_skills()

    else:
        print("App is closed.")

        commit_and_close()

else:

    print(f"sorry this command \"{user_input}\" is not found")





# --------------------------------------------------------
# -- Databases => SQLite => Very Important Informations --
# --------------------------------------------------------

# Import SQLite Module

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

my_tuple = ('Pascal', '65', 4)

# Inserting Data
# cr.execute("insert into skills values(?, ?, ?)", my_tuple)

# Fetch Data From Database
# cr.execute("select * from skills order by name limit 3 offset 2")
# cr.execute("select * from skills where user_id > 1")
cr.execute("select * from skills where user_id not in(1, 2, 3)")

# Assign Data To Variable
results = cr.fetchall()

# Loop On Results
for row in results:

  print(f"Skill Name => {row[0]},", end=" ")
  print(f"Skill Progress => {row[1]},", end=" ")
  print(f"User ID => {row[2]}")

# Save (Commit) Changes
db.commit()

# Close Database
db.close()
