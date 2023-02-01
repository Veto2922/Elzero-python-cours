# -------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------
import os

# # Main Current Working Directory
# print(os.getcwd())


# # Directory For The Opened File
# print(os.path.dirname(os.path.abspath(__file__)))

# # Change Current Working Directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(os.getcwd())

# print(os.path.abspath(__file__))

file = open(r"Veto.txt")

# --------------------------------
# -- File Handling => Read File --
# --------------------------------

my_file = open("Veto.txt", "r")

print(my_file)  # file Data object
print(my_file.name)
print(my_file.mode)
print(my_file.encoding)

# print(my_file.read())
print("*" * 40)
# print(my_file.readline())
# print(my_file.readline())

# print(my_file.readlines())
# print(my_file.readlines(30))


for line in file:

    print(line)

    if line.endswith("1"):

        break

# Close The File

my_file.close()


# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------==========================

# my_file = open("Veto.txt", "w")

# my_file.write("Hello form python file with love \n")
# my_file.write("second line")

# file2 = open("fun.txt", "w")
# file2.write("Elzero web school \n" * 1000)

# mylist = ["osama \n", "ahmed \n", "sayed \n"]

# my_file = open("Veto.txt", "w")

# my_file.writelines(mylist)


# my_file = open("Veto.txt", "a")

# my_file.write("Hello form python file with love \n")
# my_file.write("second line \n ")


# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------=======================================

import os

my_file = open("Veto.txt", "a")

# my_file.truncate(5)

# print(my_file.tell())

my_file = open("Veto.txt", "r")

my_file.seek(2)
print(my_file.read())


os.remove("D:\Python\Files\osama.txt")
