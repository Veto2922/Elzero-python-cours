

# import os


# x = range(1, 51)

# # for i in x:

# #     file = open(f"txt{i}.txt", "w")

# #     file.write(f"Elzero Web School => {i}")


# file = open(f"spi25.txt", "w")


# print(os.getcwd())

# print(os.path.dirname(os.path.abspath(__file__)))

# print(file.name)
# count = 0
# # Iterate directory
# for path in os.listdir():
#     # check if current path is a file
#     if os.path.isfile(os.path.join(path)):
#         count += 1
# print('File count:', count)
# # os.rename("spi.txt", "spi25.txt")


# ====================task 2 =================================================


# file = open("txt1.txt", "a")
# file.write("\n")
# print(file.tell())

# # print(file.seek(24))

# # print(file.tell())


# i = range(1, 51)

# for n in i:

#     file.write("Appended => Elzero Web School\n")


# ========================task 3 ================================================

# from tkinter import Y


# file = open("txt1.txt", "r")
# file2 = file
# x = 0
# y = 0

# # for count, line in enumerate(file):
# #     continue
# # print('Total Lines', count + 1)


# data = file2.read()
# words = data.split()

# print("Number of words in text file :", len(words))
# print("Number of characters in text file :", len(data))

# for i in data:

#     y += 1

#     if i == "l":
#         x += 1

# print(x)

# ----------------------task 4 ==========================================


import os

x = range(40, 51)

for i in x:

    os.remove(f"txt{i}.txt")
