
# name = input("Pleas Enter Your Nmae:").strip().capitalize()

# print(f"Hello {name}, Happy To See You Here. ")

# print("*" * 100)

# -----------------------task 3------------------------------------
# age = int(input("Enter your Age:"))

# if age < 16:
#     print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# else:
#     print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


# print("*" * 100)

# -----------------------task 2------------------------------------
# first_name = input("Enter Your First Name").capitalize().strip()
# last_name = input("Enter Your last Name").capitalize().strip()

# print(f"Hello {first_name} {last_name:.1s} ")

# print("*" * 100)


# -----------------------task 2------------------------------------
email = input("Emter Your Email:").strip().lower()

user_name = email[0:email.index("@")].capitalize()
Email_s = email[email.index("@") + 1: email.index(".")]
TLD = email[email.index(".") + 1:]

print(f"Your Nmae Is {user_name}")
print(f"Email Service Provider Is {Email_s}")
print(f"Top Level Domain Is {TLD}")
