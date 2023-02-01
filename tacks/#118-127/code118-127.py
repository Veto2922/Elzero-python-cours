import sqlite3

db = sqlite3.connect("Database1.db")

db.execute(
    "create table if not exists data (id integer , name text , bresday text , email text )")


cr = db.cursor()

# =======================task 3 ==============================================================================
# cr.execute(
#     "insert into data (id , name , bresday , email) values(1 , 'Ahmed' , '20/10/1980' , 'a@elzero.org')")

# cr.execute(
#     "insert into data (id , name , bresday , email) values(2 , 'Sayed' , '20/10/1990' , 's@elzero.org')")
# cr.execute(
#     "insert into data (id , name , bresday , email) values(3 , 'Gamal' , '5/10/1991' , 'g@elzero.org')")
# cr.execute(
#     "insert into data (id , name , bresday , email) values(4 , 'Mahmoud' , '9/10/1987' , 'm@elzero.org')")
# cr.execute(
#     "insert into data (id , name , bresday , email) values(5 , 'Sameh' , '8/11/2000' , 's@elzero.org')")

# ==============================================================================================================
# ========task 4 ===============================
# cr.execute("select * from data where id =5")

# print(*cr.fetchall())
# =================================================


# ============task 5 ==============================

num = int(input("Pleas enter the id to delete it:"))

cr.execute(f"select id from data ")

x = cr.fetchall()
print(len(x))

if len(x) >= num:

    cr.execute(f"delete from data where id = {num}")

    print("User Deleted")

    cr.execute("select * from data")

    y = cr.fetchall()

    print("show ather data:")

    for row in y:

        print(
            f"ID => {row[0]}, Name => {row[1]}, Date Of Birth => {row[2]}, Email => {row[3]}")

else:

    print("user not found")


# Save (commit)  changes

db.commit()

db.close()
