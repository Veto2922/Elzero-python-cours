# # --------------------
# # --  Control Flow  --
# # -- If, Elif, Else --
# # -- Make Decisions --
# # --------------------

# # uname = "Osama"
# # country = "KSA"
# # cname = "Python Course"
# # cPrice = 100

# # if country == "Egypt" or country == "KSA":

# #     print(f"Hello {uname} Because You Are From {country}")
# #     print(f" \"{cname}\" Price Is : ${cPrice - 80 }")

# # elif country == "KSA" or country == "Bahrain":
# #     print(f"Hello {uname} Because You Are From {country}")
# #     print(f" \"{cname}\" Price Is : ${cPrice - 60  }")

# # else:
# #     print(f"Hello {uname} Because You Are From {country}")
# #     print(f" \"{cname}\" Price Is : ${cPrice - 30}")

# # ---------------
# # -- Nested If --
# # ---------------

# uname = "Osama"
# isStudent = "yes "
# country = "KSA"
# cname = "Python Course"
# cPrice = 100

# if country == "Egypt" or country == "KSA":

#     if isStudent == "yes":
#         print(f"Hello {uname} Because You Are From {country} And Student")
#         print(f" \"{cname}\" Price Is : ${cPrice - 90 }")

#     else:
#         print(f"Hello {uname} Because You Are From {country}")
#         print(f" \"{cname}\" Price Is : ${cPrice - 80 }")


# elif country == "KSA" or country == "Bahrain":
#     print(f"Hello {uname} Because You Are From {country}")
#     print(f" \"{cname}\" Price Is : ${cPrice - 60  }")

# else:
#     print(f"Hello {uname} Because You Are From {country}")
#     print(f" \"{cname}\" Price Is : ${cPrice - 30}")


# # ----------------------------------
# # -- Ternary Conditional Operator --
# # ----------------------------------

# country = "Egypt"

# if country == "Egypt":

#     print(f"The weather in {country} Is 15C")

# elif country == "KSA":

#     print(f"The weather in {country} Is 20C")

# else:

#     print("Your country is not in the list")

# # short if
# # Condition If True | If Condition | Else | Condition If False


# movieRate = 18
# age = 19

# if age < movieRate:
#     print("Movie IS not Good for you")

# else:
#     print("Movie is good for you and happy watching :) ")

# print("Movie IS not Good for you" if age <
#       movieRate else "Movie is good for you and happy watching :) ")


# # -------------------------------------------------
# # -- Calculate Age Advanced Version and Training --
# # -------------------------------------------------

# print("#" * 80)
# print("you can write the first letter or full name of the time unit".center(
#     80, "#"))
# print("#" * 80)

# age = int(input("Please Write Your Age: ").strip())

# unit = input("choose Time Unit: Months ,Weeks , Day: ").strip().lower()

# months = age * 12
# weeks = months * 4
# days = age * 365

# if unit == "months" or unit == "m":
#     print("you Choosed The Unit Months")
#     print(f"You Lived for {months:,} Monthes.")

# elif unit == "weeks" or unit == "w":
#     print("you Choosed The Unit weeks")
#     print(f"You Lived for {weeks:,} Weeks.")

# elif unit == "day" or unit == "d":
#     print("you Choosed The Unit days")
#     print(f"You Lived for {days:,} Days.")

# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------


# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# Login
name = input("Please Type Your Name : ").strip().capitalize()

if name in admins:

    print(f"Hello {name} Welcome Back")

    option = input("Delete or update your name ?").strip().capitalize()

    if option == "Update" or option == "u":
        theNewName = input("Your New name please: ")
        admins[admins.index(name)] = theNewName

        print("Name Updated".center(40, "#"))
        print(admins)

    elif option == "Delete" or option == "d":

        admins.remove(name)
        print("Name Delete".center(40, "#"))

        print(admins)

    else:

        print("woring option try agin")


else:

    status = input(
        "You are not admin   , Add you Y , N ?").strip().capitalize()

    if status == "Yes" or status == "Y":

        print("You Have Been Added")

        admins.append(name)

        print(admins)

    else:

        print("You Are Not Added.")
