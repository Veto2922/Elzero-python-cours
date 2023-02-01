# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------

# myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# for num in myNumbers:

#     # print(num)

#     if num % 2 == 0:  # even

#         print(f"The number {num} is even")

#     else:
#         print(f"The number {num} is odd")

# else:

#     print("THe loop is ffinished")


#

# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------

# Range

# myRange = range(1, 101)

# for number in myRange:

#     print(number)

# mySkills = {

#     "Html": "90%",
#     "Css": "60%",
#     "PHP": "70%",
#     "JS": "80%",
#     "Python": "90%",
#     "MySQL": "60%"

# }

# # print(mySkills['JS'])
# # print(mySkills.get("Python"))

# for skill in mySkills:

#     print(f"My progress in lang {skill} is: {mySkills[skill]} ")


# -----------------
# -- Loop => For --
# -- Nested Loop --
# ---------------------------===================================


# peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

# skills = ['Html', 'Css', 'Js']

# for name in peoples:  # Outer Loop

#     print(f"{name} Skills Is: ")

#     for skill in skills:

#         print(f"- {skill}")


# peoples = {
#     "Osama": {
#         "Html": "70%",
#         "Css": "80%",
#         "Js": "70%"
#     },
#     "Ahmed": {
#         "Html": "90%",
#         "Css": "80%",
#         "Js": "90%"
#     },
#     "Sayed": {
#         "Html": "70%",
#         "Css": "60%",
#         "Js": "90%"
#     }
# }

# # print(peoples["Osama"])
# # print(peoples["Sayed"]["Css"])

# for name in peoples:

#     print(f"Skills and progress for {name} is : ")

#     for skill in peoples[name]:

#         print(skill, "==>", peoples[name][skill])


# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------===============================

# myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# # Continue

# for number in myNumbers:

#     if number == 13:

#         continue

#     print(number)

# print("=" * 40)

# for number in myNumbers:

#     if number == 13:

#         break

#     print(number)


# print("=" * 40)

# for number in myNumbers:

#     if number == 13:

#         pass

#     print(number)


# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------=============================

mySkills = {
    "HTML": "80%",
    "CSS": "90%",
    "JS": "70%",
    "PHP": "80%"
}

# print(mySkills.items())


# for skill in mySkills:

#     print(f"{skill} => {mySkills[skill]}")


# for key, value in mySkills.items():

#     print(f"{key} => {value}")


myUltimateSkills = {
    "HTML": {
        "Main": "80%",
        "Pugjs": "80%"
    },
    "CSS": {
        "Main": "90%",
        "Sass": "70%"
    }
}

for key, value in myUltimateSkills.items():

    print(f"{key} Progress Is: ")

    for child_key, child_value in value.items():

        print(f"- {child_key} => {child_value}")
