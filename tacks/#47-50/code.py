
# num = int(input("Enter number larger than 0 :"))
# X = num


# if num > 0:

#     num -= 1
#     a = 0
#     while num > a:

#         if num == 6:

#             num -= 1

#         else:

#             print(num)
#             num -= 1

#     else:
#         X -= 2
#         print(f"{X} Numbers printed successfully")


# else:

#     print(f"the number {num} not larger than 0 , pleas try again")


# ---------------------task 2 ------------------------------------------


# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

# x = len(friends)
# a = 0
# b = 0
# while x > 0 and b < 4:

#     x += 1

#     if friends[b].istitle():

#         print(friends[b])
#         b += 1

#     if friends[b].islower():
#         b += 1
#         a += 1
#         # print(b)
#         continue

# else:
#     print(f"Friends Printed And Ignored Names Count Is {a}")

#     # elif not friends[b].istitle():
#     #     a += 1
#     #     print(f"Friends Printed And Ignored Names Count Is {a}")

# ------------------------------task 3 ---------------------------------------------

# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
# a = 0
# while skills:

#     print(skills.pop(0))

# print(skills)

# ==================================task 4 ==========================================


my_friends = []

name = input("Enter name you want to add :").strip()

maxName = 4

while maxName > 0:

    if name.isupper():
        print("Invalid name")
        name = input("Enter name you want to add :").strip()

    elif name.islower():

        my_friends.append(name.title())
        print(f"Friend {name} Added => 1st Letter Become Capital")
        maxName -= 1
        print(f"Names Left in List Is {maxName}")
        print(my_friends)
        name = input("Enter name you want to add :").strip()

    elif name.istitle():

        my_friends.append(name)
        print(f"Friend {name} Added")
        maxName -= 1
        print(f"Names Left in List Is {maxName}")
        print(my_friends)
        name = input("Enter name you want to add :").strip()

    else:
        print("error try agien")
        name = input("Enter name you want to add :").strip()

else:
    print("your list is full")
