

# from re import X


# my_nums = [15, 81, 5, 17, 20, 21, 13]

# my_nums.sort(reverse=True)
# print(my_nums)

# b = 1


# for num in my_nums:

#     a = num / 5

#     if a.is_integer():

#         print(f"{b} => {num}")
#         b += 1

# else:
#     print("All number printed")


# =========================task 2 ===========================================

# from re import S


# x = range(1, 21)


# for num in x:

#     if num == 6:

#         continue

#     elif num == 8:
#         continue

#     elif num == 12:
#         continue

#     else:
#         print(str(num).zfill(2))

# else:
#     print("All numbers printed")

# ====================task 3 =============================================

# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }

# a = 0  # point
# b = 0  # total point
# for rank in my_ranks:

#     if my_ranks[rank] == "A":

#         a = 100
#         b += 100

#         print(
#             f"My rank in {rank} is {my_ranks[rank]} And this equal {a} points")

#     elif my_ranks[rank] == "B":

#         a = 80
#         b += 80
#         print(
#             f"My rank in {rank} is {my_ranks[rank]} And this equal {a} points")

#     else:

#         a = 40
#         b += 40
#         print(
#             f"My rank in {rank} is {my_ranks[rank]} And this equal {a} points")

# else:
#     print(f"Total points is {b}")

# =========================task 4 ===============================================

students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

p = 0  # point
c = 0

for key in students:
    c = 0
    print("-" * 40)
    print(f"--Student name is => {key}")
    print("-" * 40)
    for value in students[key]:

        if students[key][value] == "A":

            p = 100
            c += 100
            print(f"-{value} => {p} Points")

        elif students[key][value] == "B":

            p = 80
            c += 80
            print(f"-{value} => {p} Points")

        elif students[key][value] == "C":

            p = 40
            c += 40
            print(f"-{value} => {p} Points")

        else:
            p = 20
            c += 20
            print(f"-{value} => {p} Points")

    print(f"Total Points for {key} id {c}")
