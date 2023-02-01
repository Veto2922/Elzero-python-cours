# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

# from re import A


# a = 0

# while a < 15:

#     print(a)

#     a += 1

# else:
#     print("loop is done")


# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# ----------------------------

# myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# print(len(myF))

# a = 0

# while a < len(myF):  # a < 10

#     print(f"#{str(a + 1).zfill(3)} {myF[a]}")
#     a += 1  # a = a + 1

# else:
#     print("all friends are print")


# # ----------------------------
# # -- Loop => While Training --
# # -- Simple Bookmark Manage --
# # ----------------------------

# myFavouritWebs = []

# maximumWebs = 5

# while maximumWebs > 0:

#     web = input("Enter website name without https:// :")

#     myFavouritWebs.append(f"https://{web.strip().lower()}")

#     maximumWebs -= 1

#     print(f"Website Added, {maximumWebs} Places left ")

#     print(myFavouritWebs)

# else:
#     print("Bookmark is full , You can't add more")

# if len(myFavouritWebs) > 0:
#     myFavouritWebs.sort()

#     a = 0

#     print("printing the list of websites in your Bookmark")

#     while a < len(myFavouritWebs):

#         print("*" * 40)

#         print(myFavouritWebs[a])

#         a += 1

# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

tries = 4

password = "123456"

inpuPass = input("Write your password here :")

while inpuPass != password:
    tries -= 1

    print(f"wrong password , { 'last' if tries == 0 else tries } chance Left ")

    inpuPass = input("Write your password here :")

    if tries == 0:

        print("You are bloked ")

        break

else:
    print("Correct password")
