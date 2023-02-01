

# values = (0, 1, 2)

# if any(values):  # True becouse valuse contan Trous values

#     my_var = 0  # false

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]  # my_var is fales

# # fales becouse  all(my_list[:] contain 1 false value
# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

#     print("Good")


# else:

#     print("Bad")

#output is Good

# ====================task 2=======================================

# v = 40

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v))  # 820


# =================task 3 ============================================

# n = 20

# l = list(range(n))
# print(l)
# print(sum(l))

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

#     print("Good")

# Output => Good

# ===========================task 4 ===================================


# def my_all(list):
#     g = 0

#     for i in list:
#         if bool(i):
#             g += 1
#     if g == len(list):
#         return True
#     else:
#         return False


# mlist = [1, 2, 3]
# mlist2 = [1, 2, 3, []]
# print(my_all(mlist))
# print(my_all([1, 2, 0, []]))


# def my_any(list):
#     x = 0
#     for i in list:
#         if bool(i):
#             x += 1
#     if x >= 1:
#         return True
#     else:
#         return False


# print(my_any([0, 1, [], False]))  # True
# print(my_any([(), 0, False]))  # False


def my_max(list):

    x = list[0]

    for i in list:
        # print("x =", x)
        # print("i=", i)

        if i > x:
            x = i
        # print("list =", list)
    return x


print(my_max([10, 100, -20, -100, 50, 70]))
print(my_max((10, 100, -20, -100, 50, 700)))


def my_min(list):

    x = list[0]

    for i in list:
        # print("x =", x)
        # print("i=", i)

        if i < x:
            x = i
        # print("list =", list)
    return x


print(my_min((10, 100, -20, -100, 50)))  # -100
print(my_min((10, 100, -20, -100, 50)))
