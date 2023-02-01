
# def calculate(num1, num2, operation="Add".strip().capitalize()):

#     if operation == "Add".capitalize() or operation == "A" or operation == "a":

#         print(num1 + num2)

#     elif operation == "Sub" or operation == "S" or operation == "s":

#         print(num1 - num2)

#     elif operation == "mul" or operation == "M" or operation == "m":

#         print(num1 * num2)

#     else:
#         print("This is operation not found")


# calculate(10, 20, "m")

# -------------------------task 2 -----------------------------------------------


# def addition(*numbers):

#     x = 0

#     for num in numbers:
#         print("num is :", num)

#         if num == 10:

#             continue

#         if num == 5:
#             x = x - num
#             x = x - 5

#         x = x + num
#         print(x)


# addition(10, 20, 30, 10, 15, 5, 5, 100)

# ==============task 3 ============================================================

# def show_skills(name, *skills):

#     print(f"Hello {name} your skills is :")

#     for skill in skills:

#         if len(skills) == 0:
#             print("You don't have any skills -- ")
#         else:

#             print(f"- {skill}")


# show_skills("Osama", "HTML", "CSS", "JS", "Python")

# ==============task 4 ===============================================

def say_hello(name="unKnown", age="unknown", country="unknown"):

    return f"Hello {name} Your age is {age} And you live in {country}"


print(say_hello())
