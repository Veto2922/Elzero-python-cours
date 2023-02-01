
# num1 = int(input("Pleas enter the first number :").strip())
# num2 = int(input("Pleas enter the secand number :").strip())

# operation = input("Pleas enter + or - or * or / : ").strip()


# print(f"[ num1 {num1}] [operation {operation}] [num2 {num2}]")

# if operation == "+":
#     x = num1 + num2
#     print(f"{num1} {operation} {num2} = {x}")

# elif operation == "-":
#     x = num1 - num2
#     print(f"{num1} {operation} {num2} = {x}")

# elif operation == "*":
#     x = num1 * num2
#     print(f"{num1} {operation} {num2} = {x}")

# elif operation == "/":
#     x = num1 / num2
#     print(f"{num1} {operation} {num2} = {x}")

# else:
#     print("Your input is not correct pleas try agine")

# ------------------task 2 ---------------------------------------

# age = 14

# print("App Is Suitable For You") if age > 16 else print(
#     "App Is Not Suitable For You")

# # ------------------task 3 --------------------------------------------

# age = int(input("Pleas enter your age :").strip())


# if age > 10 and age < 100:
#     manths = age * 12
#     weeks = manths * 4
#     days = age * 365
#     hours = days * 24
#     menits = hours * 60
#     sacends = menits * 60

#     print(f"Your Age In Months Is {manths} Months ")
#     print(f"Your Age In weeks Is {weeks} weeks ")
#     print(f"Your Age In days Is {days} days ")
#     print(f"Your Age In hours Is {hours} hours ")
#     print(f"Your Age In menits Is {menits} menits ")
#     print(f"Your Age In Msacends Is {sacends} sacends ")

# else:
#     print("Your age  is out of scoup")

# ------------------task 4 -------------------------------------------

country = input("Input Your Country :").capitalize().strip()
countries = ["Egypt", "Palestine", "Syria",
             "Yemen", "Ksa", "Usa", "Bahrain", "England"]
price = 200
discount = 40

print(country)
print(country in countries)


if country in countries:
    dis = price - discount

    print(
        f"Your Country Eligible For Discount And The Price After Discount Is {dis}")

else:
    print(f"Your Country Not Eligible For Discount And The Price Is {price}")
