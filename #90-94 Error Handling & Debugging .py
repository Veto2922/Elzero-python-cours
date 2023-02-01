# -----------------------------------
# -- Errors And Exceptions Raising --
# -----------------------------------
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# -----------------------------------------------------------------

# x = -10

# if x < 0:

#     raise Exception(f"The Number {x} is less than zero ")
#     print(f"The Number {x} is less than zero 2 22 2222 ")

# else:

#     print(f"{x} is good number")


# # print("massage after if cond")

# # y = "Osama"

# # if type(y) != int:

# #     raise ValueError("only number allowed")
# #     print("only Number Alloed")


# # -----------------------------------
# # --      Exceptions Handling      --
# # -- Try | Except | Else | Finally --
# # -----------------------------------
# # Try     => Test The Code For Errors
# # Except  => Handle The Errors
# # ----------------------------
# # Else    => If No Errors
# # Finally => Run The Code
# # ------------------------==================================================


# # number = int(input("Write Your Age: "))

# # print(number)
# # print(type(number))

# # try:  # Try The Code and Test Errors

# #     number = int(input("Write Your Age: "))

# #     print("Good, This Is Integer From Try")

# # except:  # Handle The Errors If Its Found

# #     print("Bad, This is Not Integer")


# # else:  # If Theres No Errors

# #     print("Good, This Is Integer From Else")

# # finally:

# #     print("Print From Finally Whatever Happens")


# from http.client import FOUND
# from this import d
# from tkinter import X


# try:

#     # print(10/0)
#     # print(x)
#     print(int("ddd"))


# except ZeroDivisionError:

#     print("Can't divide")

# except NameError:
#     print("identifier not FOUND")

# except:
#     print("Error happens")


# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------======================================

# the_file = None
# the_tries = 5

# while the_tries > 0:

#     try:  # tre to open the file

#         print("Enter the file name with absolute path to open")
#         print(f"You have {the_tries} Tries left")
#         print("Example: D:\Python\Files\yourfile.extension")

#         file_name_and_path = input("File name => : ").strip()

#         the_file = open(file_name_and_path, "r")

#         print(the_file.read())

#         break

#     except FileNotFoundError:
#         print("file not found pleae try agian")

#         the_tries -= 1

#     except:
#         print("Error happen")

#     finally:

#         if the_file is not None:
#             the_file.close()

#             print("file closed")

#     # print(f"{the_tries} Tries Left")

#     # the_tries -= 1


# else:
#     print("All Tries is done")


# --------------------
# -- Debugging Code --
# --------------------==========================================================

my_list = [1, 2, 3]

my_dictionary = {"Name": "Osama", "Age": 36, "Country": "Egypt"}

for num in my_list:

    print(num)


for key, value in my_dictionary.items():

    print(f"{key} => {value}")


def function_one_one():

    print("Hello From Function One")


function_one_one()


# ------------------
# -- Type Hinting --
# ------------------=================================================

def say_hello(name) -> str:

  print(f"Hello {name}")


say_hello("Ahmed")


def calculate(n1, n2) -> int:
    
  print(n1 + n2)

calculate(10, 40)